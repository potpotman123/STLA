# Proposed tab: AI Forecast Bridge

Purpose: show what the independent AI first pass forecast, how the analyst challenged it, what changed, and how those changes affected the investment conclusions. Do not retrospectively rewrite the AI baseline or portray AI-generated revisions as numbers independently selected by the analyst.

## Baseline controls

Freeze the original independent AI workbook/tab values, formulas, prompt, information cutoff and file/version identifier. Preserve the assignment benchmark separately. The latest jointly revised main workbook is NOT the original AI forecast.

The original AI tabs in the local workbook include `Assumptions`, `NA_Quarterly`, `NA_AOI_Bridge` and `Consolidated_IS`. During the latest read-only inspection, selected formula outputs lacked cached values. Fable should recalculate a copy using a real spreadsheet engine, verify formulas/links, then freeze the baseline. A missing cache is not zero. If original inputs have already changed, recover the original artifact and disclose the gap; do not invent a baseline from conversation recollection.

Compare at the same cutoff where possible. Separately identify later factual updates versus changed analytical judgment. Recasting the AI architecture is a methodological change and must be visible.

## Rows 1–7: scope

Title; original AI artifact/version; revised artifact/version; information cutoffs; geography/currency/units; status (proposed vs implemented); definition of baseline and attribution method.

## Rows 10–23: outcome comparison

Columns A metric; B units; C/D/E = 2026 AI/revised/delta; F/G/H = 2027 AI/revised/delta; I/J/K = 2028 AI/revised/delta; L explanation/link.

Suggested rows:
- US customer sales
- NA shipments
- NA revenue
- NA effective revenue per shipment
- Recognized annual NA VCP savings
- NA AOI
- NA AOI margin
- Consolidated revenue
- Consolidated operating income
- Consolidated net income
- EPS

Use revised minus original AI. Report margin deltas in percentage points or basis points, not percentage growth. Recompute annual margins from annual totals. Do not equate AOI with reported operating income. Consolidated outputs need completed non-NA and below-AOI assumptions, not extrapolation from this research pack.

Latest proposed NA endpoints for reconciliation (EURm unless units):

| Metric | 2026 | 2027 | 2028 |
|---|---:|---:|---:|
| NA shipments, units | 1,580,625 | 1,529,931 | 1,618,100 |
| NA revenue | 65,834.067 | 62,728.400 | 65,837.075 |
| NA AOI | 117.125 | -602.033 | 2,191.726 |

These are the latest research proposal, not confirmed outputs of Fable's current workbook. Source: `research/forecast-resolution-2026-10-14/proposal.json`.

## Rows 26–40: 2028 NA AOI variance waterfall

Opening original AI 2028 NA AOI; changes below; closing revised NA AOI; reconciliation check.

Candidate change groups:
1. Actual-data/cutoff and definition alignment, including 2026 starting anchor.
2. Existing-product volume and launch forecasts, including substitution.
3. Customer-sales-to-shipments/channel assumptions.
4. Reference RPU and mix methodology.
5. Incremental incentives/net pricing.
6. Volume contribution coefficient (original AI EUR5,500 versus user-selected EUR5,000).
7. VCP scope, cost pools, reduction rates and recognition timing.
8. Refund expiration, raw-material costs, labor inflation and reinvestment.
9. Architecture/reclassification effects that cannot be assigned to a comparable assumption.
10. Unexplained reconciliation residual, if any, visibly flagged.

**Calculation method:** run sequential scenarios in a documented fixed order. Step effect = 2028 AOI after changing that block minus 2028 AOI before changing it. The sum must reconcile exactly to the total difference. Preserve scenario outputs and changed inputs on Research Support. One-at-a-time sensitivities around the final case do not sum to an additive variance bridge; do not use them as waterfall bars. Effects depend on replacement order because price, volume and costs interact. State the order rather than claiming uniquely causal attribution.

If architectures differ, build an explicitly labeled comparable recast and show its reconciliation to the original first pass before substitutions. If a category was absent in the original AI model, label it 'not separately modeled'; that does not establish an economic assumption of zero. Never force arbitrary bars to absorb an unexplained residual.

## Rows 44 onward: assumption and evidence comparison

Columns A driver; B original AI assumption; C revised assumption; D analyst challenge; E new evidence/mechanism; F resulting model change; G 2028 impact linked to scenario; H evidence/source; I who proposed the number; J confidence/remaining test.

Include approximately 10–15 material rows, with supporting detail on Research Support:
- Model-specific recovery versus broad rebound/flat extrapolation.
- New products and internal substitution.
- Sales versus wholesale shipments and inventory replenishment.
- Manufacturer net RPU versus retail sticker prices.
- Incentive support trajectory and potential double counting.
- Incremental AOI per shipment.
- Component savings: historical purchasing outcome rather than invented addressable-share × reduction-rate precision.
- Manufacturing savings: cash plant/labor scope and evidence.
- Logistics savings: selected-route analogue versus whole-pool transfer risk.
- Warranty: early claims improvement does not justify an unsupported financial conversion.
- Savings timing: annual recognized benefit versus terminal run rate/cumulative savings.
- Cost offsets, reinvestment and the normalized 2026 anchor.

Do not claim every row is a difference until the original AI model is inspected. A blank original comparable input should be explained, not backfilled.

## Analyst contribution / AI-use record

Three or four short examples should demonstrate reasoning, not merely different numbers:

| Analyst intervention | AI response and modeling implication | Attribution caution |
|---|---|---|
| Challenged company-specific explanations and asked for industry normalization/peer comparisons | Expanded causal evidence; distinguishes temporary supply problems from persistent demand weakness | Does not independently validate recovery magnitude |
| Rejected unsupported 60% addressability ×7% cuts; requested historical outcomes | Simpler cost-pool × savings-rate framework with Nissan and logistics analogues | Transferred rates remain AI-proposed estimates, not observed STLA outcomes |
| Required model-by-model demand and dealer evidence rather than flat extrapolation | Product histories, launch scenarios and channel assumptions | User directed method; AI proposed many numerical forecasts |
| Asked to distinguish annual savings from savings reached by 2028 | Explicit recognition schedule and incremental AOI bridge | Timing remains an assumption; do not call a run rate cumulative cash savings |

Keep a dated decision log: initial AI proposition → analyst challenge → evidence obtained → revised proposition → numerical effect → unresolved limitation. Link research files rather than inventing verbatim past quotes or dates. Record conclusions, calculations and evidence, not private internal deliberations.

## Presentation and checks

Place output comparison and waterfall at the top. Group detailed assumptions below. Use consistent actual/AI/revised colors and show units. Avoid percentages of the total bridge when offsetting changes make those misleading. No negative or missing denominator growth shortcuts. Every bar must link to a reproducible scenario; original and revised endpoints must link to their actual respective models. Do not present the previous collaborative-workbook delta as the original-AI delta.
