# Global VCP cost bases and North American allocations

14 October 2026. Bounded first pass. EUR billions. No forecast workbook assumptions changed.

> Subsequent proposal: [three-other-vcp-bases.md](three-other-vcp-bases.md) selects rounded NA components35bn, quality3bn and logistics/indirect2.5bn as provisional analyst assumptions. These do not convert the original unknowns into disclosed costs. Manufacturing cash subpool1.5bn is separate from labor/depreciation.

## Decision

We can anchor components to disclosed purchases and quality to adjusted provision additions. Manufacturing has an observable payroll anchor but no complete addressable expense denominator. Logistics/indirect remains unidentified. Regional allocations below are transparent sensitivities, not reported regional costs or statistically estimated confidence intervals. Do not present four completed bases as established facts.

## Sources and method

- [2025 annual report / Form 20-F](https://www.stellantis.com/content/dam/stellantis-corporate/investors/financial-reports/Stellantis-NV-20251231-Annual-Report-and-Form-20-F.pdf): PDF pp15 (headcount), 48–49 (charges by accounting line), 52–53 (R&D), 57–58 (AOI exclusions), 60–61 (segments), 185 (personnel costs), 284–285 (warranty), 316 (regional adjustments). PDF page numbers include the first page. Retrieved 14 October 2026.
- [2025 supplemental statements by activity](https://www.sec.gov/Archives/edgar/data/1605484/000160548426000023/stellantisnv20251231supple.htm): industrial versus financial-services income statements. Industrial figures include intersegment transactions.
- [2025 expanded sustainability statement](https://www.stellantis.com/content/dam/stellantis-corporate/sustainability/esg-disclosures/Stellantis-2025-Expanded-Sustainability-Statement.pdf): pp85–88 workforce definitions and categories; p114 direct-material purchasing. ESG headcounts include unconsolidated subsidiaries and differ from financial consolidation.
- User-supplied May 21, 2026 Investor Day transcript pp24–25 and finance slides: components represent 75% of new-vehicle cost; four VCP workstreams. Existing reading notes retain this source.

Selective extraction, accounting reconciliation and ratio sensitivities were used. Public filing, sustainability and procurement searches found no clean complete regional four-pool disclosure. Stop before expensive factory-level reconstruction. Calculations are reproduced in vcp-cost-bases.json; all regional cost multipliers are assumptions.

## 1. Accounting envelope, not the savings base

2025 industrial cost of revenues is 152.615, versus 134.924 in 2024. Use this instead of subtracting just the 2.060 financing-cost note from consolidated cost of revenues: the supplemental statement gives the broader actual industrial perimeter. Industrial SG&A is 8.638. R&D is 11.145, comprising 2.858 expensed spending, 2.094 amortization and 6.193 impairment/write-offs. The 4.952 R&D subtotal excludes impairments; it is not all cash spending or automatically addressable.

A partial cost-of-revenues adjustment is:

152.615 - 2.700 platform impairments - 7.000 program realignments/cancellations - 0.300 hydrogen costs - 4.130 warranty remeasurement excluded from AOI - 0.622 Takata - 0.269 CAFE = **137.594**.

The first three exclusions are rounded disclosures. Other smaller adjustments and scope questions remain. Therefore 137.594 is a partial reconciliation, NOT an exact normalized expense total and NOT a VCP base. Do not subtract the entire 25.412 AOI adjustment: that would also remove R&D, restructuring, investment and equity-accounted losses from the wrong line.

NA revenue 60.962 less AOI -1.892 gives 62.854 of net adjusted operating cost burden. It includes SG&A, R&D and other operating income/expense. It is only an envelope, not NA cost of goods sold. These are the original 2025 annual-report segment figures; earlier project inputs used 61.165 revenue, -1.928 AOI and 1.475m shipments. Keep both vintages distinct and reconcile the later restated perimeter before workbook linkage; do not silently overwrite the historical series.

## 2. Components / direct materials

**Observed:** >88 of 2025 worldwide purchases in the direct-material Tier-1 table; >81 in 2024. This is the strongest available component-pool anchor. Use 88 only as a rounded disclosed-floor proxy, not an exact reported expense.

Purchases need not equal expense: inventory movements, capitalization, eligibility, imported complete vehicles and parts/service scope require reconciliation. A cost reduction can reduce purchases before it flows through sold inventory into AOI. Do not compound a 75% factor onto this direct-material figure. Conversely 88 / 75% = 117.3 is only a conditional implied new-vehicle cost cross-check; it is not independently observed and does not establish the other three pools.

**NA allocation:** observed shipments are 1.472m / 5.484m = 26.84%. Equal cost per vehicle would assign 23.62 of an 88 pool to NA. For an assumed NA material cost per vehicle 1.5x or 2.0x the rest of the group, the weighted share is 35.50% or 42.32%, assigning **31.24 or 37.24** (use JSON for exact values). This acknowledges vehicle-content differences without confusing selling price with materials cost. The multipliers are sensitivity cases, not established facts or bounds; vehicle-class BOM evidence is still needed to select one. Regional sourcing location is not necessarily the region consuming the component.

Formula: share_NA = (NA_units × relative_cost) / (NA_units × relative_cost + other_units).

## 3. Manufacturing / transformation

**Observed:** global personnel costs excluding executive directors are 16.8. This covers multiple functions; it is NOT manufacturing payroll. ESG reports 179,990 blue-collar employees out of 259,206 at year-end (69.44%).

**Derived payroll sensitivity:** assume white-collar average pay equals 1.0x, 1.25x or 1.5x blue-collar pay. Applying those assumptions to the headcount mix gives global blue-collar payroll proxies of approximately **11.67, 10.84 and 10.12**. These are not the full transformation base: factory white-collar staff, energy, maintenance, external labor and other conversion expense are missing; not every blue-collar role is manufacturing. Year-end versus average headcount, differing consolidation perimeters and compensation capitalization further limit precision.

For NA, consolidated all-employee headcount share is 31.02%. A 1.0x/1.25x/1.5x NA-to-rest labor-cost assumption gives approximately 31.0%/36.0%/40.3% of payroll, assuming the same regional occupational mix. This is an allocation benchmark, not disclosed factory payroll. Combining a 1.25x white/blue ratio and 1.25x NA/rest ratio gives approximately **3.90** NA blue-collar payroll; assumptions in both steps must remain visible.

Model treatment: a restricted labor-efficiency subpool may use these sensitivities; leave nonlabor manufacturing separately unknown. Exclude depreciation from a near-term cash-efficiency haircut unless an identifiable depreciation mechanism exists. Higher output/fixed-cost absorption is separate from VCP productivity to avoid duplicate savings.

## 4. Quality / warranty

**Observed / derived:** 11.645 of 2025 warranty/recall provision additions less 4.130 AOI-excluded warranty remeasurement less 0.622 AOI-excluded Takata = **6.893 AOI-aligned additions proxy**. This assumes these disclosed charges sit in the corresponding provision additions; the filing does not provide a complete line-by-line expense bridge. It is the best starting proxy, not audited recurring warranty expense.

Do not subtract the entire approximately 5.4 remeasurement and call the result AOI normalization: roughly 1.27 remained inside 2025 AOI. Its disappearance must be separated from genuine repair-frequency/cost improvements. If the entire 5.4 remeasurement and 0.622 Takata are removed, the alternative subtotal is approximately **5.623**. That is a diagnostic excluding current-cohort re-estimation too, not a recommendation to assume those costs vanish.

2024 additions less releases were 6.199; less 0.768 excluded Takata gives 5.431 under the analogous mapping assumption. Different cohorts, powertrains, exchange rates and the changed actuarial method prevent interpreting the 2025–24 difference as pure quality deterioration. Settlement cash and the closing liability are not substitutes for annual expense.

**NA:** the regional annual warranty cost is not disclosed. The 3.252 NA share of 4.130 excluded remeasurement concerns deterioration of old cohorts, not ordinary expense; do not allocate the whole warranty pool using that 78.7% share. Current shipment weighting is also imperfect because claims cover multiple historical cohorts. Illustrative 1.5x/2.0x/2.5x NA warranty cost per current shipment yields approximately **2.45/2.92/3.30** of the 6.893 proxy. These are sensitivity cases only; they require cohort exposure and claims-cost evidence before selection.

Keep in-plant scrap/rework in manufacturing unless explicitly transferred out; do not add it again as quality savings. Claim-count improvement is not an equal percentage reduction in expense, which also depends on severity, exposure and reserve estimation.

## 5. Logistics and indirect costs

**Not established.** No clean 2025 global or NA addressable total was found. Do not assign the residual of cost of revenues to logistics. Residual includes depreciation, nonvehicle businesses, compliance, other manufacturing costs and reconciliation differences. Similarly, 8.638 industrial SG&A is not an indirect-procurement base: it includes advertising, staff and other costs, some intended to grow.

Leave base and derived savings blank / not estimated, rather than zero. Future freight/warehouse estimates should use physical flows and lane/handling costs; eligible indirect procurement needs an explicit expense perimeter, excluding costs already allocated to components, manufacturing and quality. A precise percentage of revenue would conceal these missing definitions.

## 6. What can enter the model now

| Input | Status / permitted use |
|---|---|
| >88 direct-material purchases | Disclosed annual purchase anchor; 88 is a provisional denominator proxy pending expense/eligibility reconciliation |
| 6.893 warranty additions after known AOI exclusions | Derived expense proxy; needs separate remeasurement/nonrepeat treatment |
| 16.8 all-function payroll and occupational mix | Observed anchors for explicit labor-only sensitivity, not full manufacturing cost |
| NA shipment / employee shares | Observed allocation drivers; regional cost multipliers and occupational/claim mix remain assumed |
| Complete manufacturing and logistics/indirect bases | Unknown; no invented forecast inputs |

One percentage point of savings on the illustrative NA 31.2–37.2 component pool is 0.312–0.372 annually. This is a sensitivity, not a savings forecast. On approximately 3.9 labor payroll it is only 0.039 annually. That helps size which diligence matters most. Do not pick rates to make the model sum to management's >3 NA / 6 global targets.

For each eventual approved pool: annual base × achievable reduction × applicable eligibility/recognition adjustments = modeled annual AOI benefit; divide by four for quarterly recognition as instructed. No implementation curve introduced. Define whether reduction is cumulative versus 2025, and avoid adding the prior year's cumulative saving again in an AOI change bridge. Sources do not yet support adding these differently scoped pools into one audited cost total.

## Next evidence with the highest value

Target a procurement/vehicle-cost source for NA component cost per vehicle versus Europe/rest, and a VCP disclosure separating manufacturing and logistics denominators. For warranty, seek regional ordinary accruals / cost-per-vehicle cohort data. These are specific missing facts; more broad earnings-call reading is unlikely to produce all four. No paid data, bulk scraping or expert outreach initiated.

## Manufacturing scope correction and component follow-up

See [transformation cost follow-up](transformation-cost-follow-up.md): machinery/building depreciation and energy anchors now identified; labor-only estimate must not stand in for the complete transformation cost base. The 2024 supplier map does not establish annual NA consumption.
