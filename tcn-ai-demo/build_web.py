"""Pre-render analytics + ledger results to JSON for the static web demo."""
import json, os, shutil
import analytics, qa, nlc, ledger

HERE = os.path.dirname(__file__)
WEB = os.path.join(HERE, "web")
contacts = json.load(open(os.path.join(HERE, "data", "contacts.json")))
transcripts = json.load(open(os.path.join(HERE, "data", "transcripts.json")))

# contacts -> web (the JS engine runs eligibility live over these)
shutil.copy(os.path.join(HERE, "data", "contacts.json"), os.path.join(WEB, "contacts.json"))

# analytics + QA, precomputed
rows = []
for t in transcripts:
    a = analytics.analyze(t)
    q = qa.score(t, a)
    rows.append({"id": t["id"], "channel": t["channel"], "sentiment": a["sentiment"],
                 "risk": a["risk_score"], "qa": q["total"], "grade": q["grade"],
                 "flags": a["flags"]})
json.dump({"rows": rows,
           "fails": sum(1 for r in rows if r["grade"] == "FAIL")},
          open(os.path.join(WEB, "analytics.json"), "w"), indent=2)

# ledger, precomputed (mirrors demo.py section 5)
ledger.reset()
base, day = 1_700_000_000, 86400
ledger.append("CONSENT_GRANTED", {"contact_id": "C001", "type": "written"}, ts=base)
ledger.append("CONSENT_REVOKED", {"contact_id": "C008", "channel": "voice"}, ts=base + day)
for i, c in enumerate(contacts):
    ok, reasons = nlc.eligible(c)
    ledger.append("CONTACT_ATTEMPT", {"contact_id": c["id"],
                  "decision": "ALLOW" if ok else "BLOCK", "reasons": len(reasons)},
                  ts=base + 2 * day + i)
recs = ledger.read_all()
first = [{"seq": r["seq"], "type": r["type"], "payload": r["payload"],
          "hash": r["hash"][:12]} for r in recs[:4]]
ok, _ = ledger.verify()
hon, hon_detail = ledger.revocation_honored("C008")
ledger.append("CONTACT_ATTEMPT", {"contact_id": "C008", "decision": "ALLOW", "reasons": 0}, ts=base + 5 * day)
viol_ok, viol_detail = ledger.revocation_honored("C008")
raw = open(ledger.LEDGER_PATH).read().splitlines()
rec = json.loads(raw[3]); rec["payload"]["decision"] = "ALLOW"; raw[3] = json.dumps(rec)
open(ledger.LEDGER_PATH, "w").write("\n".join(raw) + "\n")
tamper_ok, tamper_bad = ledger.verify()
ledger.reset()
json.dump({"records": len(recs), "first": first, "integrity": ok,
           "revocation": {"honored": hon, "detail": hon_detail},
           "violation": {"detected": not viol_ok, "detail": viol_detail},
           "tamper": {"detected": not tamper_ok, "bad_seq": tamper_bad}},
          open(os.path.join(WEB, "ledger.json"), "w"), indent=2)
print("built web data:", os.listdir(WEB))
