"""
Conversational Analytics + compliance flagging.

Runs over call transcripts and surfaces the things a compliance/QA team cares
about in collections: missing mini-Miranda, third-party disclosure, ignored
cease-and-desist, threats/abuse, and overall sentiment + risk score.

With Claude: full classification. Offline: transparent keyword/heuristic rules
(shown so a viewer can see exactly what fired).
"""
import llm

# pattern -> (flag label, severity 1-3)
RISK_PATTERNS = [
    (["arrest", "jail", "garnish your wages", "sue you today", "warrant"],
     "Threat / false legal claim (FDCPA 807)", 3),
    (["stop calling", "don't call me", "do not call me", "quit calling"],
     "Cease-and-desist expressed by consumer", 3),
    (["tell your", "let your", "your husband", "your wife", "your boss", "your neighbor"],
     "Possible third-party disclosure (FDCPA 805)", 3),
    (["lazy", "deadbeat", "shame", "stupid", "irresponsible"],
     "Abusive / harassing language (FDCPA 806)", 2),
]
MINI_MIRANDA = "attempt to collect a debt"
SENT_NEG = ["angry", "upset", "ridiculous", "harassing", "furious", "unacceptable", "stop"]
SENT_POS = ["thank you", "appreciate", "great", "okay", "sounds good", "happy to"]


def _text(transcript):
    return " ".join(t["text"].lower() for t in transcript["turns"])


def analyze(transcript):
    """Return dict: flags, sentiment, risk_score(0-100), engine."""
    if llm.USE_LLM:
        try:
            sys = ("You are a contact-center compliance analyst. Given a debt-collection "
                   "call transcript, return JSON: {flags:[{label,severity}], "
                   "sentiment:'positive|neutral|negative', risk_score:0-100, summary}. "
                   "Check FDCPA: mini-Miranda present, no threats, no third-party "
                   "disclosure, honored cease-and-desist.")
            body = "\n".join(f"{t['speaker']}: {t['text']}" for t in transcript["turns"])
            out = llm.complete_json(sys, body)
            out["engine"] = "Claude"
            return out
        except Exception:
            pass
    return _heuristic(transcript)


def _heuristic(transcript):
    text = _text(transcript)
    flags = []
    for phrases, label, sev in RISK_PATTERNS:
        if any(p in text for p in phrases):
            flags.append({"label": label, "severity": sev})
    # mini-Miranda required on collection calls
    if transcript.get("channel") == "voice" and MINI_MIRANDA not in text:
        flags.append({"label": "Missing mini-Miranda disclosure (FDCPA 807(11))", "severity": 2})
    # cease-and-desist honored? if consumer said stop AND agent kept pitching after
    neg = sum(text.count(w) for w in SENT_NEG)
    pos = sum(text.count(w) for w in SENT_POS)
    sentiment = "negative" if neg > pos else ("positive" if pos > neg else "neutral")
    risk = min(100, sum({1: 15, 2: 30, 3: 45}[f["severity"]] for f in flags))
    return {"flags": flags, "sentiment": sentiment, "risk_score": risk, "engine": "local"}
