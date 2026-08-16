---
name: land-scout
description: Runs the daily I-90 corridor industrial land search - dispatches the listing, off-market, and building scouts, underwrites the results against the hard criteria, emails the digest, and updates the dedupe ledger. Use when the user asks to run the land search, check for new sites, or when the daily scheduled trigger fires.
---

# I-90 Corridor Land Scout — daily run

Finds vacant land for a 50,000 SF factory along I-90 between IL-53 and Huntley,
and emails a qualified shortlist. One full pass takes roughly 5–12 minutes.

## 0. Set up

```bash
cd /home/user/hello-world 2>/dev/null || cd "$(git rev-parse --show-toplevel)"
git fetch origin claude/chicago-i90-land-agents-avzx0w
git checkout claude/chicago-i90-land-agents-avzx0w
git pull origin claude/chicago-i90-land-agents-avzx0w
```

Each scheduled run starts in a **fresh container**. The ledger only exists because
it was pushed to this branch last time — so pull before you start and push when you
finish. Skipping either end means duplicate emails tomorrow.

Read `land-scout/config.json` (all criteria) and `land-scout/ledger/seen.json`
(everything already evaluated). The config is authoritative — never substitute
criteria you remember from a previous run.

## 1. Probe egress, once

Direct page fetching may be blocked by the environment's network policy. Find out
before the scouts waste turns on it:

```bash
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 10 https://www.crexi.com
```

`000`/`ERR`/`403`/`407` means deep fetch is unavailable → the run is **WebSearch-only**.
That is a supported, fully functional mode: WebSearch returns addresses, acreage,
and pricing. It just cannot open parcel GIS, flood maps, or full listing pages, so
more fields land at `claimed` rather than `verified` and scores are correspondingly
capped. Note the degradation and carry on. Do **not** attempt to route around the
proxy or disable TLS verification.

If it returns `200`, deep fetch is live — tell the scouts to use WebFetch
aggressively, especially for utility, zoning, floodplain, and wetland verification.

## 2. Dispatch the three scouts — in parallel

Launch all three in a **single message with three Agent tool calls** so they run
concurrently. They are fully independent; running them serially triples the wall
clock for no benefit.

- `land-listings-scout` — marketplaces and brokerage inventory
- `land-offmarket-scout` — municipal, county, state, utility and land-bank sources
- `land-building-scout` — existing ~35–75k SF vacant industrial buildings

Tell each one: the repo path, today's date, whether deep fetch is available, and
the count of sites already in the ledger. Each returns JSON.

If a scout fails or returns nothing, continue with the others and record it for the
run notes — a partial run that is honestly labeled beats a failed one.

## 3. Underwrite

Pass the listing and off-market candidates to `land-underwriter` (single agent, it
needs the whole set at once to dedupe across scouts). It applies the hard gates —
geography, 2-acre floor, vacancy, and **all four utilities including sanitary sewer
as a hard requirement** — then scores survivors 0–100 and returns a shortlist plus
an audited rejection list.

The building scout's output **bypasses the underwriter** — buildings are not scored
on the land rubric and go straight to the digest as a separate section.

## 4. Send and persist

Pass the underwriter's output plus the building scout's output to
`land-digest-writer`. It composes the Gmail-safe HTML digest from
`land-scout/templates/email.html`, sends to the address in `config.delivery.to`,
then updates and **pushes** the ledger.

Send even on an empty day — `config.delivery.send_when_empty` is `true`. Silence is
ambiguous between "nothing new" and "the job broke."

## Run notes to surface in the email

Be straight with the buyer about coverage. Include, when they apply:
- sources blocked this run and what that means for confidence
- any scout that failed
- whether the run was WebSearch-only
- sites truncated by `config.delivery.max_sites_per_email`

## Ground rules

- **Never fabricate** an acreage, price, PIN, zoning code, or utility fact. `unknown`
  is a correct answer; an invented one can send the buyer into five-figure due
  diligence on a site that does not exist as described.
- **Reject on uncertainty at the hard gates**, but only after actually trying to
  verify. The scouts optimize recall; the underwriter optimizes precision.
- **Flag, don't bury, the exceptions** — tight sites under 3.5 ac, Hampshire's
  edge-of-range location, and utility extensions all get visible badges.
- **Push the ledger.** An unpushed ledger is a lost ledger.

## Manual invocation

`/land-scout` runs the same pass on demand. To retune the search — acreage floor,
geography, scoring weights, sources, recipient — edit `land-scout/config.json`; every
agent reads it at the start of each run and needs no other change.
