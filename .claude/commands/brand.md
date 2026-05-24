---
description: Build or advance the user's personal brand using the 5-stage Donley framework. Routes to the brand-orchestrator agent.
---

Launch the `brand-orchestrator` agent via the Agent tool. Pass it any text the user typed after `/brand` as additional context (e.g. `/brand let's work on the funnel today` → tell the orchestrator the user wants to focus on the funnel stage).

The orchestrator will read `brand/STATE.md`, decide the next best step, and either interview the user directly or delegate to a specialist (`story-miner`, `voice-capturer`, `pillar-strategist`, `platform-coach`, `waterfall-producer`, `outlier-analyst`, `funnel-architect`).

If `brand/STATE.md` doesn't exist yet, the orchestrator will run a brief session-zero intake.
