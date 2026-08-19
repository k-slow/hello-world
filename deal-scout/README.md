# Deal Scout

Two daily agents that hunt for machine shops and adjacent precision
manufacturers to acquire across Illinois, Wisconsin, northwest Indiana,
western and northern Michigan, and the Twin Cities.

## The two agents

| Agent | Beat | Report |
|---|---|---|
| **`listing-scout`** | What is on the market today — marketplaces, regional brokers, industrial real estate sold with a business, auctions | `reports/YYYY-MM-DD-listings.md` |
| **`adjacent-scout`** | What is not on the market yet — builds a universe of adjacent manufacturers and watches it for retirement, succession, and wind-down signals | `reports/YYYY-MM-DD-adjacent.md` |

They split by **source type**, not geography, so each one covers the full
territory. The listing scout finds deals that already exist; the adjacent
scout finds deals before a broker does, which is where the price advantage is.

## Files

| File | What it is |
|---|---|
| `TERRITORY.md` | The search box. Region codes, city lists, and an explicit out-of-territory list (Detroit metro is excluded and will otherwise swamp every search). |
| `SOURCES.md` | Where to look. §1–§3 belong to `listing-scout`, §4–§7 to `adjacent-scout`. Includes NAICS anchors and plain-language capability terms. |
| `SCHEMA.md` | Record fields, the dedup key, the 1–5 scoring rubric, and freshness rules. |
| `tracker.md` | The running deduped index. One row per company, forever. |
| `reports/` | Dated daily reports with the full detail behind each row. |
| `../.claude/agents/` | The agent definitions themselves. |

## Running them

Both are Claude Code subagents. From a session in this repo:

```
> Run the listing-scout for today
> Run the adjacent-scout for today
```

Or ask for both and they will run concurrently. On a fresh session, check out
the working branch first:

```bash
git fetch origin claude/midwest-machine-shop-agents-55r814
git checkout claude/midwest-machine-shop-agents-55r814
```

## The daily schedule

Two Routines fire a fresh session each weekday morning (US Central):

| Routine | Time | Agent | Trigger ID |
|---|---|---|---|
| Deal Scout — Listings | 6:30am CT, Mon–Fri | `listing-scout` | `trig_01FceeXGgRErhUrfQjD5jzFF` |
| Deal Scout — Adjacent | 7:15am CT, Mon–Fri | `adjacent-scout` | `trig_015vWxKe2GgikSz8btYqVbgM` |

Cron is stored in UTC (`30 11 * * 1-5` and `15 12 * * 1-5`), which is CDT.
**When daylight saving ends in November these shift an hour later in local
time** — retime them to `30 12` and `15 13` to hold 6:30/7:15am CST.

They are staggered so the two runs do not commit to the same files at the same
time. Each run reads the tracker, does its sweep, appends and updates rows,
writes its dated report, and commits and pushes to
`claude/midwest-machine-shop-agents-55r814`.

Manage them with the Routines tools — list, pause, retime, or fire one
manually outside its schedule. Ask in any session in this repo, e.g. "pause the
adjacent scout routine" or "run the listings routine now."

## What these agents will not do

Worth being explicit, because the boundary is the point:

- **No outbound contact.** Ever. No emails, calls, LinkedIn messages, or
  contact forms to brokers, sellers, or owners. The agents research and
  report; a human makes every approach.
- **Public sources only.** No accounts, no logins, no paywall or
  registration-wall workarounds. A gated listing is recorded as gated with
  whatever the public teaser shows, and you decide whether it is worth paying.
- **No crawling.** A handful of fetches per domain per run. A site that blocks
  automated access gets noted under Source health, not worked around.
- **Evidence over inference.** Every field either traces to a URL or is marked
  `inferred`. Teaser financials are labeled as the marketing numbers they are.
- **Care with personal signals.** Illness, death, and bankruptcy of a named
  owner are recorded factually with `sensitivity: high` and nothing more —
  no suggested timing, no drafted approach.

## Reading the output

Start with the tracker sorted by score. Scores of 4–5 are the day's real
output and lead every report; the rest is inventory. A short report is a
correct report — the agents are told not to pad, so an empty day says so in
one line.

The adjacent scout's `universe` rows are the part that compounds. They are a
standing watchlist of in-territory shops, and their value is that six months
of accumulated rows means a succession signal lands against a company you
already know the size, capabilities, and certifications of.
