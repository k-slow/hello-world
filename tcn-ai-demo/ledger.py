"""
Consent / revocation audit ledger -- the one piece with a real moat.

In a TCPA/FDCPA world the lawsuit-defining question is: "prove that at the moment
you dialed, you had the right to, and prove you honored the consumer's opt-out in
time." The defense is not the dialer or the AI -- it is an immutable, timestamped,
tamper-evident record of every consent change and every dial decision.

This is an append-only, hash-chained event log (each record commits to the hash of
the previous one), so any after-the-fact edit breaks the chain and is detectable.
That property -- not the model calls -- is what a regulator/court actually wants.

Event types:
  CONSENT_GRANTED / CONSENT_REVOKED / DNC_ADD / CONTACT_ATTEMPT
"""
import hashlib
import json
import os
import time

LEDGER_PATH = os.path.join(os.path.dirname(__file__), "data", "ledger.jsonl")
GENESIS = "0" * 64
REVOCATION_WINDOW_DAYS = 10  # FCC rule (Apr 2025): honor opt-out within 10 business days


def _hash(seq, ts, etype, payload, prev_hash):
    blob = f"{seq}|{ts}|{etype}|{json.dumps(payload, sort_keys=True)}|{prev_hash}"
    return hashlib.sha256(blob.encode()).hexdigest()


def reset():
    open(LEDGER_PATH, "w").close()


def _last():
    if not os.path.exists(LEDGER_PATH) or os.path.getsize(LEDGER_PATH) == 0:
        return None
    with open(LEDGER_PATH) as f:
        last = None
        for line in f:
            if line.strip():
                last = json.loads(line)
    return last


def append(etype, payload, ts=None):
    prev = _last()
    seq = (prev["seq"] + 1) if prev else 0
    prev_hash = prev["hash"] if prev else GENESIS
    ts = ts if ts is not None else time.time()
    rec = {"seq": seq, "ts": ts, "type": etype, "payload": payload,
           "prev_hash": prev_hash, "hash": _hash(seq, ts, etype, payload, prev_hash)}
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(rec) + "\n")
    return rec


def read_all():
    if not os.path.exists(LEDGER_PATH):
        return []
    with open(LEDGER_PATH) as f:
        return [json.loads(l) for l in f if l.strip()]


def verify():
    """Recompute the whole chain. Returns (ok, first_bad_seq_or_None)."""
    prev_hash = GENESIS
    for rec in read_all():
        expect = _hash(rec["seq"], rec["ts"], rec["type"], rec["payload"], rec["prev_hash"])
        if rec["prev_hash"] != prev_hash or rec["hash"] != expect:
            return False, rec["seq"]
        prev_hash = rec["hash"]
    return True, None


def revocation_honored(contact_id):
    """Did we stop contacting after a revocation? Returns (honored, detail)."""
    recs = [r for r in read_all() if r["payload"].get("contact_id") == contact_id]
    revoke = next((r for r in recs if r["type"] == "CONSENT_REVOKED"), None)
    if not revoke:
        return True, "no revocation on file"
    # any ALLOWED contact attempt strictly after the revocation = violation
    after = [r for r in recs if r["type"] == "CONTACT_ATTEMPT"
             and r["ts"] > revoke["ts"] and r["payload"].get("decision") == "ALLOW"]
    if after:
        return False, f"{len(after)} contact(s) AFTER opt-out -- VIOLATION"
    return True, f"opt-out at seq {revoke['seq']} honored; no contact after"
