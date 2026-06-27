# TCN AI components — reverse-engineered demo

A small, runnable demo of the **AI pieces** of TCN's contact-center platform,
rebuilt from scratch over **100 synthetic collections contacts** and **12 call
transcripts**. It demonstrates the parts that are actually "AI," not the dialer
plumbing.

> Conclusion from the teardown: TCN's AI is mostly a thin wrapper over commodity
> models. The only piece worth building is the **eligibility engine + audit trail**
> under "Natural Language Compliance." This demo builds that piece for real and
> stubs the rest with the same models TCN would call.

## Run it

```bash
cd tcn-ai-demo
python3 gen_data.py     # regenerate the 100-row dataset (already committed)
python3 demo.py         # run all four AI components
python3 demo.py nlc        # just Natural Language Compliance
python3 demo.py analytics  # just conversational analytics + auto-QA
python3 demo.py assist     # just agent assist
```

No dependencies. Pure Python 3. Runs **fully offline** with a deterministic
heuristic engine, so it always demos.

## Offline vs. real Claude

Every "AI" call routes through `llm.py`. If `ANTHROPIC_API_KEY` is set it upgrades
to real Claude; otherwise it uses a transparent local engine. Each section prints
which engine produced the result.

```bash
export ANTHROPIC_API_KEY=sk-ant-...   # optional: same demo, real model
python3 demo.py
```

## The four components

| # | Component | File | What it shows |
|---|-----------|------|---------------|
| 1 | **Natural Language Compliance** | `nlc.py` | Operator types a rule in plain English → parsed to machine predicates → real-time allow/block over 100 contacts, **every block carrying an audit reason** (TCPA hours, National DNC, Reg F 7-in-7, internal DNC, litigator, mini-TCPA states). |
| 2 | **Conversational Analytics** | `analytics.py` | Scores 100% of transcripts for FDCPA risk: threats, missing mini-Miranda, third-party disclosure, cease-and-desist, sentiment, 0–100 risk. |
| 3 | **Auto-QA** | `qa.py` | Auto-evaluates every call against a 5-item rubric → PASS/FAIL, replacing manual 2% sampling. |
| 4 | **Agent Assist** | `agent_assist.py` | Per call: auto summary, disposition, next-best-action, and a real-time compliance nudge. |

## Why this split matters (the moat point)

- **Buy:** ASR, LLMs, TTS, and the DNC/litigator/reassigned-number data (commodity
  vendors: DNC.com, PossibleNOW, Gryphon, Blacklist Alliance).
- **Build:** the eligibility engine, plain-English rule authoring, the append-only
  consent/revocation ledger, and the audit trail — that is the only defensible code.

Components 2–4 are deliberately thin: in production they are one model call each.
Component 1 is where the real engineering (and any moat) lives.

## Files

```
gen_data.py            deterministic generator (seed=42) -> data/contacts.json
data/contacts.json     100 synthetic contacts
data/transcripts.json  12 call transcripts (clean + violations)
llm.py                 Claude-or-offline abstraction
nlc.py                 Natural Language Compliance (the differentiator)
analytics.py           conversational analytics + FDCPA flagging
qa.py                  automated QA scoring
agent_assist.py        agent assist + summaries
demo.py                runs everything
```

*All data is fabricated. Regulatory rules are simplified for demonstration and are
not legal advice.*
