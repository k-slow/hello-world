# Lead Schema, Scoring, and Dedup

Both scouts write the same record shape so the tracker stays one table.

## Record fields

| Field | Required | Notes |
|---|---|---|
| `key` | yes | Dedup key. See below. |
| `first_seen` | yes | ISO date this lead first entered the tracker. Never changes. |
| `last_seen` | yes | ISO date of the most recent run that re-confirmed it. |
| `name` | yes | Company name, or `Confidential — <broker> #<listing id>`. |
| `city`, `state` | yes | Physical operating location. `Unknown` is allowed only with `geo_confidence: low`. |
| `county` | no | Useful for territory disputes. |
| `region` | yes | One of `IL`, `SWI`, `WWI`, `NWI`, `SWMI`, `WMI`, `NWMI`, `MSP`. |
| `geo_confidence` | yes | `high` / `medium` / `low`. |
| `category` | yes | `machine-shop` or the adjacent type: `tool-and-die`, `mold-building`, `stamping`, `fabrication`, `edm`, `grinding`, `gear`, `swiss-turning`, `waterjet-laser`, `heat-treat`, `plating-coating`, `machine-building`, `machine-repair`, `equipment-dealer`, `metrology-calibration`, `castings-foundry`, `additive`, `contract-mfg`, `other`. |
| `channel` | yes | `listed` (actively for sale), `auction`, `real-estate-signal`, `succession-signal`, `distress-signal`, `universe` (known target, no sale signal yet). |
| `status` | yes | `new`, `active`, `under-contract`, `sold`, `withdrawn`, `stale`, `dead`, `not-a-fit`. |
| `source` | yes | Site or publication name. |
| `url` | yes | Direct link. If gated, link the public teaser. |
| `access` | no | `open` or `gated`. |
| `broker` | no | Firm and named contact if public. |
| `asking_price` | no | As published. `Undisclosed` if not. |
| `revenue` | no | Annual, with year if known. |
| `cash_flow` | no | SDE or EBITDA — say which. |
| `employees` | no | Headcount. |
| `sq_ft` | no | Facility size. |
| `real_estate` | no | `included`, `available`, `leased`, `unknown`. |
| `capabilities` | no | Machine list, axis counts, materials, part sizes. |
| `certifications` | no | ISO 9001, AS9100, ISO 13485, IATF 16949, NADCAP, ITAR. |
| `end_markets` | no | Aerospace, medical, defense, ag, auto, RV/marine, energy, food equipment, etc. |
| `signal` | yes for non-`listed` | The specific evidence. "Founded 1968, sole officer since 1974, building listed on LoopNet March 2026." |
| `score` | yes | 1–5, see below. |
| `why` | yes | Two sentences max on why it scored that way. |
| `risks` | no | Customer concentration, owner-dependence, aging equipment, environmental (plating/heat treat), union, lease. |
| `sensitivity` | no | `high` when the signal involves death, illness, divorce, or bankruptcy of a named individual. |
| `next_action` | yes | One concrete step for a human. |
| `agent` | yes | `listing-scout` or `adjacent-scout`. |

## Dedup key

`key` = slugified company name + `-` + state, e.g. `acme-precision-mi`.

For confidential listings, use the broker slug plus the broker's listing ID:
`calder-capital-2291-mi`. If a confidential listing is later identified, keep
the original `key`, add the real name to `name`, and note the resolution — do
not mint a second row.

Before writing any lead, read `tracker.md` and check for the key. Also check
for near-duplicates: same city plus same phone, same street address, or a
company name differing only by `Inc`/`LLC`/`Co`/`&`/`and`/punctuation. The same
shop is routinely listed by two brokers and syndicated to four marketplaces —
one row, additional URLs appended to the existing row's source list.

## Scoring (1–5)

Start at 3 and adjust.

**Up:**
- +1 actively for sale with disclosed financials
- +1 core machining or tool & die rather than loosely adjacent
- +1 in `WMI`, Chicago metro, `MSP` core, or Rockford — depth of workforce
- +1 AS9100 / ISO 13485 / IATF 16949 certified
- +1 diversified end markets or a defensible niche
- +1 real estate included and owner willing to sell or lease it

**Down:**
- −1 no financials published anywhere
- −1 single customer over ~40% of revenue
- −1 owner is the only estimator/programmer/salesperson
- −1 equipment base is manual or pre-2000 CNC with no reinvestment
- −1 plating, anodizing, or heat treat with unaddressed environmental history
- −2 already under contract, sold, or withdrawn
- −2 `universe` channel with no sale signal at all

Clamp to 1–5. A 5 goes at the top of the daily report and gets called out in
the summary; a 1 stays in the tracker but is not repeated in the report.

## Freshness rules

- A `listed` lead not re-confirmed for 30 days moves to `stale`.
- A `stale` lead whose URL 404s or whose listing page says removed moves to
  `dead`. Keep the row — a shop that fails to sell often relists.
- `universe` rows are permanent. They are the standing watchlist, and the
  point of the adjacent scout is that this list gets more valuable over time.
- Never delete rows. Status changes only.

## Sourcing honesty

Every field either traces to a source URL or is marked `inferred`. If a number
came from a broker teaser, say so — teaser revenue is a marketing number. If a
company's location, size, or capabilities are guessed from a website with no
date, mark the record `geo_confidence` / `inferred` accordingly rather than
presenting it as verified. A short honest row beats a long speculative one.
