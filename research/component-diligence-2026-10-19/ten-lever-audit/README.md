# Ten-lever audit: gasoline/hybrid applicability

19 October 2026. No workbook edits. User-provided exhibit supplies per-lever percentages absent from the prior text extraction. This corrects the previous overly broad statement that a filtered subtotal could not be calculated. A filtered EV benchmark is calculable; an actual ICE savings rate still requires transfer assumptions.

## Decision table

Ranges below are contributions to original EV material cost, not percentage reductions in individual systems. Applicability judgments are analyst inference.

|#|Lever|Exhibit range|Gasoline/hybrid treatment|Evidence and limits|
|---|---|---|---|---|
|1|Energy demand/battery sizing|2.4–6.4%|Exclude quantified range for ICE; conditional for hybrids|Efficiency helps gasoline consumption, but does not reproduce removal of a large traction battery. Schaeffler Audi EA888 thermal module demonstrates ICE efficiency, not disclosed material savings.|
|2|Design to value|2.3–6.1%|Broadly transferable|Ford Blue material substitutions: $35m/year projected, exhaust manifolds/mounts/front rails. WorldAutoSteel front-body redesign: 10% piece-cost modeled reduction. Neither validates whole-vehicle percentage.|
|3|Technology selection|1.6–4.3%|Exclude quantified EV range for ICE; selective hybrid applicability|EV battery/motor choices dominate source. No matched gasoline technology substitution with equivalent functionality and current cost delta established.|
|4|System integration|0.7–1.9%|Conditional|EFESO integrated thermal-module project: >10% material/manufacturing savings indicated; hybrid/EV supplier, mixed technical/commercial actions, not pure integration attribution. Audi thermal module supports ICE mechanism without disclosed dollars.|
|5|Trim complexity|0.6–1.6%|Broadly transferable|Ford Explorer configurations >1,900 to 23; wiring variants 500 to 14, $7m/year estimated. Wiring example overlaps #10; count once. Some savings outside materials.|
|6|Eliminate subsystems|0.5–1.4%|Exclude from core subtotal, retain mechanism watchlist|ZF front electric parking brake removes manual rear-brake actuation components and integrates electronics into existing ESC. No dollar saving disclosed. Specific structural-battery examples do not transfer to ICE.|
|7|Flexible platforms|0.5–1.4%|Broadly transferable, redesign-dependent|Renault–Nissan CMF announced 20–30% component-purchasing reduction and 30–40% entry engineering/investment reduction in 2013. Targets, not independently verified outcomes; multi-year deployment through 2020.|
|8|Challenge specifications|0.3–0.8%|Broadly transferable|Ford planned removal of manufacturing-aid cable: $11m/year. Interpretation: delete unnecessary requirement. No affected-unit denominator disclosed. Avoid duplicate #2 allocation.|
|9|Supplier-standard modules|0.3–0.8%|Broadly transferable|Bosch ABS Gen9 modular software reduces testing/application costs; 30% reported reduction is weight/size, NOT cost. CMF supports shared-module purchasing mechanism but is same evidence as #7, not additive.|
|10|Electronics/software integration|0.2–0.6%|Broadly transferable, architecture-dependent|Aptiv satellite ADAS: 10% like-for-like system cost claim. Ford wiring is another example but already counted #5. Not a 10% whole-vehicle saving.|

## Filtered calculation

Use calculate.py and calculations.json. Core six (#2,5,7,8,9,10): 4.2–11.3%, midpoint 7.75%. With conditional #4: 4.9–13.2%, midpoint 9.05%. With #6 too: 5.4–14.6%, midpoint 10%. Do not call a midpoint an empirical average. These retain the original EV denominator; neither rebasing to non-battery EV material cost nor a Ram/Jeep BOM is justified without further cost data. Displayed low rows sum 9.4% versus printed 9.5% total; use row sums consistently and flag rounding. These are screening subsets, not confidence intervals or lower/upper estimates for STLA.

## Primary evidence and provenance

- F: [Ford CMD, 22 May 2023, PDF pp8–9](https://s201.q4cdn.com/693218008/files/doc_events/2023/May/22/capital-markets-day-transcript-5-22-23.pdf). Forward-looking identified annual savings, not proof of realized net margin. Three cited projects total $53m/year; includes wiring counted only once. Do not divide by all Ford units because affected populations differ.
- N: [Nissan CMF release, 19 June 2013](https://usa.nissannews.com/en-US/releases/common-module-family-cmf-a-new-approach-to-engineering-for-the-renault-nissan-alliance). Covers Rogue/Qashqai/X-Trail and Renault models; useful non-BEV engineering analogue. Purchasing and investment percentages have different denominators.
- Z: [ZF front EPB, 2020](https://press.zf.com/press/en/releases/release_15683.html). Search extract accessible; full-page retrieval failed. Mechanism evidence only, no quantitative cost credit.
- B: [Bosch ABS generation9](https://www.bosch-mobility.com/en/solutions/braking-systems/abs-module/). Production component architecture; no savings dollars or cost percentage.
- S: [Schaeffler 2014 symposium](https://www.schaeffler.com/remotemedien/media/_shared_media/08_media_library/01_publications/schaeffler_2/symposia_1/downloads_11/Schaeffler_Kolloquium_2014_21_en.pdf). Audi gasoline thermal module already in volume production. CO2 benefits do not establish manufacturing cost savings.
- E: [EFESO thermal case](https://www.efeso.com/client-results/product-cost-optimization-for-automotive-thermal-management-system/). Indicated savings; not externally audited.
- A: [Aptiv sustainability report p22](https://downloads.aptiv.com/libraries/docs/default-source/aptiv-storage/2020_aptiv_sustainability_report_f.pdf?sfvrsn=f2ae913e_2). Supplier claim for like-for-like ADAS features, not OEM fleet outcome.
- W: [WorldAutoSteel/Ricardo study](https://www.worldautosteel.org/wp-content/uploads/2026/05/WorldAutoSteel-A4-PC-Study_512.pdf). Virtual engineering study, not production outcome.

## McKinsey citation audit

[2026 article](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/building-profitable-evs-ten-structural-design-moves-to-cut-material-costs) attributes methodology to Caresoft teardowns and 20 McKinsey experts. Public pages do not provide ten independent, reproducible before/after cost datasets. Footnotes 1–4 point to internal forecast/cost-model analysis. Footnote5 links the [2021 EV-profitability report](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/electrifying-the-bottom-line-how-oems-can-boost-ev-profitability); outside-in model, not independent realization evidence. Footnote6 links [2026 battery research](https://www.mckinsey.com/features/mckinsey-center-for-future-mobility/our-insights/the-future-of-affordable-evs-breakthroughs-in-battery-pack-costs), less useful for ICE scope. Footnote7 names Auto Research Center's aerodynamic/fuel-economy work; not followed because it establishes energy rather than component-cost savings. Footnote8 links the [2018 teardown study](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/what-a-teardown-of-the-latest-electric-vehicles-reveals-about-the-future-of-mass-market-evs), reviewed: it explicitly notes traditional OEMs' prior design-to-cost maturity. Footnote9 is an accounting clarification excluding battery downsizing from thermal savings, not another source. The chart's footnote1 is cropped from the supplied screenshot and was not independently recovered; do not invent its conditions.

## Decision

9% has an illustrative benchmark rationale under broader transfer assumptions; it is not proven by adding unrelated subsystem cases. The next test is incremental headroom in STLA's existing architectures and project rollout by 2028. Carryover designs may already embody these optimizations. Track revenue sacrificed through content deletion and retain cost-category boundaries to avoid counting material, manufacturing and warranty benefits twice. Existing forecast left unchanged.
