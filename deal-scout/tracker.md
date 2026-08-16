# Deal Tracker

The running, deduped index of every lead either scout has found. One row per
company, forever — status changes, rows never get deleted.

This table carries the index columns only. The full field set from
`SCHEMA.md` (financials, capabilities, certifications, risks, signal evidence)
lives in the dated report where the lead first appeared, linked from the
`First report` column. When a lead materially changes, the new detail goes in
that day's report and the row here is updated to point at it.

**Before adding anything, read this whole file and check the `Key` column.**
Then check for near-duplicates — same address or phone, or a name differing
only by Inc/LLC/Co/punctuation. The same shop gets listed by two brokers and
syndicated to four marketplaces; that is still one row.

Sort order: `Score` descending, then `Last seen` descending.

| Key | Name | City, ST | Region | Category | Channel | Status | Score | First seen | Last seen | Source | First report | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _no leads yet — first run pending_ | | | | | | | | | | | | |

---

## Status legend

| Status | Meaning |
|---|---|
| `new` | Found this run, not yet reviewed by a human |
| `active` | Confirmed still on the market or still a live target |
| `under-contract` | LOI or purchase agreement reported |
| `sold` | Transaction closed |
| `withdrawn` | Pulled off the market by the seller |
| `stale` | No re-confirmation in 30+ days |
| `dead` | Listing gone or company closed. Keep the row — shops relist. |
| `not-a-fit` | Human-reviewed and declined. Keep the row so it stops resurfacing. |

## Channel legend

| Channel | Meaning |
|---|---|
| `listed` | Actively for sale through a broker or marketplace |
| `auction` | Equipment or going-concern auction scheduled |
| `real-estate-signal` | Building listed while the company still operates |
| `succession-signal` | Retirement, no successor, ownership transition evidence |
| `distress-signal` | WARN notice, bankruptcy, lapsed certs, wind-down evidence |
| `universe` | Known in-territory target, no sale signal yet — the watchlist |
