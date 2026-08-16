# I-90 Corridor Industrial Land Scout

A five-agent system that searches daily for vacant land suitable for a **50,000 SF
factory** along the I-90 / Jane Addams corridor in Chicago's northwest suburbs, and
emails a qualified, scored shortlist.

## Search criteria

| | |
|---|---|
| **Corridor** | I-90, west of IL-53/I-290, no further west than Huntley (IL-47). Hampshire/US-20 included but flagged *edge of range*. |
| **Band** | Within ~6 miles north or south of the I-90 mainline |
| **Counties** | Kane, McHenry, northwest Cook |
| **Size** | 3.5–15 acres. Not scored down anywhere in that range; 15–25 ac surfaces flagged "over target"; above 25 ac rejected |
| **Condition** | Vacant, unimproved, raw, farmland, cleared, or pad-ready |
| **Utilities** | Natural gas + electric + water + **sanitary sewer**, all to the site — all four are hard gates |
| **Deal types** | Land for sale, ground lease / build-to-suit pads, off-market & publicly-owned sites, plus existing ~35–75k SF buildings in a separate section |
| **Delivery** | Daily email to `keslowinski@gmail.com`, 6:00 AM Central |

### Why the floor is 3.5 acres

A 50,000 SF single-story building is about **1.15 acres of footprint**. Add truck
court, trailer and auto parking, setbacks, and stormwater detention, and suburban
Chicago industrial sites typically run 25–35% lot coverage — putting the real need
at **3.5–6 acres**. Below 3.5 ac the building plus detention does not realistically
fit, so the search simply starts there.

Within **3.5–15 acres, size is not scored at all** — a 4-acre site and a 13-acre
site get identical marks on that dimension. Two things are noted in the write-up
rather than the score: a 3.5–4.0 ac site fits the building but leaves no room to
expand, and on a 10–15 ac site the digest says whether the excess is subdividable or
resaleable, since you would be carrying land you will not immediately use.

### Why sanitary sewer matters more than you'd think

Sewer is set as a **hard requirement**. This is the gate that kills the most sites,
and the reason is structural: incorporated parcels inside Huntley, Elgin, Hoffman
Estates, Algonquin, Gilberts and the other corridor villages generally have
municipal water and sewer, but **unincorporated Kane and McHenry parcels are
typically private well and septic**.

So the underwriter treats *incorporation status* as a first-class question and does
not trust the mailing address to answer it — parcels routinely carry a village name
while sitting outside its corporate limits.

The standard is **"some kind of sewer."** Three forms clear the gate, ranked:

1. **Municipal sanitary main** at or adjacent to the property line — clean, full marks.
2. **Documented, funded extension**, usually via annexation. Passes, badged
   "extension required," with cost and timeline exposure called out. Villages here
   will often extend mains for a 50,000 SF manufacturing user, so this is checked
   before any unincorporated parcel is rejected.
3. **Permitted or clearly permittable engineered on-site treatment system** sized for
   the use. Passes, with the IEPA permitting risk flagged.

An ordinary residential septic field does not count, and neither does a listing that
just asserts "all utilities available" with nothing behind it.

## The agents

| Agent | Role |
|---|---|
| `land-listings-scout` | Sweeps Crexi, LoopNet, LandSearch, LandWatch, Catylist and brokerage inventory. Optimizes **recall**. |
| `land-offmarket-scout` | Village/county economic development, Illinois DCEO Vetted Sites & Megasites, ComEd and Nicor site databases, land banks, corporate parks. The low-competition lane. |
| `land-building-scout` | Existing vacant ~35–75k SF industrial buildings, as an alternative to building. Reported separately, never scored against land. |
| `land-underwriter` | The quality gate. Dedupes, applies the hard gates, independently verifies utilities and zoning, scores 0–100. Optimizes **precision**. |
| `land-digest-writer` | Composes and sends the Gmail-safe HTML digest, then updates and pushes the ledger. |

The three scouts run **in parallel**; the underwriter needs the full candidate set
at once to merge the same parcel appearing across three marketplaces under two
brokers with three different acreage roundings.

## Scoring

Sites clearing every hard gate are scored 0–100:

| Dimension | Weight |
|---|---|
| Site size fit (real 50k SF capacity) | 20 |
| Utilities completeness & confidence | 20 |
| Zoning readiness (by-right vs. rezoning) | 20 |
| I-90 interchange access | 15 |
| Price per acre vs. corridor comps | 15 |
| Risk flags (floodplain, wetland, contamination) | 10 |

Grades: **A** 85+, **B** 70–84, **C** 55–69. Below 55 is ledgered but not emailed,
so the digest stays signal-dense. `verified` utilities score full; `claimed`
utilities cap that dimension at 60%.

## Deduplication

`ledger/seen.json` records **every site ever evaluated, including rejections** — so
a disqualified parcel is never re-surfaced tomorrow. A known site returns to the
digest only under **Updates**, and only on a material change: a price cut of 5%+, a
corrected acreage, or a status flip.

The ledger is committed and pushed at the end of every run. Each scheduled run
starts in a fresh container, so **an unpushed ledger is a lost ledger** and the next
digest would duplicate the last one.

## Known constraint: network egress

This environment's proxy enforces an **organization egress policy that currently
blocks the commercial listing sites and county GIS domains** — Crexi, LoopNet,
LandSearch, county assessors and municipal sites all return `EGRESS_BLOCKED`.

**The system works anyway**, because `WebSearch` is served through Anthropic's own
infrastructure and is not subject to that policy. Search results carry addresses,
acreage, and pricing — verified against live results during the build.

What the block costs you, concretely:

- More fields land at `claimed` instead of `verified`, which caps the utilities
  score at 60% of its weight
- No direct reads of parcel GIS, FEMA flood layers, or wetland inventories, so
  floodplain and wetland risk is flagged from search evidence rather than confirmed
- Full listing pages (site plans, utility exhibits, broker packages) cannot be opened

The agents handle this automatically: they probe once at the start of each run, fall
back to WebSearch-only, mark the affected fields honestly, and disclose the coverage
gap in the email. They never retry a policy denial or try to route around it.

### Unblocking deep fetch

If you want full-fidelity verification, an admin can widen the environment's network
policy at **claude.ai → settings → Claude Code environments**. Worth allowlisting:

```
crexi.com            loopnet.com          landsearch.com       landwatch.com
land.com             catylist.com         totalcommercial.com  commercialsearch.com
countyofkane.org     mchenrycountyil.gov  cookcountyassessor.com
huntley.il.us        cityofelgin.org      hoffmanestates.org
dceo.illinois.gov    intersectillinois.org
msc.fema.gov         fws.gov
```

No code change is needed. The agents detect reachability at runtime and upgrade
themselves to deep-fetch verification on the next run.

## Enabling inbox delivery

There is a second platform constraint worth knowing about, separate from egress.

This organization **does not permit connectors to be attached to a scheduled
Routine** created programmatically. The Gmail tool is available in interactive
sessions but is **absent when the daily trigger fires**, so automated runs cannot
send email out of the box.

The system degrades rather than failing: when Gmail is unavailable the digest
writer saves the digest to `land-scout/digests/YYYY-MM-DD.{html,md}`, commits and
pushes it, and delivers the markdown to your Claude app. You still get the results
daily — just not in your inbox.

**To restore true inbox delivery (one time, ~2 minutes):** recreate the Routine from
the claude.ai UI, where connectors *can* be attached.

1. Go to **claude.ai → Settings → Routines** (or the Routines tab in Claude Code on
   the web) and delete the existing "I-90 Corridor Land Scout — daily".
2. Create a new Routine: schedule **daily at 6:00 AM Central**, environment set to
   the same one this repo uses, and **attach the Gmail connector**.
3. Paste the prompt stored in [`trigger-prompt.md`](./trigger-prompt.md) as the
   Routine's instruction.

Once Gmail is attached, the digest writer detects it automatically and emails
`keslowinski@gmail.com` — no code change needed. The file-based fallback simply
stops being used.

## Tuning

Everything lives in **`config.json`** — every agent reads it at the start of every
run, so a config edit takes effect on the next run with no other change.

Common adjustments:

- **Acreage floor** → `hard_criteria.min_acres`
- **Relax the sewer gate** → `hard_criteria.utilities_required_to_site.sanitary_sewer: false`
- **Widen or narrow the corridor** → `geography.west_boundary`, `geography.north_south_band_miles`, `geography.in_scope_municipalities`
- **More or fewer sites in the digest** → `scoring.report_threshold` (lower = more), `delivery.max_sites_per_email`
- **Price expectations** → `scoring.price_per_acre_benchmarks`
- **Recipients** → `delivery.to`
- **Turn off a deal type** → `deal_types.*.enabled`

## Running it

- **Scheduled:** daily at 6:00 AM Central, via a Claude Code Routine.
- **On demand:** `/land-scout` in any session on this repo.

## Caveat

Listing data is aggregated from public sources and is not independently appraised.
Acreage, zoning, utility availability, and floodplain status must be confirmed with
the municipality, the county, and a survey before committing capital. The system is
a sourcing funnel, not due diligence.
