"""
Agent Assist + post-call summary.

Given a transcript (and the analytics result), produce: a one-line summary, a
disposition, the next-best-action, and a real-time compliance nudge for the agent.
"""
import llm


def assist(transcript, analysis):
    if llm.USE_LLM:
        try:
            sys = ("You are a real-time agent-assist copilot for a debt-collection agent. "
                   "Given the call transcript, return JSON: {summary, disposition, "
                   "next_best_action, compliance_nudge}. disposition is one of "
                   "PTP(promise to pay)/DISPUTE/CEASE/CALLBACK/NO_CONTACT.")
            body = "\n".join(f"{t['speaker']}: {t['text']}" for t in transcript["turns"])
            out = llm.complete_json(sys, body)
            out["engine"] = "Claude"
            return out
        except Exception:
            pass
    return _heuristic(transcript, analysis)


def _heuristic(transcript, analysis):
    text = " ".join(t["text"].lower() for t in transcript["turns"])
    labels = [f["label"] for f in analysis["flags"]]

    if any("cease-and-desist" in l.lower() for l in labels):
        disp = "CEASE"
        nba = "Log cease-and-desist NOW; add to internal DNC within 10 business days; stop all calls."
        nudge = "STOP PITCHING. Consumer invoked do-not-call. Confirm removal and end call."
    elif "promise" in text or "i can pay" in text or "i'll pay" in text:
        disp = "PTP"
        nba = "Capture promise-to-pay amount + date; send written confirmation."
        nudge = "Read the validation notice; do not overstate consequences."
    elif "dispute" in text or "not my debt" in text or "wrong" in text:
        disp = "DISPUTE"
        nba = "Open dispute; pause collection on this debt until validated (Reg F)."
        nudge = "Cease collection activity until the debt is validated."
    elif any("missing mini-miranda" in l.lower() for l in labels):
        disp = "CALLBACK"
        nba = "Re-attempt with compliant script."
        nudge = "You did NOT give the mini-Miranda. Always disclose: 'this is an attempt to collect a debt.'"
    else:
        disp = "CALLBACK"
        nba = "Schedule follow-up within calling hours; respect 7-in-7 cap."
        nudge = "Stay within 8am-9pm local and the 7-in-7 attempt limit."

    summary = (f"{transcript.get('channel','voice').title()} call re debt "
               f"{transcript.get('debt_id','?')}; sentiment {analysis['sentiment']}, "
               f"risk {analysis['risk_score']}/100, {len(labels)} compliance flag(s).")
    return {"summary": summary, "disposition": disp, "next_best_action": nba,
            "compliance_nudge": nudge, "engine": "local"}
