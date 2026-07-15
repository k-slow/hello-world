"""
Natural Language Compliance (NLC) -- the piece worth building.

  plain-English rule  ->  structured predicates  ->  real-time eligibility decision

This is the reverse-engineered core of TCN's headline "AI" feature. The "AI" part
is only the English->rule translation; the value is the eligibility engine + the
auditable reason trail. We always enforce a baseline of real federal rules, then
layer whatever extra rules the user types in plain English.

Baseline rules encoded (real regs, simplified for demo):
  * Internal DNC / revoked consent      -> never contact (TCPA)
  * Known TCPA litigator                -> never contact (risk policy)
  * National DNC w/o written consent    -> deny (TCPA / TSR)
  * Calling hours 8am-9pm LOCAL         -> deny outside window (TCPA)
  * Reg F 7-in-7                         -> deny if >=7 attempts in last 7 days
  * Stricter hours for FL/NY/OK         -> mini-TCPA states, 8am-8pm
"""
import re
import llm

STRICT_STATES = {"FL", "NY", "OK"}  # mini-TCPA: tighter calling window

STATE_PHRASES = {
    "new york": "NY", "ny": "NY", "florida": "FL", "fl": "FL", "texas": "TX",
    "tx": "TX", "california": "CA", "ca": "CA", "utah": "UT", "ut": "UT",
    "oklahoma": "OK", "ok": "OK", "illinois": "IL", "il": "IL", "georgia": "GA",
    "ga": "GA", "washington": "WA", "wa": "WA", "arizona": "AZ", "az": "AZ",
}


def parse_rule(text):
    """English -> list of predicate dicts. Uses Claude if available, else keywords."""
    if not text.strip():
        return [], "none"
    if llm.USE_LLM:
        try:
            sys = ("You convert a debt-collection compliance instruction into JSON. "
                   "Output a list under key 'predicates'. Each predicate: "
                   "{type, ...}. Allowed types: block_state(state), "
                   "max_attempts(n), require_written_consent(bool), "
                   "no_call_before(hour), no_call_after(hour), block_national_dnc(bool).")
            out = llm.complete_json(sys, text)
            return out.get("predicates", []), "Claude"
        except Exception:
            pass  # fall through to local parser
    return _keyword_parse(text), "local"


def _keyword_parse(text):
    t = text.lower()
    preds = []
    blocky = any(k in t for k in ("don't call", "dont call", "no call", "skip", "block"))
    seen = set()
    for phrase, code in STATE_PHRASES.items():
        if code not in seen and blocky and re.search(r"\b" + re.escape(phrase) + r"\b", t):
            preds.append({"type": "block_state", "state": code})
            seen.add(code)
    m = re.search(r"(\d+)\s*(?:attempts|calls|times)", t)
    if m:
        preds.append({"type": "max_attempts", "n": int(m.group(1))})
    m = re.search(r"before\s*(\d+)\s*(am|pm)?", t)
    if m:
        h = int(m.group(1)) + (12 if m.group(2) == "pm" and int(m.group(1)) != 12 else 0)
        preds.append({"type": "no_call_before", "hour": h})
    m = re.search(r"after\s*(\d+)\s*(am|pm)?", t)
    if m:
        h = int(m.group(1)) + (12 if m.group(2) == "pm" and int(m.group(1)) != 12 else 0)
        preds.append({"type": "no_call_after", "hour": h})
    if "written consent" in t or "unless we have consent" in t:
        preds.append({"type": "require_written_consent", "val": True})
    if "do not call" in t or "national dnc" in t or "dnc list" in t:
        preds.append({"type": "block_national_dnc", "val": True})
    return preds


def eligible(contact, extra_preds=None):
    """Return (allow: bool, reasons: list[str]). Reasons explain every block."""
    extra_preds = extra_preds or []
    reasons = []
    hour = contact["local_hour"]

    # ---- baseline federal/risk rules (always on) ----
    if contact["consent"] == "revoked" or contact["on_internal_dnc"]:
        reasons.append("Internal DNC / consent revoked (TCPA)")
    if contact["is_known_litigator"]:
        reasons.append("Known TCPA litigator (risk policy)")
    if contact["on_national_dnc"] and contact["consent"] != "written":
        reasons.append("National DNC without written consent (TCPA/TSR)")
    low, high = (8, 20) if contact["state"] in STRICT_STATES else (8, 21)
    if hour < low or hour >= high:
        reasons.append(f"Outside calling hours {low}:00-{high}:00 local "
                       f"(now {hour}:00, {contact['state']})")
    if contact["attempts_last_7d"] >= 7:
        reasons.append(f"Reg F 7-in-7 exceeded ({contact['attempts_last_7d']} attempts/7d)")
    if contact["reassigned_risk"]:
        reasons.append("Reassigned-number risk -- verify before dialing")

    # ---- extra user rules (from the plain-English instruction) ----
    for p in extra_preds:
        ty = p.get("type")
        if ty == "block_state" and contact["state"] == p.get("state"):
            reasons.append(f"User rule: blocked state {p['state']}")
        elif ty == "max_attempts" and contact["attempts_last_7d"] >= p.get("n", 99):
            reasons.append(f"User rule: max {p['n']} attempts (has {contact['attempts_last_7d']})")
        elif ty == "require_written_consent" and contact["consent"] != "written":
            reasons.append("User rule: written consent required")
        elif ty == "no_call_before" and hour < p.get("hour", 0):
            reasons.append(f"User rule: no calls before {p['hour']}:00 (now {hour}:00)")
        elif ty == "no_call_after" and hour >= p.get("hour", 24):
            reasons.append(f"User rule: no calls after {p['hour']}:00 (now {hour}:00)")
        elif ty == "block_national_dnc" and contact["on_national_dnc"]:
            reasons.append("User rule: skip all National DNC numbers")

    return (len(reasons) == 0), reasons
