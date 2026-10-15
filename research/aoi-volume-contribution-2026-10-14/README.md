# North American volume-to-AOI conversion

14 October 2026. User-selected base case (originally proposed by AI): **EUR5,000 effective volume/mix AOI contribution per incremental shipment in 2027 and 2028**, sensitivity EUR3,000–8,000. The user elected to retain this shortcut after discussing a cost-based alternative; that alternative is not the selected architecture. Sensitivities remain AI proposals. No workbook changed. This is not a measured pure marginal contribution or a model-specific margin.

## Sources and extraction

Read existing handoff and VCP notes first. Reviewed official results index, original FY2025 and Q2 2026 presentation bridges, FY2024 industrial-cost commentary, 2026 restatement factsheet and July 2026 management Q&A. SEC annual-report HTML was too large for web extraction; switched to presentation bridges. Four local bridge pages were text-extracted and visually checked. Bridge sums reconcile exactly. No regression, bulk collection or competitor-margin extrapolation.

- [FY2025 results materials](https://www.stellantis.com/en/investors/reporting/quarterly-results-materials), presentation pp43,48. Local source `/Users/kwu/Downloads/Stellantis N.V._EP_2025-12-31_English.pdf`.
- [Q2 2026 presentation](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/presentations/Stellantis-Q2-2026-Financial-Results-Presentation.pdf), pp25,27. Local source `/Users/kwu/Downloads/Stellantis N.V._EP_2026-06-30_English.pdf`.
- [July 2026 call](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-Q2-2026-Financial-Results-Call-Transcript.pdf), printed pp12,15: management attributes sequential volume/mix drop-through weakening to nameplate mix, especially Mexico-produced vehicles. Analyst's 27%/8% figures are question framing, not a verified constant-definition contribution-margin series.
- [FY2024 presentation](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/presentations/Stellantis-FY2024-Results-Presentation.pdf), p12: lower fixed-cost absorption included in Industrial. No numerical FY2024 volume/mix coefficient admitted from this pass.
- [Restatement factsheet](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Financial-Fact-Sheet-Expanded-Quarterly-Reporting-for-2025-and-Segment-Reclassification-for-2025-and-2024.pdf), p2: Maserati geographically reassigned from January 2026. FY2025 shipments originally 1,472k versus restated 1,474k; do not combine original bridge amounts with restated denominators.

## Observed bridges and derived ratios

| Comparison | Shipment change | Volume/mix AOI change | Derived EUR per net added shipment |
|---|---:|---:|---:|
| H2 2025 versus H2 2024 | +231k | +991m | 4,290 |
| H1 2026 versus H1 2025 | +176k | +1,049m | 5,960 |
| Q2 2026 versus Q2 2025 (within H1, not independent) | +122k | +409m | 3,352 |
| FY2025 versus FY2024 | +40k | -1,430m | -35,750; unusable as marginal profit |

Q1 effect inferred from H1 minus Q2 is EUR640m on approximately 54k additional units, or EUR11,852. Rounded shipments can cause discrepancies with separately published quarterly data. This illustrates volatility; it is not a preferred forecast anchor.

Recovery-period pooling: (991+1,049)m / (231+176)k = EUR5,012, rounded to EUR5,000. Pool only the two half-year recovery observations; do not add Q2 again. Each observation uses internally matched scope, but the pooled series spans a small reporting-perimeter change and is approximate. Selection favors recent recovery economics; this is not an unbiased long-run estimate. FY2025's opposite-sign result is explicit disconfirming evidence against treating the ratio as structural marginal profit. Mix affects the entire book, not just the net incremental units.

## Decision and mechanism

An added vehicle earns revenue but requires components, variable manufacturing, freight and ordinary warranty accruals. The remaining contribution can support fixed expenses. Existing AOI margin is after fixed expenses and therefore is not the right rate to apply to incremental revenue. Conversely, total AOI improvement divided by units includes pricing, industrial savings and overhead movements.

The EUR5,000 working input is an effective **volume-and-mix** coefficient, excluding the separately disclosed price, industrial, SG&A, R&D and FX categories. Holding it constant is a simplifying assumption. Affordable launches may produce less profit per unit; evidence does not justify pretending all models have the same economics. Use EUR3,000 (near rounded Q2 outcome) and EUR8,000 (judgmental favorable-mix sensitivity between H1 and inferred Q1) as sensitivities, not statistical bounds. If mix changes materially with little net volume change, this one-coefficient method fails; review model-level contribution or introduce an explicit mix adjustment before relying on the result.

## Model implementation and double counting

- `Model Assumptions` row14: 5,000 in each forecast quarter, no division by four. `NA AOI Bridge` volume/mix line: (current shipments - comparable prior-year shipments) × 5,000 / 1m. Recalculate annually by summing quarters.
- Treat coefficient as frozen at the reference price/cost environment. Model subsequent price/support effects separately, not via total weighted RPU movement. With fixed-reference coefficient and price deviation p_t, incremental price effect is Q_t*p_t - Q_previous*p_previous (or the model-level sum). This also captures support paid on extra units. Alternatively use a prior-year-price coefficient plus Q_t*change_in_price; do not mix the two conventions.
- RPU already reduces revenue for incentives. In an AOI bridge starting from prior-year AOI, a separate pricing effect is necessary to translate that change into profit; this is not double counting unless profit was already calculated from current revenue less costs before adding the bridge. Do not deduct it twice within a single calculation route.
- Do not translate all RPU dilution into a euro-for-euro profit loss: cheaper vehicles also have different variable costs. The effective volume/mix coefficient already approximates that mix effect.
- VCP: add only incremental recognized YoY savings. Existing productivity embedded in the starting AOI cannot be added again. Industrial includes more than VCP (tariffs, warranty, regulatory, absorption and other items). No additional numerical factory-utilization uplift is selected here. Genuine manufacturing cost reductions can be modeled separately, but must not also include an unsupported duplicate volume benefit.

## Forecast scale check

Current shipment proposal is 1,533,851 NA units in 2027 and 1,636,700 in 2028, conditional on gross portfolio forecasts before an unselected substitution deduction. Increase 102,849 × EUR5,000 = **EUR514.245m 2028 YoY volume/mix AOI benefit**. Sensitivity EUR308.547m–822.792m. This is not total AOI growth. Some growth comes from ending destocking, not incremental customer sales. No 2027 benefit calculated until comparable full-year 2026 shipment baseline is finalized.

Historical calibration supports use as a transparent provisional input; it does not independently validate 2027–28 mix or the recovery thesis. Remaining work: finalize VCP, pricing attribution and non-VCP cost offsets, then check total implied margins. Calculations and arithmetic checks are retained in `calculations.json`.
