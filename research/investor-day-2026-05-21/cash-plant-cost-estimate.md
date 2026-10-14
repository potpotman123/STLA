# NA maintenance, energy and other cash plant costs: annual working estimate

14 October 2026. User requests one rounded annual driver base, with detailed support outside workbook. Recommendation: **EUR1.5bn annual 2025-reference operating cost base**, low-confidence analyst estimate; sensitivity EUR1.0bn / EUR2.0bn, not a statistical interval. No actual expense disclosure found. No forecast workbook changed and no savings rate chosen.

## Perimeter

Include purchased plant repair services, maintenance consumables/spares expensed in-year, energy/water, factory cleaning/security/waste services, site insurance/taxes and eligible production-support services. Exclude employee and agency labor already captured in labor, depreciation and IFRS16 charges captured elsewhere, capital purchases, vehicle components/raw materials, R&D, HQ/SG&A, freight/distribution, warranty and any separately modeled quality expense. Treat in-plant logistics consistently with the logistics pool, not both. External technicians embedded in repair-service invoices stay here; do not also add their FTEs to labor. Consumables must be carved out of a broad materials denominator if that denominator includes them. This is an expense pool underlying AOI, not a new incremental expense to subtract from reported revenue.

## Research executed

Checked prior source ledger, direct company transformation definition, national Census manufacturing expense detail/definitions, and government automotive cost studies. Direct disclosed current NA total not located. Avoided bulk plant collection and unsupported generic business-plan websites. No paid data or agents. The European JRC PDF surfaced in discovery but could not be retrieved and was not used. Company SVG thumbnail rendering failed; no values inferred from it.

## Route 1: observable partial pools plus explicit residual judgment

Prior company NA manufacturing energy quantities and tariff scenarios support a working EUR0.3bn utility allowance (not measured2025 spend). Historical Census purchased repairs scaled to assumed plant staffing support roughlyEUR0.25bn, rounded toEUR0.3bn for this deliberately coarse decomposition; rounding is NOT a measured inflation adjustment. Combined identifiable core roughlyEUR0.6bn. Remaining EUR0.9bn in the proposed1.5bn is an explicit allowance for consumables, facility and other factory-support costs, NOT an observed cost and NOT independently validated by the total below.

To assess whether this allowance is implausibly large, aggregate disjoint national NAICS3361,336310,336350 (vehicle assembly, engines and transmissions) in the2019/2021 Census table. Divide aggregate costs by aggregate employment, then multiply by the previous ASSUMED63k NA plant staff and divide by2025USD/EUR1.130:

| Expense | 2019-based EURbn | 2021-based EURbn |
|---|---:|---:|
| Purchased repair services | .254 | .242 |
| Refuse removal | .034 | .031 |
| Taxes/license fees | .078 | .075 |
| Professional/technical services | .233 | .226 |
| All other operating expenses | 2.024 | 1.849 |

These are scope/scale comparisons, not Stellantis expense estimates. Historical prices, US-only costs, outsourcing differences and uncertain staffing prevent direct application. Census residual includes R&D, freight, SG&A, insurance and plant overhead. Thus only a fraction belongs here. For transparency, one way to calibrate the0.9bn allowance is approximately0.1bn refuse/site taxes +0.05bn selected technical support +0.6bn eligible residual services (~one-third of the historical broad1.85–2.02bn proxy) +0.15bn expensed maintenance/operating consumables not already elsewhere. Those allocations are analyst judgments, not evidence that precisely one-third is eligible. Do not create forecast rows for them.

Lower case1.0bn effectively allows0.4bn beyond the rounded0.6bn core; upper2.0bn allows1.4bn. These choices expose uncertainty in the missing spend rather than disguise it. Employee-based scaling is vulnerable to automation/outsourcing; labor estimate has not been validated and cannot validate this pool.

## Route 2: broader historical MRO reference, not independent modern verification

EPA-420-R-09-003 (February2009), section3.2.2, states that a Sierra Research2007 estimate put Chrysler historic maintenance/repair/operations at approximately3% of cost of sales. Authors applied that same proxy to other OEMs when undisclosed. Do NOT treat those multiple OEM rows as independent confirmations. The underlying Sierra data and exact modern mapping were not independently verified.

The same report rejects a larger McKinsey2003 estimate because it likely includes equipment and technician costs already elsewhere. Do not cherry-pick that8.3%ofMSRP/14%ofmanufacturing figure or add MRO on top of costs already counted.

For scale only:2025NA revenue60.962bn minusAOI(-1.892bn) equals62.854bn of net adjusted operating expense. This is NOT disclosed NA cost of sales and includes SG&A/R&D and potentially other income. Applying3% mechanically gives1.886bn, which is NOT our estimate. Our1.5bn is2.39%of that broad expense denominator. This loose comparison puts the proposal in the vicinity of the historical MRO reference, but cannot validate it or justify a precise1.886bn. Present-day scope, tariffs, production mix and efficiencies differ materially.

## Decision and use

Use1.5bn as a transparent, low-confidence provisional analyst assumption for the ENTIRE defined cash-plant bucket, not a reported fact or a newly proven value. Detailed evidence supports the core; judgment supplies most of the remainder. It is reasonable enough for scenario modeling, not enough to call a solid observed cost base. Preserve1.0/2.0bn sensitivities outside the main workbook. If later evidence shows the nonlabor transformation definition contains materially more outsourced conversion, revisit scope and move matching costs out of other VCP pools.

One workbook driver row: annual base1.5bn. Separate achievable reduction assumption. Annual saving=base x reduction; quarterly=annual/4 per user preference. Illustrative10%reduction gives150m/year and37.5m/quarter; not recommended savings assumption. Across1–2bn bases that same illustrative rate gives100–200m/year. At2025NA revenue60.962bn, that is16–33bp of margin, showing model sensitivity. Some site taxes/insurance are less controllable than repairs/energy: achievable reduction must reflect that, not assume the whole pool can be cut equally. Cost base is2025-reference, not evidence annual spend remains flat as production recovers.

## Sources

- Company perimeter: https://stellantisnegotiations2023.com/transformation-costs/
- Census data: https://www2.census.gov/programs-surveys/asm/data/2021/AM1831BASIC01.zip ; saved original rows in manufacturing-census-benchmarks.json and supplementary calculations in cash-plant-cost-estimate.json.
- Census scope: https://www.census.gov/programs-surveys/economic-census/year/2022/about/faq/faq-manufacturing.html , question24 (broad residual), questions16–23(materials/repairs/energy/contract work). Definitions page is2022 survey; field taxonomy corresponds to earlier ASM but do not assume accounting alignment with IFRS.
- EPA report: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100AGJ1.TXT , section3.2.2 pp3-4/3-5 and appendixA. Historical secondary estimate within primary government research, not contemporary company disclosure.
- Company energy/financial sources and prior assumptions: na-manufacturing-cost-assumptions.md and manufacturing-input-validation.md.
