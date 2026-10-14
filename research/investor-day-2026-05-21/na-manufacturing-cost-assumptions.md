# NA manufacturing: numerical cost-base proposal

14 October 2026. North America only. 2025-reference annual EUR costs; NOT a verified actual, 2026 run rate or forecast savings. The country breakdown below is supporting research, not new Canada/Mexico revenue tabs. No workbook changed.

> Validation update: see [manufacturing-input-validation.md](manufacturing-input-validation.md). The EUR5.5bn labor proposal is an unvalidated scenario; current evidence does not justify it as a central estimate.

## Proposed working inputs

- Plant labor: 5.5bn rounded central case; explicit joint low/high assumptions produce 4.195–6.825bn. This supersedes using the old 3.9bn blue-collar-only allocation as a complete labor denominator. Neither estimate is reported expense.
- Maintenance/energy/other cash plant costs: full total remains unknown. Energy-only working estimate approximately 0.3bn; cannot pretend this is the whole subgroup.
- Depreciation: 1.8bn rounded central allocation case, with 1.38–2.18bn sensitivity. Weakest element is regional allocation; no regional manufacturing D&A disclosure established.

These are transparent provisional model assumptions, not empirically estimated ranges. Labor is retained for sensitivity only, pending input validation; D&A is a placeholder allocation only. Do not sum to a complete transformation base or choose a savings rate yet.

## Labor reconstruction

| Assumed average equivalent plant staffing | Central headcount | Assumed fully loaded annual EUR cost | Annual EURbn |
|---|---:|---:|---:|
| U.S. hourly | 36,000 | 115,000 | 4.14 |
| Canada hourly | 8,000 | 80,000 | 0.64 |
| Mexico hourly | 16,000 | 20,000 | 0.32 |
| NA salaried plant staff | 3,000 | 110,000 | 0.33 |
| Total | 63,000 | — | 5.43 |

Every entry above is ASSUMED, not a newly discovered 2025 headcount or compensation statistic. They include maintenance employees once; exclude headquarters, product R&D, finance and distribution employees. External agency labor is included only insofar as represented by equivalent staffing; no separate duplicated contractor bill. Paid shutdown time, benefit expense, layoffs and overtime make raw headcount times wages inadequate.

Observed anchors:
1. Company 2023 negotiations factsheet: approximately 43,000 active represented employees including supplementals at end-2022; approximately USD63/hour all-in compensation, over USD126,000 annually. This historical rate includes earnings/benefits/other payments, not just base wages. Applying the full contractual wage percentage to all of it would be wrong, particularly given changing profit sharing.
2. 2023 CSR p126: NA 60,053 blue-collar employees, 79,211 total in that table (75.8%). This CSR table differs in scope from consolidated employee disclosures; not a directly comparable 2025 annual average. Supports roughly 60k blue-collar scale, not each country assumption.
3. 2025 annual report: NA year-end employees 80,247; average 2025 USD/EUR1.130, CAD/EUR1.578, MXN/EUR21.675 (PDF p212). The proposed US 115k euro equals USD130k annually, close to the historical all-in annual benchmark; this is an assumption allowing offsetting wage/profit-sharing changes, not an exact contract roll-forward.
4. Unifor September2026 release covers >9,000 Canadian workers. This is a later contract population (including idle/nonfactory roles), not 8,000 observed 2025 active plant FTEs. Company December2025 release says idle Brampton hourly workers continue receiving 70% salary and health benefits, illustrating why active-production headcount alone misses cost.

The 63k central plant staffing is about 78.5% of reported 2025 NA year-end employees. That is a scale check, not independent validation. No exact current regional staff-cost disclosure was found. Country pay/headcount sensitivities are in the JSON; do not conceal them behind a single 5.5 figure.

## Cash costs: a real energy anchor, but an unresolved services bill

2023 CSR p72 explicitly gives NA manufacturing energy: 2,379,534 MWh electricity and 3,404,870 MWh gas/LPG/propane, plus small other fuels. These are historical quantities, not 2025 quantities. EIA reports 2025 U.S. industrial average electricity price USD86.2/MWh. Applying that to all NA is only a benchmark; actual regional contracts differ.

Central scenario retains 85% of 2023 physical volumes and uses USD86.2/MWh electricity plus ASSUMED USD22/MWh gas-equivalent, translated at 1.130. Result about 0.211bn, before other fuels, water, demand charges not represented by the proxy and scope gaps. Rounded 0.3bn is a judgmental utility allowance, not an observed bill. Alternative volume/price cases produce approximately 0.135–0.358bn before those additions. Avoid duplicate demand charges if already captured in the actual tariff.

Crucially, Stellantis's own transformation-cost explanation includes purchased services and describes labor as one of the largest components behind purchased services. No amount, period or exact geography for that ranking is supplied. It disconfirms treating nonlabor costs as merely a small energy/maintenance allowance, but does NOT let us assert current NA services exceed labor by a specific amount. The SVG linked from that page could not be read as numeric text; no graphic values inferred.

External repairs, facility services, consumables and other eligible overhead remain unknown. No arbitrary maintenance percentage of net assets used: book assets are affected by depreciation/impairments and differ from replacement cost. Leave the full subgroup blank rather than a false 0.3bn. Do not label raw-material/component purchases as plant purchased services.

## Depreciation

Global 2025 machinery/equipment depreciation 3.361bn plus buildings0.594bn =3.955bn. Applying assumed NA shares35%/45%/55% gives1.384/1.780/2.175bn. These are judgmental sensitivity cases, NOT measured allocation boundaries. Shipment share26.8%, employee share31.0%, and broad geographic noncurrent-asset share54.0% measure different things and are not interchangeable. The latter includes intangibles and leasing assets and is NOT the asset allocation used to calculate a factual D&A number.

Exclude finance-fleet depreciation and R&D amortization; do not add separately disclosed right-of-use depreciation again. Plant-specific leases may already be in D&A. The global machinery/buildings categories still contain some nonfactory assets. 2025 impairment, new investment and asset retirement will change 2026–28 depreciation; annual base cannot be carried flat and called management guidance. Assume no VCP D&A saving until an actual expense-reduction mechanism is supported.

## Sources / stopping rule

- https://stellantisnegotiations2023.com/2023-uaw-negotiations-facts-figures/
- https://stellantisnegotiations2023.com/transformation-costs/
- https://www.stellantis.com/content/dam/stellantis-corporate/sustainability/csr-disclosure/stellantis/2023/Stellantis-2023-CSR-Report.pdf (pp72,126)
- https://www.stellantis.com/content/dam/stellantis-corporate/investors/financial-reports/Stellantis-NV-20251231-Annual-Report-and-Form-20-F.pdf (pp15,212,258,319)
- https://www.unifor.org/news/all-news/unifor-begins-stellantis-contract-negotiations
- https://www.newswire.ca/news-releases/stellantis-expands-canadian-workforce-as-windsor-assembly-plant-surpasses-1-000-new-hires-for-third-shift-853929721.html (company-issued release)
- https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php

Discovery covered filings, historical regional sustainability records, company bargaining materials, union coverage and energy statistics; followed the concrete energy/workforce leads. Stop before expensive plant-by-plant collection or weak proxy multiplication. Highest-value missing evidence: NA transformation cost breakdown or plant purchased-services spend; NA manufacturing D&A; actual average plant FTE and loaded payroll. Target those facts in existing expert-call materials rather than broad sentiment research. No outreach or paid collection initiated.
