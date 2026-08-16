# Routine prompt

Paste the block below as the instruction for the daily "I-90 Corridor Land Scout"
Routine. Schedule it **daily at 6:00 AM Central**, point it at the environment that
holds this repo, and **attach the Gmail connector** so the digest can reach the
inbox (see "Enabling inbox delivery" in `README.md` for why that step is manual).

---

Run the daily I-90 corridor industrial land search for the k-slow/hello-world repo.

Steps:
1. cd into the repo, then:
   git fetch origin claude/chicago-i90-land-agents-avzx0w
   git checkout claude/chicago-i90-land-agents-avzx0w
   git pull origin claude/chicago-i90-land-agents-avzx0w
2. Invoke the `land-scout` skill (.claude/skills/land-scout/SKILL.md) and follow it exactly.

The skill orchestrates five agents defined in .claude/agents/: it probes whether deep web fetch is available, dispatches land-listings-scout, land-offmarket-scout and land-building-scout in parallel (one message, three Agent calls), passes results to land-underwriter for hard-gate filtering and scoring, then to land-digest-writer to deliver the digest to keslowinski@gmail.com and push the updated ledger.

All search criteria live in land-scout/config.json — read it, never substitute remembered criteria. The dedupe ledger is land-scout/ledger/seen.json and MUST be committed and pushed at the end of the run, or tomorrow's digest will duplicate today's.

Deliver even if there are no new sites (config.delivery.send_when_empty is true) so silence is never ambiguous between "nothing new" and "the job broke". If sources were blocked or a scout failed, disclose it in the run notes rather than presenting a degraded run as a clean one.

Two environment constraints, both expected — handle them, do not treat them as errors:
- The egress policy blocks Crexi/LoopNet/LandSearch/county GIS. Fall back to WebSearch-only, mark unverified fields as "claimed", and never retry a policy denial or route around the proxy.
- If the Gmail tool (mcp__Gmail__send_message) is not present in this session, use the file fallback: write the digest to land-scout/digests/YYYY-MM-DD.{html,md}, commit and push it, and deliver the markdown with SendUserFile.
