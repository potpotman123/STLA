# Electronics, component sharing and engineering: bounded evidence review

Reviewed 19 October 2026. Research only; no workbook or forecast changes. The project register is `records.json`. This is a selective systems review, not an independently priced bill of materials.

## Investment findings

1. **A real technical mechanism exists:** deleting duplicate controllers, housings, relays and wiring can reduce cost without deleting customer functions. Aptiv's unusually concrete demonstration reports **$40 per vehicle** from a specified electrical-center redesign. It does not establish a Stellantis production saving.
2. **The most directly relevant new Stellantis number is ~70% lower L2+ system cost.** Investor Day technology slide 23 explicitly limits this to hands-free highway driver assistance. No dollar baseline, bill-of-material scope, model eligibility or production penetration is disclosed. It is not 70% lower total electronics cost.
3. **Timing limits the big architecture thesis:** management's 2026 transcript places STLA Brain's US introduction in 2028; that does not establish a full-year, full-fleet saving by 2028. Earlier 2024 announcements envisaged 2025 vehicle integration, so old launch promises cannot be treated as accomplished deployment.
4. **Toyota's widely cited TNGA 20% is a development-resource measure**, not a verified 20% component-cost reduction. Component sharing and bulk ordering are sound mechanisms, but this evidence provides no Toyota component-cost percentage to transplant to Stellantis.
5. This work supplies no defensible positive numerical NA savings forecast on its own. Eligibility, old-design prevalence, contract savings and implementation costs remain unknown. **Unknown is not zero opportunity**, but it cannot be silently multiplied by all NA vehicles.

## How the systems work and what can change

| System | What it physically contains and does | Cost drivers and plausible improvement | Constraints / accounting |
|---|---|---|---|
| Power distribution and harnesses | Fuse/relay boxes protect circuits; wires, terminals, connectors, seals and clips carry current/data | Shorter routes, fewer connections, smaller permissible wire gauges, smart protection, fewer variants | Current, heat, voltage drop, crash damage isolation, water/vibration durability, service access and validation remain necessary. Purchased harness price is variable to OEM but recovers supplier labor, tooling and engineering. OEM installation labor is manufacturing, not component cost |
| Distributed controllers / zonal architecture | Controllers combine chips, circuit boards, power supplies, enclosures, connectors and software | Several local devices can share computing, power and housing; zone controllers connect nearby devices to a backbone | Added central computers, network bandwidth, cooling, redundancy, cybersecurity and integration offset gross deletions. Safety-critical functions require suitable separation and fault handling |
| Occupant classification | Sensors determine occupant type/position to control airbag deployment | Existing camera and software may replace seat pressure hardware and its wires | Camera field of view/occlusion, lighting, occupants/child seats, computing capacity and validated airbag decisions matter. If a suitable camera is absent, include its added cost; whole-seat savings are the wrong denominator |
| Hands-free driver assistance | Cameras/radar, compute, driver monitoring, communication and control software | Hardware/system design, shared computation and sourcing may lower the cost of a given feature set | Precisely defined operating domain and supervision requirements; software/map/licensing cost and subscription economics; package fitment and customer uptake. Not interchangeable with autonomous driving |
| Shared platforms/components | Common interfaces enable reuse of assemblies across multiple models | Fewer engineering variants, larger orders, repeated validation/production processes | A pickup's towing/payload needs are not a compact crossover's; legacy tooling and launches constrain introduction. Avoid claiming benefits already achieved through prior platform/purchasing programs |

Supplier cost reduction enters Stellantis components only to the extent the purchase price falls. Internal software development and new tooling are primarily fixed/program costs, with step increases for new architecture/platform capacity. Their amortization or supplier recovery may be embedded in per-unit prices. Cost per unit can fall with scale while total cash cost does not. No public source reviewed supplies a reliable Ram/Jeep dollar breakdown of these systems.

## Four quantified cases and their exact limits

### E01 — Aptiv smart electrical centers: $40 per vehicle

[Original case study, PDF pp1–2](https://www.aptiv.com/docs/default-source/case-studies/aptiv-case-study-smart-electrical-centers.pdf?sfvrsn=dbc9c73d_10). Three conventional centers become one smart plus one conventional. Seventeen fuses and 22 electromechanical relays change to electronic alternatives; 22 of 37 cables into the removed center disappear (6.7 meters). Reported result: $40 system cost reduction and 2 kg less weight, with improved diagnostic capability. The price year, original system cost, tooling, engineering recovery and production volume are unspecified. The PDF says smart centers have been produced since early 2019; it does **not** establish that this exact demonstration entered production. Do not add its wire/relay/controller deletions again as separate projects.

[Aptiv's dated 30 September 2021 article](https://www.aptiv.com/en/insights/article/getting-vehicle-architectures-from-ice-to-bev-and-beyond) identifies the customer only as a major North American OEM. It also describes a separate same-vehicle architecture comparison removing more than 9 kg and more than 20 connectors. This is not independent validation and provides no second dollar result. It discusses retaining functions after crash damage as an architecture evaluation criterion. Neither case names Stellantis or a Ram/Jeep model.

### E02 — Aptiv camera-only occupant classification: up to 40% of system BOM

[Aptiv release, 8 June 2026](https://ir.aptiv.com/news/news-details/2026/Aptiv-Introduces-Advanced-Occupancy-Classification-The-Industrys-First-Camera-Only-Occupant-Detection-System/default.aspx). Supplier commercial claim: camera-based classification replaces conventional in-seat detection hardware, cutting the detection-system bill of materials by up to 40%. The release reports successful federal tests and announces a live demonstration; it does not identify a contracted series-production customer, eligible model volumes or realized savings. Most existing interior cameras are described as usable, but compatibility must be verified. The percentage is neither the seat price nor the total restraint-system cost. No dollar denominator or engineering investment is disclosed. Unquantified for Stellantis through 2028.

### E03 — Stellantis L2+ assistance: ~70% system-cost target

[Product & Technology transcript, p3](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Product-and-Technology.pdf); [official presentation, technology slide 23](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/presentation/Stellantis-Investor-Day-2026-FaSTLAne2030-Product-and-Technology.pdf). Management targets ~70% lower L2+ cost, with expanded hands-free functionality from 2027. Door-to-door supervised assistance is separately scheduled for 2028. The same transcript places STLA Brain in Europe in 2027 and the US in 2028; SmartCockpit remarks name Grand Cherokee North America in 2027. These are plans, not confirmed production coverage. No measured dollar base or net rollout cost is provided. Hardware/software overlap prevents adding separate Brain, cockpit and ADAS savings mechanically.

The local deck's PDF pp39 and 49 (technology slides10 and23) were visually inspected. The L2+ denominator and launch labels are clear. SmartCockpit's spoken model/timing should still be cross-checked against a model launch before forecasting.

### E04 — Toyota TNGA: 20% development resources, not component BOM

[Toyota 27 March 2013 framework](https://global.toyota/en/detail/85129) targets 20–30% better development efficiency through grouped planning and shared parts, with savings reinvested. It describes global bulk ordering and compatibility with more standard components, but gives no purchasing-cost reduction percentage. [Toyota 6 December 2016 follow-up](https://global.toyota/en/detail/14384838) reports a 20% reduction in development resources and reinvestment into quality/product performance. This is a management-reported development outcome, not a 20% recurring component saving. [2015 progress report](https://media.toyota.ca/en/releases/2015/making-ever-better-cars-a-progress-report.html) likewise uses development resources as the denominator. No defensible total component-cost outcome from TNGA was found in this bounded pass.

## Stellantis already had this strategy; what has actually changed?

[June 2024 software release](https://www.stellantis.com/en/news/press-releases/2024/june/stellantis-unveils-multiple-world-premiere-software-driven-products-addressing-b2c-and-b2b-customers) targeted roughly halving ECUs to around60 and 2025 vehicle integration. It was a forward plan, not a realized unit-cost observation. [2026 STLA One announcement](https://www.stellantis.com/en/news/press-releases/2026/may/stellantis-unveils-stla-one-global-modular-vehicle-architecture) targets 20% cost efficiency, 2027 launch and B/C/D coverage. The corresponding slide explicitly benchmarks **current Europe against best-in-class European-built vehicles**. It is not a blanket 20% saving on NA Ram pickups. The architecture includes battery changes; adding this target on top of battery/electronics projects would double count. Up to70% component reuse is a reuse measure, not a savings rate.

Inference: the obstacle is not ignorance of consolidation. New hardware/software integration, validation and platform replacement must occur while existing vehicles remain sellable. Counterhypotheses are that existing Ram/Jeep architecture already captures much of the opportunity, that premium added functions consume the saving, or that rollout/integration cost exceeds near-term procurement savings. We have not established the old architecture of each eligible Ram/Jeep variant, so none can be ruled out.

## Case-model treatment and scale

| Case | Treatment in this sub-study |
|---|---|
| A Technical frontier | E01 offers an observed supplier-demonstration delta of $40 per compatible vehicle, in unspecified historical dollars. E02 can be expressed as ≤40% of a separately established eligible detection-system BOM; E03 as management's ~70% of a separately established L2+ system-cost baseline. No coherent whole-vehicle sum is presently possible |
| B Economically attractive | Require net replacement cost, validation/software/tooling spend and remaining program units. Break-even units = upfront project cost / net recurring saving per vehicle. If E01 really yields $40, each $1m of implementation cost needs25,000 units just to recover that spend, before time value and ongoing costs |
| C Through2028 | E01/E02 adoption and eligible volumes unknown; E03 launch plan is known but package uptake, scope and regional coverage unknown. Keep NA benefit null/unquantified, not a fabricated0 or full-fleet benefit |
| D Downside | Delayed architecture launch or pre-existing new design can mean no incremental benefit for a particular 2028 cohort; higher added compute/software cost can erase gross deletions. Quantify once project-specific data exists |

Illustrative scaling only: $40 ×100,000 eligible sold vehicles = $4m annual recurring benefit before unknown rollout costs. This is not a Stellantis forecast, not converted to euros, and not inflation-adjusted. It demonstrates why one elegant $40 change cannot independently justify a multi-billion-euro target. The 9% component assumption requires both many projects and substantial eligible production coverage; this source set proves neither.

For the L2+ claim, let **B** be the verified comparable baseline system cost and **N** the eligible sold vehicles receiving the redesign. Management's target implies **0.70 × B × N** annual recurring savings, provided the quoted reduction includes the full replacement-system cost. At 100,000 vehicles, each 100 currency units of verified B represents 7 million currency units of benefit. This is a scale ruler, not an assumed $100 baseline. If an unequipped base vehicle gains L2+, the cheaper system is still additional content cost relative to that vehicle's own baseline. `calculate.py` reproduces these examples and retains unknown actual NA benefit as null.

## What to obtain next

Prioritize (1) named L2+ baseline and replacement BOM with licensing scope, (2) program-level 2027/28 fitment and model-year timing, (3) old/new Ram and Jeep electrical schematics and contracted invoice savings, and (4) project investment and costs already credited to VCP. These would convert evidence of mechanisms into a defensible forecast. Repeating supplier weight reductions without prices will not.

## Interview explanation

“An electrical component often contains a tiny computer, its own power supply, a housing and several connections. Combining functions lets the manufacturer remove repeated support hardware while retaining the function. But the replacement computer is more capable and requires software validation. I therefore count the net system saving, apply it only to vehicles that actually adopt the design, and keep engineering expenditure and plant-labor benefits separate.”
