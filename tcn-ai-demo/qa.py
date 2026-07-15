"""
Automated QA scoring -- auto-evaluate 100% of calls against a rubric.

Replaces the manual "QA listens to 2% of calls" process. Score is derived from
the compliance analysis so it is fully explainable.
"""

RUBRIC = [
    ("Identity verification", 15),
    ("Mini-Miranda / disclosure given", 20),
    ("Professional & non-abusive", 25),
    ("Honored consumer requests", 20),
    ("Resolution / next step set", 20),
]


def score(transcript, analysis):
    text = " ".join(t["text"].lower() for t in transcript["turns"])
    labels = [f["label"].lower() for f in analysis["flags"]]
    pts = {}
    pts["Identity verification"] = 15 if ("verify" in text or "confirm" in text
                                          or "date of birth" in text) else 5
    pts["Mini-Miranda / disclosure given"] = 0 if any("mini-miranda" in l for l in labels) else 20
    pts["Professional & non-abusive"] = 0 if any(("threat" in l or "abusive" in l)
                                                 for l in labels) else 25
    pts["Honored consumer requests"] = 0 if any(("cease" in l or "third-party" in l)
                                                for l in labels) else 20
    pts["Resolution / next step set"] = 20 if ("pay" in text or "follow up" in text
                                               or "call back" in text or "dispute" in text) else 8
    total = sum(pts.values())
    grade = "PASS" if total >= 80 and not any(f["severity"] == 3 for f in analysis["flags"]) else "FAIL"
    return {"total": total, "breakdown": pts, "grade": grade}
