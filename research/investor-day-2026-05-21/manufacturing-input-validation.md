# Manufacturing inputs: evidence validation after user challenge

14 October 2026. NA-only target; research, no workbook change. Supersedes the earlier implication that EUR5.5bn labor was adequately substantiated for model use. It remains an archived scenario, not an evidence-backed central estimate.

## New numerical evidence

US Census Annual Survey of Manufactures, national industry data (monetary source fields USD thousands):

| Industry | Year | Payroll + benefits / employee, USD | Purchased repairs / employee, USD |
|---|---:|---:|---:|
| Vehicle manufacturing, 3361 | 2019 | 108,726 | 4,620 |
| Vehicle manufacturing, 3361 | 2021 | 112,236 | 4,453 |
| Engines and engine parts, 336310 | 2019 | 87,242 | 3,920 |
| Engines and engine parts, 336310 | 2021 | 88,777 | 3,994 |
| Transmission/powertrain parts, 336350 | 2019 | 94,966 | 4,937 |
| Transmission/powertrain parts, 336350 | 2021 | 88,791 | 4,254 |

Calculations: (PAYANN + BENEFIT)*1000/EMP and PCHRPR*1000/EMP. This is annual expense divided by the survey employee count, NOT an observed individual compensation rate or annual average FTE measure. Repairs specifically mean purchased repair/maintenance services for buildings/machinery; in-house repair wages remain in payroll. Parts-only purchases may sit in materials rather than purchased repair services. The industries include other OEMs and suppliers; cannot assume identical Stellantis outsourcing, asset age or country costs.

At the old ASSUMED 63,000 plant staff and 2025 USD/EUR1.130, applying the historical repair intensities gives EUR0.219–0.275bn. This is a conditional scale illustration, not a 2025 estimate or statistical confidence interval: no inflation adjustment, no Canada/Mexico adjustment, no verified factory staff denominator. A round EUR0.25bn can be retained only as an explicitly weak purchased-repairs sensitivity. It does NOT estimate all maintenance, consumables, facility services or the full cash-cost subgroup.

The original EUR0.3bn energy allowance plus this repairs illustration is still only a partial subtotal, not a complete cost base. Do not count owned maintenance workers twice. Census total other operating expenses also contains temporary staffing, advertising, professional services and other items. Its size is not a license to assign it all to transformation costs; logistics, indirect costs and R&D may overlap our other pools. Rentals can also overlap IFRS16 depreciation/interest rather than cash AOI expense.

## Labor: what is supportable

1. US company bargaining factsheet (August2023): approximately43,000 active UAW employees incl supplementals at Dec2022; USD63 hourly all-in average, annual compensation aboveUSD126,000. Historical annual benchmark translated at2025FX is aboveEUR111,500 per worker. Holding that historical cost constant and using the prior ASSUMED36k people gives roughlyEUR4.01bn; neither factor proves2025 expense. The benchmark includes variable payments; applying negotiated base-wage increases to its entire value would overstate the roll-forward. Company also forecastUSD900m active-hourly health expense for2023. This is included in all-in compensation, not additive.
2. Canada union contract pp11,27: illustrative full-rate assembler base CAD43.23/hour until September22,2025 and44.52 thereafter, before incremental COLA. Day-weighted base for2025 (264/365 and101/365) isCAD43.587/hour. At ASSUMED2080 paid hours and observed2025FX1.578 CAD/EUR, annual base pay isEUR57,453. The earlier EUR80k loaded assumption therefore requires another roughlyEUR22,547/head, or39.2% above this base, for the combined effects of benefits, employer taxes, premiums and worker mix. That loading has NOT been established. Skilled trades have different rates; newer workers lower progression rates. The contract's8,200-member2023 population also includes parts distribution; cannot use it as2025 plant FTE. Paid shutdown support must not be omitted.
3. Mexico: found a2025 Stellantis wage revision in the federal labor registry (Coahuila, contract CFCRL-CONTRATO-XII-2024-11413). Linked salary workbook and agreement redirect to the portal; no wage numbers extracted. Earlier16k plant workers andEUR20k loaded pay remain unsupported assumptions, not registry-derived facts.
4. Salaried plant staff: earlier3k xEUR110k not established; exclude HQ, R&D, finance and distribution before using any NA white-collar count.

The Census payroll/benefit benchmarks independently support the broad scale of US manufacturing compensation, but historical cross-company figures cannot validate Stellantis2025 labor. The old5.5bn is plausible in scale, not defensible as a precise central estimate. Confidence is low until country average paid staffing and benefit/loading are established. No new supposedly precise total replaces it.

## Model-ready distinction and next evidence

- Observed inputs ready for an evidence ledger: historical industry repair intensity; US historical all-in compensation and health expense; Canadian contractual wage schedule; 2023 NA manufacturing energy quantities (previous note).
- Conditional sensitivities only: EUR0.25bn purchased repairs; prior energy, staffing and loaded-pay scenarios.
- Not established: full NA cash plant costs, 2025 NA labor total, salaried plant population and country loaded-cost reconciliation.
- For estimation, use average paid plant workers by country/worker category × contractual pay and paid hours + employer benefits/taxes + premiums/variable pay, separating idle-pay and agency cost. Do not mix cash bonus payment year with expense accrual year. For forecasts separate discretionary efficiency from contractual wage inflation, volume-driven shifts and profit-sharing recovery.
- Best missing evidence is actual NA manufacturing payroll or plant-average staffing/benefits, and purchased-services spend split by function. A labor headcount-by-plant compilation could improve the denominator, but snapshots will still require shutdown/layoff reconciliation; not undertaken as a bulk job here.

## Provenance and access

- Census bulk source: https://www2.census.gov/programs-surveys/asm/data/2021/AM1831BASIC01.zip ; metadata https://api.census.gov/data/timeseries/asm/area2017/variables.html . Small public bulk file used because API data request required a key. Source rows and arithmetic saved in manufacturing-census-benchmarks.json. Original published table, not later benchmark revisions.
- https://stellantisnegotiations2023.com/2023-uaw-negotiations-facts-figures/
- https://assets.nationbuilder.com/unifortheunion/pages/4020/attachments/original/1699044683/Unifor-Stellantis-Master_Report-final-web.pdf
- https://www.unifor.org/news/all-news/unifor-and-stellantis-reach-tentative-agreement
- https://repositorio.centrolaboral.gob.mx/contrato/660298
- FX and previous energy/headcount provenance: na-manufacturing-cost-assumptions.md. CSR2023 p125 confirms regional workforce includes fixed-term and permanent contracts; p12660,053 blue collars still not an annual plant-FTE measure.

Bounded discovery covered government manufacturing expense tables, company compensation disclosures, union contracts and Mexican labor records. Stop before bulk plant collection or further weak proxy multiplication. User's challenge is recorded as a correction to confidence, not confirmation of earlier figures.
