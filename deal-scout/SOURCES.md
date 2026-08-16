# Source Map

Where the two scouts look. `listing-scout` owns §1–§3, `adjacent-scout` owns
§4–§7. Neither agent is limited to this list — it is a floor, not a ceiling.

## Ground rules

- Public pages only. Honor `robots.txt` and site terms of service.
- Never create accounts, log in, use someone else's credentials, or work around
  a paywall or registration wall. If a listing is gated, record what the public
  teaser shows and set `access: gated` so a human can decide whether to pay.
- No contacting brokers, sellers, or owners. These agents research and report;
  a human makes every outbound approach.
- Rate-limit yourself. A handful of fetches per domain per run, never a crawl.
- If a source consistently blocks automated fetching, record it in the run's
  **Source health** section and move on. Do not retry around the block.

---

## 1. National for-sale marketplaces

| Source | Notes |
|---|---|
| BizBuySell | Deepest inventory. Search by state + "manufacturing" and by keyword (`machine shop`, `CNC`, `tool and die`, `fabrication`, `machining`). |
| BizQuest | Overlaps BizBuySell heavily; still carries exclusives. |
| BusinessesForSale.com | Better for larger/rep'd deals. |
| BusinessBroker.net | Long tail of independent brokers. |
| DealStream (formerly MergerNetwork) | Lower-quality but occasionally early. |
| Synergy Business Brokers | Runs its own listing site, strong in manufacturing. |
| Axial / Sunbelt Network listings | Public teasers only. |
| LoopNet / Crexi | Industrial real estate **with a business included** — search "business included" or "owner-user with operating business." Also the best early signal that a shop is winding down. |
| Facebook Marketplace / industry groups | Very low signal, occasionally an unbrokered owner. Time-box it. |

## 2. Regional brokers and M&A advisors

Check each firm's own listings page — many never syndicate.

- **West Michigan / Michigan:** Calder Capital (Grand Rapids; the single most
  productive source in `WMI`), Charter Capital Partners, Cascade Partners,
  Grand Rapids Business Brokers, Michigan Business Brokers, Sunbelt of
  Michigan, Transworld Michigan, Blackford Capital (PE — watch for platform
  add-ons, not listings).
- **Chicago / Illinois:** Sun Acquisitions, Sikich M&A, Prairie Capital
  Advisors, Livingstone Partners, Chicagoland Business Brokers, Certus,
  Transworld Chicago, Murphy Business Chicago, VR Business Brokers.
- **Wisconsin:** Sunbelt Business Advisors of Wisconsin, Murphy Business
  Wisconsin, Neumann & Associates, Kaufman Hall regional affiliates,
  Wisconsin Business Development brokers.
- **Minnesota:** Sunbelt Business Advisors (Minneapolis — the dominant local
  shop), Calhoun Companies, True North Mergers & Acquisitions, Chapman
  Associates MN, Transworld Minnesota, Kingsley Group.
- **Indiana:** Indiana Business Advisors, ProNova Partners, Transworld
  Indiana.
- **Networks:** IBBA member directory, M&A Source, Small Business Deal
  Alliance (SBDA) — search their member listing feeds.

## 3. Auctions, liquidations, and distress

A machine-shop auction announcement is a **going-concern opportunity that has
already failed** — but the pre-auction window is sometimes buyable, and the
equipment list tells you exactly what the shop was.

- Perfection Industrial Sales, Hilco Industrial, Heritage Global Partners,
  PPL Group, Capital Recovery Group, Machinery Values, Corporate Assets,
  Cincinnati Industrial Auctioneers, Bidspotter, Proxibid, HiBid.
- Chapter 7/11 filings naming manufacturers in-territory (PACER dockets,
  regional bankruptcy notices, business-journal coverage).
- Sheriff's sales and tax sales on industrial parcels.

## 4. Adjacent-industry target discovery

The `adjacent-scout` builds and works a **universe** of in-territory companies
in these categories, then watches them for sale signals. NAICS anchors:

| NAICS | Category |
|---|---|
| 332710 | Machine shops (the core) |
| 332721 | Precision turned products / screw machine / Swiss |
| 333514 | Special dies, tools, jigs & fixtures |
| 333515 | Cutting tools & machine tool accessories |
| 333517 | Machine tool manufacturing |
| 332111 / 332112 | Forging, impression die |
| 332119 | Metal crown, closure & stamping |
| 332312 / 332313 | Fabricated structural metal, plate work |
| 332322 / 332323 | Sheet metal work, ornamental & architectural metal |
| 332811 / 332812 / 332813 | Heat treating, coating & engraving, plating & polishing |
| 333249 / 333998 | Special-purpose & other industrial machinery |
| 326121 / 326199 | Plastics profile & other plastics products |
| 333511 / 333514 | Industrial mold manufacturing, mold building |
| 336412 / 336413 | Aircraft engine parts, other aerospace parts |
| 339112 / 339113 | Surgical & medical instruments, medical supplies |
| 335312 | Motor & generator manufacturing |
| 811310 | Industrial machinery repair & maintenance |
| 423830 | Industrial machinery & equipment distributors |
| 541330 / 541380 | Engineering services, testing & metrology labs |

Plain-language capability terms to search on, since most shops never mention a
NAICS code: CNC milling, CNC turning, Swiss screw machine, multi-spindle,
5-axis, wire EDM, sinker EDM, surface/cylindrical/centerless grinding, honing,
lapping, gear cutting, gear hobbing, broaching, waterjet, laser cutting, plasma
cutting, press brake, turret punch, weldments, tube bending, roll forming,
progressive die, deep draw stamping, tool & die, mold building, mold repair,
jig & fixture, gauge shop, prototype shop, contract manufacturing, build-to-
print, machine building, automation integration, powder coating, anodizing,
passivation, black oxide, heat treat, CMM inspection, calibration lab,
additive/metal 3D printing service bureau, pattern shop, foundry, screw
products, fastener manufacturing.

Certifications worth capturing because they materially raise value: ISO 9001,
AS9100, ISO 13485, IATF 16949, NADCAP, ITAR registration, DFARS compliance.

## 5. Company universe sources

- Manufacturers' directories: MNI / Harris Manufacturers Directories for IL,
  WI, IN, MI, MN; ThomasNet; MFG.com; Kompass.
- Association member rosters: NTMA chapters (Chicago, West Michigan,
  Wisconsin, Minnesota), PMA district chapters, PMPA, AMBA (American Mold
  Builders), TMA (Technology & Manufacturing Association, Schaumburg IL),
  Michigan Manufacturers Association, Wisconsin Manufacturers & Commerce,
  Minnesota Precision Manufacturing Association (MPMA), Indiana Manufacturers
  Association.
- MEP centers: IMEC (IL), MMTC (MI), WMEP (WI), Enterprise Minnesota, Purdue
  MEP (IN) — case studies and client lists surface small shops by name.
- State business registries for entity age and officer names: IL SOS, WI DFI,
  MI LARA, MN SOS, IN SOS.

## 6. Succession and off-market signal sources

- **Trade & regional business press:** MiBiz (West Michigan — best single
  source for `WMI`), Crain's Chicago Business, Crain's Grand Rapids Business,
  Milwaukee Business Journal, BizTimes Milwaukee, Minneapolis/St. Paul
  Business Journal, Twin Cities Business, Rockford Register Star business
  page, South Bend Tribune business page, Traverse City Record-Eagle,
  Modern Machine Shop, Production Machining, Manufacturing News, IndustryWeek.
- **Succession language** to search for by name plus territory city:
  "owner retiring," "retirement sale," "second generation," "third
  generation," "no succession plan," "family-owned since 19—," "founder is
  retiring," "seeking successor," "ESOP feasibility study," "transition of
  ownership."
- **Age and tenure proxies:** incorporation year before 1990 combined with an
  officer who has held the role 25+ years; a website copyright date that
  stopped updating; a LinkedIn company page with an owner listing 30+ years
  of tenure; "celebrating 50 years" anniversary press.
- **Stress and wind-down proxies:** WARN notices filed in IL, WI, IN, MI, MN;
  equipment listed for sale individually on MachineTools.com, eBay, or
  Facebook by the shop itself; the building listed on LoopNet while the
  company still operates; ISO certificate lapsing; job postings stopping.
- **Community signals:** chamber of commerce and EDC announcements, county
  economic development newsletters, local "business changes hands" columns.
- Obituaries of a named owner-operator are a real signal but a human matter.
  Note the fact neutrally, never draft an approach, and set
  `sensitivity: high` so a person handles the timing.

## 7. Deal-flow context (not leads, but sharpens scoring)

- Recent comparable transactions in the region — who is buying, at what
  multiple, in what niche.
- Active acquirers to be aware of as competition: regional PE platforms and
  serial acquirers in precision machining across the five states.
- Local SBA 7(a) lender activity for manufacturing acquisitions.
