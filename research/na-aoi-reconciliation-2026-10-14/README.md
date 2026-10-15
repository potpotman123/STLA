# North American AOI reconciliation and retained-savings test

14 October 2026. User authorized connecting existing VCP, shipment and price assumptions and testing overlaps, offsets and timing. This completes a conditional bridge and identifies what prevents a final absolute margin forecast. No workbook, independent baseline, or existing selected input was overwritten. Reproduce with `python3 research/na-aoi-reconciliation-2026-10-14/calculate.py`; results in [bridge.json](bridge.json).

## Findings and decision

- Existing proposals produce **EUR3,212.1m 2028 versus 2027 AOI improvement before other changes**, comprising EUR514.2m volume/mix, EUR306.3m lower incremental support expense, and EUR2,391.6m additional recognized VCP.
- This is not EUR3,986m of new savings every year. Annual VCP levels are EUR398.6m / EUR1,594.4m / EUR3,986m in 2026/27/28, relative to the reference. The 2026 credit is an unverified placeholder already assumed within the starting AOI, not an observed saving.
- Management's **NA 8–10% margin ambition is for 2030**, not 2028. Group 2028 margin ambition is 5%. No separate NA2028 target established. Do not compare our NA2028 forecast to group5% or NA2030 8–10% as a same-scope management variance.
- Management already includes raw-material inflation and growth-related SG&A in its group bridge. These are not overlooked risks unique to our analysis.
- No evidence justifies an automatic numerical overlap haircut or a calibrated NA cost-offset forecast. Unknown movements remain null/unestimated rather than silently zero. The current gross case is generous; it cannot establish that management's cost target is implausible.

## Inputs, population and revenue reconciliation

Use the existing D098 gross portfolio scenario, before an unselected cannibalization deduction; customer-model mix proxies US shipment mix. US wholesale/customer ratio98% in2027,100% in2028; Canada115k/Mexico91k shipments annually. Rounded model RPUs and rounded country RPUs follow the existing RPU builder (CanadaEUR38,500; MexicoEUR30,000). EUR500/250 incremental US support is already deducted from those RPUs.

| EURm unless stated | 2027 | 2028 |
|---|---:|---:|
| NA shipments, units |1,533,851|1,636,700|
| Revenue, country shipments × country RPU |62,864.130|66,518.425|
| Effective NA RPU, EUR |40,984.51|40,641.79|
| Incremental US support cost versus reference |663.926|357.675|
| Recognized annual VCP benefit |1,594.4|3,986.0|

The earlier EUR41,001 2027 RPU was weighted by customer sales. Country-specific shipment conversion slightly changes that weight: use EUR40,985 after the shipment reconciliation. This is a mechanical scope correction, not a price revision. 2028 matches the existing EUR40,642 because every country's conversion is100%.

## AOI bridge and timing

With EURm AOI, units in vehicles, and Other as signed net changes:

`AOI27 = AOI26 + (1,533,851 − NAshipments26) × 0.005 + 1,195.8 − 663.9255 + USsupportcost26_vs_reference + Other27`

`AOI28 = AOI27 + 514.245 + 306.2505 + 2,391.6 + Other28`

The 2027 formula needs a comparable full-year 2026 shipment/AOI forecast and full-year support deviation from the H1 reference. We have not established those inputs in this evidence package. Do not substitute twice H1 results and call it a forecast. Q3 shipments alone do not establish full-year AOI. A final absolute2028 margin is consequently unresolved.

Fixed-reference EUR5,000 coefficient means the price contribution is the change in aggregate price deviations: `USshipments27×500 − USshipments28×250 = EUR306.2505m`. Simply multiplying2028 shipments byEUR250 givesEUR357.675m, overstating the bridge byEUR51.4245m because support applies to added vehicles too. Canada/Mexico price changes are zero by existing assumption.

For quarterly implementation: sum quarterly shipment differences×EUR5,000; calculate support-cost differences from each quarter's shipments; VCP incremental benefits EUR298.95m/quarter2027 andEUR597.9m/quarter2028 under existing even-year phasing. Do not divide the EUR5,000 or per-vehicle support inputs by four. Carry missing other movements explicitly; annual totals must equal quarterly sums.

## Double-counting audit

| Item | Treatment |
|---|---|
| Model/geographic mix lowers weighted RPU | Revenue already captures this. Do not also call the entire RPU decline a price loss. EUR5k effective coefficient approximates volume/mix profit jointly. |
| Incentives | Embedded in RPU. Separately bridge their AOI impact only when starting from prior-year AOI; never deduct again after a complete revenue-minus-cost profit calculation. |
| Volume absorption | Earlier shorthand that the EUR5k coefficient necessarily includes all absorption was too strong. Historical Stellantis FY2024 disclosure placed lower absorption in Industrial; our coefficient comes from Volume/Mix. No separately quantified absorption uplift is selected. |
| Manufacturing VCP | Define as cash efficiency at comparable output, excluding utilization uplift. Nissan's8.3% empirical benchmark does not isolate absorption, so its transfer still carries unresolved overlap risk; wording alone cannot validate independence. Test exclusion of the entire row rather than invent a percentage haircut. |
| Component scrap / factory rework / warranty | Component material scrap in components; paid rework hours in manufacturing; post-sale repair costs in warranty. Supplier recoveries once only. |
| Freight | Supplier-embedded freight remains in components unless explicitly removed; standalone logistics excludes it. No17% freight rate applied to IT/other indirect. |
| Implementation and old charges | Include incremental AOI-recognized operating costs once. Capex, payment of prior provisions and charges excluded from AOI follow separate IS/cash-flow schedules. |
| Prior VCP | Starting AOI already contains achieved savings. Add only changes in recognized annual benefit. |

## Offsets: evidence versus assumptions

1. **Raw materials:** CFO group2025–28 bridge includes−1.4 margin points. Applying that rate to our NA2028 revenue gives a **EUR931m scale sensitivity**, not disclosed NA guidance or a2028 YoY deduction. It lacks a regional allocation and annual path. One percentage point of inflation on our post-saving reference component pool isEUR318.5m, at frozen output/content; not a commodity-exposure estimate. Do not add both sensitivities or subtract inflation already netted in a benchmark.
2. **Growth SG&A:** CFO group bridge includes−0.6 points. Same NA revenue scaling givesEUR399m as another scope-unmatched sensitivity. It is a cumulative2025–28 bridge effect, not an annual recurring new charge. No automatic linear ramp assumed.
3. **Labor:** UAW contract evidence establishes continuing wage increases andCOLA, but does not supply the wage-sensitive share of our EUR5.5bn all-in, multi-country labor pool or2028 successor-contract terms. A1% increase on post-saving reference labor isEUR50.4m as sensitivity only. Applying a US base-wage rate to all NA labor would be false precision.
4. **Tariffs/regulation:** July2026 group guidance givesEUR1.0–1.2bn net tariff costs for2026; H1EUR0.3bn includesEUR0.4bn IEEPA refund. Do not allocate all toNA or subtract the whole existing tariff bill again annually. Forecast changes from the starting-year burden, one-off refund nonrecurrence and localization separately; no unsupported refund NA allocation.
5. **Launch, execution, R&D, FX and warranty:** no calibrated incremental NA estimates found in this bounded pass. Mark unknown. Warranty improvement could be positive; new launches can raise expense. Unspecified costs are not all pessimistic offsets, nor guaranteed zero.

Management's raw-material andSG&A rates imply a combinedEUR1.330bn scale on our NA2028 revenue, but **cannot be deducted in full from the2028 YoY bridge**. Part may already be in2026/27 AOI. This is a horizon/scope check, not a selected forecast.

## What can change the conclusion?

These are one-at-a-time illustrative tests; no probabilities and no automatic additions across rows. Margin column assumes an illustrative2% NA2027 margin, not a selected2027 forecast. Other unestimated movements are held flat solely for the sensitivity.

| Case |2028 YoY AOI change EURm|Illustrative2028 margin|
|---|---:|---:|
|Existing quantified gross case|3,212.1|6.72%|
|Recognize70% of terminal VCP in2028, versus40% in2027|2,016.3|4.92%|
|Remove manufacturing VCP from both years|2,863.5|6.19%|
|Remove logistics VCP from both years|3,059.1|6.49%|
|AdditionalEUR500m net2028-vs2027 cost headwind|2,712.1|5.97%|
|AdditionalEUR1bn net2028-vs2027 cost headwind|2,212.1|5.22%|

Slower VCP recognition matters more to this bridge than eliminating the logistics assumption. At the existing gross bridge, achieving8% in2028 would require2027 AOI ofEUR2.109bn (3.36% margin), before additional other movements. This is an illustrative threshold, not management's2028 target. A EUR1bn incremental headwind raises that required2027 starting AOI byEUR1bn.

## Sources and provenance

Existing input files: [RPU](../rpu-working-assumptions-2026-10-14.json), [shipment conversion](../wholesale-sales-working-assumptions-2026-10-14.md), [volume coefficient and historical scope](../aoi-volume-contribution-2026-10-14/README.md), [VCP schedule](../vcp-schedule-2026-10-14/README.md). These are mixed user-selected and AI-proposed assumptions, not newly observed actuals.

- [Management finance transcript, pp1–2](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Financial-Overview.pdf): group raw-material andSG&A bridge, VCP, separate utilization,2028group/2030regional targets. Existing May reading notes corroborated; same source is not new independent evidence.
- [NA transcript, pp2,5](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-North-America.pdf): more thanEUR3bn2028run-rate savings;2030regional margin.
- [July30 results](https://www.stellantis.com/en/news/press-releases/2026/july/second-quarter-2026-financial-results): group tariffs, refund and prior-charge cash payments.
- [UAW Stellantis contract hub](https://uaw.org/stellantis2023/) and [hourly contract](https://uaw.org/wp-content/uploads/2023/11/Stellantis_PM___P__BOOK-Hourly_book-WEB.pdf): contractual wage mechanism; no numeric cost allocation adopted. Full contract was not bulk parsed.

Checks: VCP year-to-year telescoping; fixed-reference price interaction; country-shipment revenue reconciliation;2028RPU agreement with prior rounded case; scenario arithmetic. These validate calculation consistency, not forecasts. Bounded discovery stopped where annual regional offsets require unreported allocations. Next model dependency is a comparable2026starting forecast, then explicit signed other-industrial/SG&A/R&D/FX changes. Preserve nulls until selected rather than reporting conditional margins as completed forecasts.
