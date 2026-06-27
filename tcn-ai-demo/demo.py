"""
TCN AI components -- runnable demo.

Reverse-engineered, from-scratch versions of TCN's headline "AI" features, run
over 100 synthetic collections contacts + 12 call transcripts.

    python3 demo.py            # run everything
    python3 demo.py nlc        # Natural Language Compliance
    python3 demo.py analytics  # conversational analytics + auto-QA
    python3 demo.py assist     # agent assist
    python3 demo.py ledger     # tamper-evident consent/revocation audit ledger
    python3 demo.py llm        # check whether real-Claude wiring is live

Runs fully offline. If ANTHROPIC_API_KEY is set, the same calls upgrade to Claude.
"""
import json
import os
import sys

import llm
import nlc
import analytics
import agent_assist
import qa
import ledger

HERE = os.path.dirname(__file__)
CONTACTS = json.load(open(os.path.join(HERE, "data", "contacts.json")))
TRANSCRIPTS = json.load(open(os.path.join(HERE, "data", "transcripts.json")))
BY_ID = {c["id"]: c for c in CONTACTS}

C = {"hd": "\033[1;36m", "ok": "\033[32m", "no": "\033[31m",
     "dim": "\033[2m", "warn": "\033[33m", "x": "\033[0m"}


def banner(t):
    print(f"\n{C['hd']}{'='*74}\n  {t}\n{'='*74}{C['x']}")


def engine_line():
    print(f"{C['dim']}  engine: {llm.ENGINE}{C['x']}")


# ----------------------------------------------------------------- LLM check
def demo_llm():
    banner("0. MODEL WIRING  (offline heuristic vs. real Claude)")
    ok, msg = llm.selftest()
    color = C['ok'] if ok else C['warn']
    print(f"  {color}{msg}{C['x']}")
    print(f"  {C['dim']}set ANTHROPIC_API_KEY (and optionally ANTHROPIC_MODEL) to light up Claude.{C['x']}")


# ----------------------------------------------------------------- NLC
def demo_nlc(rule_text="Don't call anyone in New York, skip national DNC numbers, "
                       "and no more than 5 attempts in 7 days"):
    banner("1. NATURAL LANGUAGE COMPLIANCE  (plain English -> real-time eligibility)")
    engine_line()
    print(f"\n  Operator types:  {C['warn']}\"{rule_text}\"{C['x']}")
    preds, how = nlc.parse_rule(rule_text)
    print(f"  Parsed by [{how}] into machine rules:")
    for p in preds:
        print(f"      - {p}")

    allowed = blocked = 0
    samples = []
    for c in CONTACTS:
        ok, reasons = nlc.eligible(c, preds)
        allowed += ok
        blocked += (not ok)
        if not ok and len(samples) < 6:
            samples.append((c, reasons))

    print(f"\n  Scanned {len(CONTACTS)} contacts at dial time:")
    print(f"      {C['ok']}ALLOW: {allowed}{C['x']}     {C['no']}BLOCK: {blocked}{C['x']}")
    print(f"\n  Sample blocks (every block carries an audit reason):")
    for c, reasons in samples:
        print(f"    {C['no']}x{C['x']} {c['id']} {c['name']:<18} {c['state']} "
              f"{c['local_hour']:>2}:00  consent={c['consent']}")
        for r in reasons:
            print(f"         {C['dim']}- {r}{C['x']}")
    for c in CONTACTS:
        ok, _ = nlc.eligible(c, preds)
        if ok:
            print(f"    {C['ok']}OK{C['x']} {c['id']} {c['name']:<18} {c['state']} "
                  f"{c['local_hour']:>2}:00  consent={c['consent']}  -> safe to dial")
            break


# ------------------------------------------------ analytics + QA
def demo_analytics():
    banner("2. CONVERSATIONAL ANALYTICS + 3. AUTO-QA  (100% of calls scored)")
    engine_line()
    rows = []
    for t in TRANSCRIPTS:
        a = analytics.analyze(t)
        q = qa.score(t, a)
        rows.append((t, a, q))

    print(f"\n  {'call':<5}{'chan':<6}{'sent':<9}{'risk':<6}{'QA':<6}{'grade':<7}flags")
    print(f"  {C['dim']}{'-'*68}{C['x']}")
    for t, a, q in rows:
        gc = C['ok'] if q['grade'] == "PASS" else C['no']
        print(f"  {t['id']:<5}{t['channel']:<6}{a['sentiment']:<9}"
              f"{a['risk_score']:<6}{q['total']:<6}{gc}{q['grade']:<7}{C['x']}"
              f"{len(a['flags'])}")
    fails = [r for r in rows if r[2]['grade'] == "FAIL"]
    print(f"\n  {C['no']}{len(fails)} of {len(rows)} calls auto-flagged FAIL for review.{C['x']}")
    worst = max(rows, key=lambda r: r[1]['risk_score'])
    t, a, q = worst
    print(f"\n  Highest-risk call -> {t['id']} (risk {a['risk_score']}/100):")
    for f in a['flags']:
        print(f"      {C['no']}!{C['x']} [{f['severity']}] {f['label']}")


# ------------------------------------------------------- agent assist
def demo_assist():
    banner("4. AGENT ASSIST  (live next-best-action + auto summary + compliance nudge)")
    engine_line()
    for tid in ("T03", "T05", "T07"):
        t = next(x for x in TRANSCRIPTS if x["id"] == tid)
        a = analytics.analyze(t)
        r = agent_assist.assist(t, a)
        c = BY_ID.get(t["contact_id"], {})
        print(f"\n  --- {t['id']}  ({c.get('name','?')}, debt {t['debt_id']}) ---")
        print(f"  {C['dim']}summary :{C['x']} {r['summary']}")
        print(f"  {C['hd']}disposition:{C['x']} {r['disposition']}")
        print(f"  {C['ok']}next best action:{C['x']} {r['next_best_action']}")
        print(f"  {C['warn']}compliance nudge:{C['x']} {r['compliance_nudge']}")


# ------------------------------------------------------- audit ledger
def demo_ledger():
    banner("5. CONSENT / REVOCATION AUDIT LEDGER  (the part with a real moat)")
    print(f"  {C['dim']}append-only, hash-chained: every dial decision is provable in court{C['x']}")
    ledger.reset()
    base = 1_700_000_000  # fixed epoch so the demo is deterministic
    day = 86400

    # seed a couple of consent events
    ledger.append("CONSENT_GRANTED", {"contact_id": "C001", "type": "written"}, ts=base)
    ledger.append("CONSENT_REVOKED", {"contact_id": "C008", "channel": "voice"}, ts=base + day)

    # log a contact-eligibility decision for every contact (the dial-time record)
    for i, c in enumerate(CONTACTS):
        ok, reasons = nlc.eligible(c)
        ledger.append("CONTACT_ATTEMPT",
                      {"contact_id": c["id"], "decision": "ALLOW" if ok else "BLOCK",
                       "reasons": len(reasons)}, ts=base + 2 * day + i)

    recs = ledger.read_all()
    print(f"\n  Ledger now holds {len(recs)} immutable records. First few:")
    for r in recs[:4]:
        print(f"    seq {r['seq']:<3} {r['type']:<16} "
              f"{str(r['payload'])[:42]:<44} {C['dim']}hash {r['hash'][:10]}…{C['x']}")

    ok, bad = ledger.verify()
    print(f"\n  Chain integrity: {C['ok'] if ok else C['no']}"
          f"{'VALID -- not tampered' if ok else 'BROKEN at seq ' + str(bad)}{C['x']}")

    hon, detail = ledger.revocation_honored("C008")
    print(f"  Revocation honored (C008, {ledger.REVOCATION_WINDOW_DAYS}-business-day rule): "
          f"{C['ok'] if hon else C['no']}{hon}{C['x']} -- {detail}")

    # demonstrate the ledger CATCHING a violation: a rogue dial after opt-out
    ledger.append("CONTACT_ATTEMPT",
                  {"contact_id": "C008", "decision": "ALLOW", "reasons": 0}, ts=base + 5 * day)
    hon, detail = ledger.revocation_honored("C008")
    print(f"  After a rogue dial post-opt-out: {C['no'] if not hon else C['ok']}"
          f"{'VIOLATION DETECTED' if not hon else 'ok'}{C['x']} -- {detail}")

    # demonstrate tamper-evidence: edit a record in place, re-verify
    raw = open(ledger.LEDGER_PATH).read().splitlines()
    rec = json.loads(raw[3]); rec["payload"]["decision"] = "ALLOW"  # silently flip a BLOCK
    raw[3] = json.dumps(rec)
    open(ledger.LEDGER_PATH, "w").write("\n".join(raw) + "\n")
    ok, bad = ledger.verify()
    print(f"  Someone edits seq 3 to hide a block -> verify: {C['no']}"
          f"{'TAMPER DETECTED at seq ' + str(bad) if not ok else 'undetected!'}{C['x']}")
    ledger.reset()  # keep the repo clean
    print(f"  {C['dim']}(ledger reset; data/ledger.jsonl is a runtime artifact, git-ignored){C['x']}")


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"{C['hd']}TCN AI components -- reverse-engineered demo{C['x']}")
    print(f"{C['dim']}100 contacts | 12 transcripts | engine: {llm.ENGINE}{C['x']}")
    if arg in ("all", "llm"):
        demo_llm()
    if arg in ("all", "nlc"):
        demo_nlc()
    if arg in ("all", "analytics"):
        demo_analytics()
    if arg in ("all", "assist"):
        demo_assist()
    if arg in ("all", "ledger"):
        demo_ledger()
    print()


if __name__ == "__main__":
    main()
