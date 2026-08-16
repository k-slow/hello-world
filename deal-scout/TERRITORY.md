# Territory Definition

The search box for all Deal Scout agents. A lead is **in territory** only if its
physical operating location falls in one of the regions below. When a listing is
blind ("confidential, Northern Illinois"), map it to the closest region and mark
`geo_confidence: low`.

Region codes are used verbatim in the `region` column of the tracker.

---

## `IL` — Illinois (entire state)

Whole-state coverage. Highest-density subzones, in rough priority order:

- **Chicago metro / collar counties** — Cook, DuPage, Lake, Will, Kane, McHenry,
  Kendall. Elk Grove Village, Addison, Wood Dale, Bensenville, Itasca, Franklin
  Park, Melrose Park, Bedford Park, Cicero, Schiller Park, Elgin, Aurora,
  Carol Stream, Wheeling, Palatine, Lake Zurich, Waukegan, Libertyville,
  Bolingbrook, Romeoville, Joliet, Crystal Lake, McHenry.
  Elk Grove Village alone is one of the densest machining corridors in the US.
- **Rockford / Winnebago–Boone** — Rockford, Loves Park, Machesney Park,
  Belvidere, Rockton, Roscoe. Aerospace-heavy.
- **Quad Cities** — Rock Island, Moline, East Moline, Silvis (ag/heavy equipment).
- **Peoria / Bloomington–Normal / Decatur / Springfield** — Caterpillar and ADM
  supply base.
- **Downstate & metro-east** — Champaign, Danville, Quincy, Galesburg,
  Belleville, Edwardsville, Granite City, Effingham, Mattoon, Marion.

## `SWI` — Southern & Eastern Wisconsin

Roughly everything south and east of a Green Bay–Wausau line.

- **Milwaukee metro** — Milwaukee, Waukesha, New Berlin, Menomonee Falls,
  Butler, Germantown, Brookfield, Franklin, Oak Creek, Cudahy, West Allis.
- **I-94 corridor** — Racine, Sturtevant, Mount Pleasant, Kenosha, Pleasant
  Prairie, Burlington.
- **Rock River / state line** — Janesville, Beloit, Delavan, Elkhorn, Whitewater,
  Lake Geneva. Tight economic ties to Rockford.
- **Madison area** — Madison, Sun Prairie, Middleton, Verona, Stoughton,
  Watertown, Fort Atkinson, Jefferson.
- **Fox Valley / lakeshore** — Fond du Lac, Sheboygan, Oshkosh, Appleton,
  Neenah, Menasha, Manitowoc, Two Rivers, West Bend, Hartford, Beaver Dam.

## `WWI` — Western Wisconsin

Twin Cities commute shed and the Mississippi corridor. Treated separately from
`SWI` because these deals compete with Minneapolis buyers, not Milwaukee ones.

- St. Croix / Pierce counties — Hudson, River Falls, New Richmond, Somerset,
  Baldwin, Prescott, Ellsworth.
- Eau Claire, Chippewa Falls, Menomonie, Altoona, Bloomer.
- La Crosse, Onalaska, Holmen, Sparta, Tomah, Black River Falls, Winona-adjacent.
- Rice Lake, Barron, Cumberland, Amery, Osceola, St. Croix Falls.

## `NWI` — Northwest Indiana & the South Bend–Elkhart corridor

- Lake, Porter, LaPorte counties — Hammond, Gary, East Chicago, Munster,
  Highland, Griffith, Merrillville, Portage, Valparaiso, Chesterton,
  Michigan City, LaPorte.
- St. Joseph, Elkhart, Kosciusko, Marshall counties — South Bend, Mishawaka,
  Elkhart, Goshen, Bristol, Nappanee, Warsaw, Plymouth, Bremen.
  Warsaw is the orthopedic-implant machining capital; Elkhart is RV/marine.
- **Edge:** Fort Wayne and Indianapolis are **out of territory** unless the
  seller is explicitly open to a buyer in-region — flag rather than drop.

## `SWMI` — Southwest Michigan

- Berrien, Cass, Van Buren counties — Niles, Buchanan, St. Joseph, Benton
  Harbor, Stevensville, Dowagiac, Cassopolis, South Haven, Paw Paw.
- Kalamazoo, Calhoun, Branch, St. Joseph counties — Kalamazoo, Portage,
  Vicksburg, Three Rivers, Sturgis, White Pigeon, Constantine, Battle Creek,
  Marshall, Albion, Coldwater.

## `WMI` — West Michigan

The single densest target region in the territory — tool & die, injection mold
building, and contract machining at unusual concentration.

- Kent / Ottawa / Allegan — Grand Rapids, Wyoming, Kentwood, Walker, Comstock
  Park, Rockford, Cedar Springs, Grandville, Jenison, Hudsonville, Zeeland,
  Holland, Coopersville, Allendale, Grand Haven, Spring Lake, Wayland,
  Plainwell, Otsego.
- Muskegon / Oceana / Newaygo — Muskegon, Norton Shores, Muskegon Heights,
  Fruitport, Whitehall, Montague, Fremont, Newaygo, Hart, Shelby.
- Ionia / Montcalm / Mecosta — Ionia, Belding, Greenville, Stanton, Big Rapids.
- Ottawa County's "mold belt" (Zeeland–Holland–Hudsonville) deserves standing
  attention even in quiet weeks.

## `NWMI` — Northern Michigan, west side only

Everything on or west of a rough US-127 line, north of Big Rapids.

- Traverse City, Kingsley, Acme, Elk Rapids, Suttons Bay.
- Cadillac, Manton, Reed City, Evart, Clare, Lake City.
- Manistee, Ludington, Scottville, Baldwin, Hart.
- Petoskey, Charlevoix, Boyne City, East Jordan, Harbor Springs, Gaylord.
- Alpena, Grayling, Rogers City and points east of US-127 are **out of
  territory** — flag only if unusually strong.

## `MSP` — Minneapolis–St. Paul and surrounds

- **Core metro** — Hennepin, Ramsey, Anoka, Dakota, Washington, Scott, Carver.
  Minneapolis, St. Paul, Plymouth, Maple Grove, Brooklyn Park, Coon Rapids,
  Blaine, Ramsey, Anoka, Eagan, Burnsville, Lakeville, Shakopee, Chaska,
  Chanhassen, Eden Prairie, Bloomington, New Brighton, Vadnais Heights,
  White Bear Lake, Oakdale, Woodbury, Cottage Grove, Hastings.
- **Outer ring** — Wright, Sherburne, Isanti, Chisago, Rice, Le Sueur counties.
  Monticello, Buffalo, Elk River, Big Lake, Becker, St. Michael, Rogers,
  Cambridge, North Branch, Northfield, Faribault, New Prague, Jordan.
- **Regional centers** — St. Cloud / Sartell / Waite Park, Rochester,
  Mankato / North Mankato, Owatonna, Albert Lea, Willmar, Alexandria,
  Hutchinson, Litchfield, Glencoe, Winona, Red Wing.
  Rochester is medical-device machining; Winona and Red Wing straddle `WWI`.

---

## Out of territory (do not report)

- Detroit metro and eastern/southeastern Michigan — Wayne, Oakland, Macomb,
  Livingston, Washtenaw, Monroe, Genesee, Saginaw, Bay, Midland, Lapeer,
  St. Clair. This is the largest machining market in the region and will
  dominate every search if allowed. Filter it out aggressively.
- Michigan's Upper Peninsula. (Western UP — Iron Mountain, Escanaba,
  Marquette — may be surfaced as a flagged edge case, never as a primary hit.)
- Ohio, Iowa, Missouri, Kentucky, the Dakotas, Nebraska.
- Central and southern Indiana, including Indianapolis and Fort Wayne.
- Northern Wisconsin above the Green Bay–Wausau line, except the `WWI`
  counties listed above.

## Edge handling

- A multi-site company qualifies if **any** production site is in territory.
- A broker headquartered out of territory listing an in-territory business
  qualifies — location of the business governs, never the broker's address.
- Confidential listings that give only a state qualify if the state is fully
  in territory (Illinois, Minnesota). For Wisconsin, Indiana, and Michigan a
  state-only listing is `geo_confidence: low` and needs a follow-up call to
  place it — report it, flag it, do not discard it.
