"""Reproduce D098. No workbook or pre-audit forecast is overwritten."""
import json
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent
OLD = RESEARCH / 'model-diligence-2026-10-14'
BASE = json.loads((HERE/'baseline/proposed-forecast-inputs.json').read_text())
BY_ID = {r['id']: r for r in BASE['rows']}
RAW = json.loads((RESEARCH/'volume-recovery-2026-10-14/normalized-source-observations.json').read_text())['tables']['q3_2026']
FY25 = json.loads((RESEARCH/'volume-recovery-2026-10-14/normalized-source-observations.json').read_text())['tables']['fy_2025']

def write(name, value):
    (HERE/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')

SOURCES = [
 {'id':'N01','url':'https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Q-A-Session.pdf','date':'2026-05-21','locator':'PDF pp6–7 and11','type':'primary management plan; reread','finding':'Filosa links Chrysler launch/sales maturation to 2028, and Ram pickup expansion to late2027–2029. CFO describes NA mix as broadly neutral versus2025 during2028–30.','limit':'No individual Chrysler delivery month or model sales target. Spoken pickup cadence and platform2028 SOP do not establish 2027 deliveries.'},
 {'id':'N02','url':'https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-North-America.pdf','date':'2026-05-21','locator':'PDF pp3,5','type':'primary management plan; reread','finding':'Three crossovers below Pacifica: one STLA One midsize and two related European-platform vehicles. Two Chrysler entry points below$30k planned by2030.','limit':'Positioning and pricing targets are not tested willingness to buy or final transaction prices.'},
 {'id':'N03','url':'https://www.motortrend.com/features/2027-chrysler-lineup-updates-changes','date':'2026-07-14','locator':'Airflow and Arrow/Arrow Cross sections','type':'secondary reporting','finding':'Lists Airflow and Arrow/Arrow Cross as expected2028 products.','limit':'Model year is not calendar year; precise SOP, customer arrival, powertrain and price commitments require manufacturer confirmation.'},
 {'id':'N04','url':'https://investor.gm.com/static-files/be64d2c4-adee-41e8-9c97-fa478654e9e7','date':'2024-01-03','locator':'one-page2023 sales table, Envista/Trax/EncoreGX/Trailblazer','type':'primary observed US retail+fleet','finding':'Envista2023 13,302/Q4 7,917; Trax109,382/Q4 44,127; EncoreGX64,149; Trailblazer111,014.','limit':'Envista new; Trax replaced an existing model. Supply, price and brand reach differ from future Chrysler. Parsed column labels checked; direct download403 prevented local render.'},
 {'id':'N05','url':'https://investors.gm.com/static-files/e1bb38a4-aaf9-4141-b44a-4c61c1f2ec54','date':'2025-01-03','locator':'one-page2024 sales table','type':'primary observed US retail+fleet','finding':'Envista51,316; Trax200,689; EncoreGX58,239; Trailblazer104,398; Colorado98,012; Canyon38,215.','limit':'Successful affordable launches are selected precedents, not the average outcome. Different vehicles and periods. Direct download403; parsed column labels verified.'},
 {'id':'N06','url':'https://news.buick.com/newsroom.detail.html/Pages/news/us/en/2023/apr/0417-envista.html','date':'2023-04-17','locator':'availability, pricing and MSRP footnote','type':'primary launch announcement','finding':'Envista planned customer arrival summer2023; entry$23,495 includes destination.','limit':'Announced summer arrival does not reveal exact first selling day. Cheaper than an unspecified future sub$30k Chrysler.'},
 {'id':'N07','url':'https://investor.gm.com/static-files/1294f515-0131-4d38-986e-f4d3160e7a68','date':'2026-10-01','locator':'one-pageQ3 table, Silverado and Sierra LD/HD rows','type':'primary observed US retail+fleet','finding':'Q3 GM combinedHD72,882 vs79,954; LD156,546 vs143,173. YTDHD212,015 vs238,503.','limit':'GM is a partial peer set, not the entire segment; chassis scope can differ from Ram. No causal attribution. Direct download403; parsed column labels verified.'},
 {'id':'N08','url':'https://investor.gm.com/news-releases/news-release-details/gms-winning-portfolio-continues-getting-stronger/','date':'2026-10-01','locator':'pickup launch paragraph','type':'primary competitor plan','finding':'Next-generation Silverado/Sierra dealer arrivals planned Q42026.','limit':'A competitive event, not a measured future Ram sales loss. GM reported total sales−6% with EV/portfolio effects, not universal demand growth.'},
 {'id':'N09','url':'https://www.sec.gov/Archives/edgar/data/37996/000003799626000184/exhibit99q32026salesrele.htm','date':'2026-10-02','locator':'Explorer/Bronco and SuperDuty passages','type':'primary issuer sales and production','finding':'ExplorerYTD189,210,+17.6%; BroncoQ3 38,020,YTD114,956.','limit':'SuperDuty110,275 is production, not sales. Ford own retail/pricing claims not independent market measurement.'},
 {'id':'N10','url':'https://www.prnewswire.com/news-releases/toyota-motor-north-america-reports-september-third-quarter-2026-us-sales-results-302896251.html','date':'2026-10-01','locator':'Toyota model table, Sienna row','type':'primary observed US retail+fleet','finding':'SiennaYTD84,770 vs75,876,+11.7%.','limit':'Use model row, not hybrid subtotal. Growing deliveries can reflect capacity; no full minivan segment total derived.'},
 {'id':'N11','url':'https://www.prnewswire.com/news-releases/stellantis-reports-q3-sales-302896446.html','date':'2026-10-01','locator':'model table and retail highlights','type':'primary observed US customer sales','finding':'Latest Q3/YTD totals324,277/958,463. Ram1500 retail+42% versus total+73%; Pacifica retail+7%,Durango+18%.','limit':'No retail unit levels, fleet shares, incentives or reorder profitability. Latest YTD can differ from sum of earlier quarter publications; preserve reconciliation.'},
 {'id':'N12','url':'https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-Q2-2026-Financial-Results-Call-Transcript.pdf','date':'2026-07-30','locator':'rental seasonality; Ram inventory question; Cherokee answer','type':'primary management testimony','finding':'Rental deliveries more concentrated inH1; Cherokee trims/channels restricted for economics, more competitive trims plannedH12027, Belvidere date withheld.','limit':'No model rental shares or estimated unit response. Funnel interest is management testimony. Transcript page numbering differs from licensed version.'},
 {'id':'N13','url':'https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-Preliminary-Results-H22025-Transcript-20260206.pdf','date':'2026-02-06','locator':'PDFp4 and launch Q&A','type':'primary management testimony','finding':'Already refers to certain discontinued US PHEVs byFebruary6; Cherokee/Charger delivery lead times discussed.','limit':'Does not identify every named model cessation date or date residual dealer stocks sold out. Do not automatically book another full PHEV exit shock in2028.'},
 {'id':'N14','url':'https://www.prnewswire.com/news-releases/fca-us-reports-fourth-quarter-and-full-year-2019-sales-300980866.html','date':'2020-01-03','locator':'Gladiator launch paragraph/table; City row','type':'primary historical launch outcome','finding':'Gladiator May debut,40,047 sales in2019,Q4 16,663; first part of launch year23,384 derived. City2019 12,920.','limit':'Gladiator enthusiast launch is not a demand forecast for Dakota; price/positioning and May–September window differ.'},
 {'id':'N15','url':'https://www.sec.gov/Archives/edgar/data/1144980/000114498026000089/a2026q2ex991.htm','date':'2026-07-28','locator':'Asbury Q2 release; full-text Stellantis search','type':'primary dealer-group disclosure','finding':'No Stellantis-specific text found in release.','limit':'Cannot upgrade2025 dealer testimony to2026 profitable replenishment; request detailed call transcript if needed.'},
 {'id':'N16','url':'https://www.chrysler.com/news/2027-chrysler-pacifica-debut.html','date':'2026-04-01','locator':'LX, orders, dealer-arrival and pricing sections','type':'primary product announcement','finding':'MY2027 Pacifica refresh; Voyager becomes LX; planned summer2026 arrival;LX$41,495+$1,995destination.','limit':'Not a calendar2027 launch; no demonstrated volume uplift.'},
 {'id':'R_HISTORY','path':'../volume-recovery-2026-10-14/historical-sales-ledger.json','type':'reused structured issuer observations','finding':'US model annual/quarterly actuals. Underlying releases and normalization in adjacent files.','limit':'Missing LD/HD pre2024 split and revised YTD differences retained.'},
 {'id':'R_RAM','path':'../model-diligence-2026-10-14/ram-diligence.json','type':'reused mechanisms and source registry','finding':'Launch availability, HEMI, Classic, dealer offers,HD supplier transition, City dated plan.','limit':'Old forecast paragraphs and derivative metadata superseded; source facts retained.'},
 {'id':'R_JEEP','path':'../model-diligence-2026-10-14/jeep-diligence.json','type':'reused mechanisms and source registry','finding':'4xe/non4xe split, financing, recalls, supply and product histories.','limit':'Source facts do not establish causal coefficients.'},
 {'id':'R_CD','path':'../model-diligence-2026-10-14/chrysler-dodge-diligence.json','type':'reused mechanisms and source registry','finding':'Minivan regrouping, Durango, Charger, Hornet and small-brand histories.','limit':'Prior forecast magnitudes are not validation.'},
 {'id':'R_OPERATOR','path':'../model-diligence-2026-10-14/support/operator-evidence.json','type':'reused dealer calls and practitioner records','finding':'Asbury2025 ordering/sales improvement; Lithia still described difficulty.','limit':'Conflicting selected dealers; no2026 model margin/replenishment series.'},
 {'id':'R_GC','path':'../model-diligence-2026-10-14/grand-cherokee-causal-followup/evidence.json','type':'reused historical causal audit','finding':'Price/availability,4xe decomposition, allocation and financing hypotheses.','limit':'2024 decomposition is arithmetic, not estimated driver contributions.'},
 {'id':'R_LAUNCH','path':'../investor-day-2026-05-21/north-america-launch-register.json','type':'reused visually checked investor-day deck register','finding':'Model identities and platformSOP timing; all2030 models not automatically2028 sales.','limit':'Read alongside stronger Q&A2028 launch statement N01.'},
 {'id':'R_SHIP','path':'/Users/kwu/Downloads/Stellantis N.V._6-K_2026-10-13_English.pdf','type':'primary preliminary shipments; previously inspected','finding':'Q3 NAshipments357k vs404k; GC/Compass each about25k lower, primarily downtime.','limit':'NAwholesale units cannot be assigned directly to US retail losses.'},
]
for s in SOURCES:s['accessed_or_reused']='2026-10-14'
write('sources.json',SOURCES)

# Values in thousands. Central figures are conditional planning levels, not fitted demand.
# Bounds are evidence-informed scenarios, not statistical confidence intervals.
SPECS = {
 'ram_ld': ([270,285,307],[260,285,320], 'Replace the unsupported+7% company/+1% market construction with a recent two-quarter operating level.',
  'Q2+Q3 actual sales of142,319 imply284,638 over twelve months; round to285k. This uses both quarters rather than carrying peak Q3 alone. YTD annualized269.5k and Q3 annualized306.6k bracket the2027 level. It assumes broadly normal annual seasonality, not a statistical seasonal adjustment.2028 maintenance at285k requires defending the recovered position against new GM pickups; there is no second HEMI uplift.',
  '2027 low270k retains the YTD pace; high307k sustains Q3.2028 low260k approximates the trailing263k level; high320k exceeds Q3 pace and requires further share gains. Endpoints are operating cases, not independently estimated probabilities.', ['N07','N08','N11','R_RAM']),
 'ram_hd': ([164,170,186],[160,170,186], 'Remove generic light-vehicle market growth; use commercial/pickup operating benchmarks.',
  '170k rounds2025 actual169,920 and sits between current YTD/Q3 pace164k and trailing174k. Restoring186k would recover the2024 level; it is an upside scenario, not a presumed outcome of the refresh. Hold170k in2028 because neither the supplier improvement nor current commercial data quantifies further gains.',
  'Low164k in2027 is current nine-month pace; low160k in2028 allows further softening. High186k is an observed prior annual outcome. GM HD weakness reduces confidence that all Ram weakness is a unique launch problem.', ['N07','N09','R_RAM']),
 'grand_cherokee': ([152,190,210],[150,190,216], 'Retain190k as an explicitly conditional level; reject the offsetting generic growth factors.',
  '2026 YTD adjusted only by the2025 Q4 share gives190,388; trailing sales195,625 and unadjustedYTD186,352 surround190k. H1 pace203,474 is an upside check, not the base.2025 seasonality itself includes channel effects and the choice to reuse it is an assumption. Maintain190k in2028 before the separately displayed launch-substitution sensitivity; do not assume a second shutdown rebound or recovery to244.6k.',
  'Low152k approximates Q3x4 and represents persistent sell-through weakness;2028 low150k rounds it. High210k/216k recalls2025/2024 annual levels and requires evidence of post-downtime retail replenishment without materially higher support.', ['N09','N12','R_GC','R_SHIP']),
 'wrangler': ([167,175,179],[155,175,190], 'Replace market/category/company percentages with an observed current operating level.',
  '2026 YTD annualized174,681 supports175k; H1 pace172,508 and Q3 pace179,028 are nearby.2025 actual167,322 provides the lower recent annual comparison.175k in2028 means maintaining this franchise despite Bronco competition, not assuming share recapture or a halo-edition multiplier.',
  '2027 limits167k–179k come from prior annual/currentQ3 anchors.2028 155k approximates2023/24 weak levels;190k requires higher sustainable demand than any2026 pace observed here. Wider horizon warrants wider uncertainty, not an invented mean-growth adjustment.', ['N09','N13','R_JEEP']),
 'minivans': ([126,140,150],[120,140,160], 'Remove unsupported category-growth and company-share coefficients; treat family sales consistently.',
  'Trailing137,236,Q3x4 137,964 and2025-seasonality-adjustedYTD141,755 support a rounded140k level. The MY2027 refresh was scheduled for summer2026 and is already partly in the observation window; it is not another full new-product event in2027. Hold140k in2028 before crossover-substitution sensitivity: utility differentiation supports retention, but hybrid competition and unknown fleet exposure prevent underwriting an extra9k.',
  '126k approximates2025 actual;120k approximates2023/24.150k/160k are clearly conditional growth cases, between current whole-year pace and Q2x4 of166.8k. They require sustained broader retail gains rather than annualizing a potentially fleet-heavy spring quarter.', ['N10','N11','N12','N16','R_CD']),
 'promaster': ([55,58,65],[50,58,66], 'Replace automatic growth with a fleet-replacement level.',
  'YTDannualized58,707,TTM56,325 and2019 56,409 support58k;Q3x4 65,256 is the stronger case.2023 81,663 did not persist and has no verified backlog mechanism for restoration. City-related substitution is in the separate portfolio sensitivity, not another hidden negative factor.',
  '55k approximatesH1pace55,432;65k approximatesQ3pace;2028 high66k approximates2024actual65,869. Low50k requires weaker fleet renewals or substantial City substitution.', ['R_RAM','N09']),
 'gladiator': ([38,45,57],[35,45,57], 'Use observed product-cycle and seasonal ranges; no generic pickup uplift.',
  '2025-seasonality-adjustedYTD45,629 andQ3pace47,644 support45k, balanced byH1pace38,066.2024actual42,123 is corroborating scale, not evidence the same causes recur.2028 central45k is before explicit Dakota-substitution sensitivity; it is not an assertion that new competition has no effect.',
  '38k isH1pace;57k approximates2025actual56,790.2028 low35k allows Dakota/category pressure. Price cuts in2024 did not prevent the decline, so discounts alone do not establish the upside.', ['N14','R_JEEP']),
 'compass': ([43,65,74],[40,65,80], 'Separate partial supply repair from longstanding product/competitive weakness.',
  'CurrentYTDpace63,783 andTTM66,914 support65k. H1pace74,052 predates theQ3 interruption but already reflected majorYoY losses. Neither the25k NAwholesale reduction nor European new-generation timing supports restoration to102k USsales.2028 central65k is before launch-substitution sensitivity; exact US replacement timing remains unresolved.',
  '43k approximatesQ3pace;74k isH1pace.2028 high80k requires a stronger offering and successful sell-through, not just resumed production.40k allows continued demand and internal substitution pressure.', ['R_JEEP','R_SHIP']),
 'cherokee': ([33,45,60],[35,48,70], 'Replace55k/70k with an explicit, conditional trim-availability ramp.',
  'ObservedQ3rate is3,448/month. Central2027 assumes3,500/month inH1 and4,000 inH2 after the promised more competitive trims:21k+24k=45k.2028 carries that4,000 exit pace for12months=48k, with no further rate acceleration. The extra552/month overQ3 is an assumed response, not a measured price elasticity; delivery economics and conversion must validate it.',
  '2027 low33k isQ2pace;high60k assumes5k/month.2028 low35k implies weak conversion;high70k requires substantially more availability/customer acceptance. Legacy191k in2019 is not a target for a different priced/generation proposition.', ['N11','N12','R_JEEP']),
 'wagoneer_family': ([45,55,60],[45,55,65], 'Maintain the regrouped family at a defensible recent pace.',
  'CurrentYTDpace56,856,TTM53,010 and2025-seasonality-adjustedYTD55,393 anchor55k. Q3pace49,980 is belowH1pace60,294, so no automatic continuation of early rebound. Wagoneer/Grand Wagoneer naming changes create no sales.2028 upside requires retaining a stronger luxury-family offering; central55k assumes no further proven rate gain.',
  '45k/60k bracket2025actual andH1pace;2028 upside65k would exceed observedH1pace and is conditional. RamSUV opportunity is a separate optional launch, not additive in the central path.', ['N11','R_JEEP']),
 'durango': ([77,88,91],[70,88,100], 'Anchor to an already recovered product, not a depressed2024 base.',
  'TTM88,081 andQ3pace91,020 support88k;H1pace77,150 is weaker. Recent retail growth supports real customer activity, but recovery started before the2026 R/T392 production milestone. Central88k in2028 requires retention of its differentiated performance/utility niche and does not assume an undated full replacement.',
  '2027 low77k/high91k are observed pace checks;2028 low70k approximates2023 volume and100k requires a further product/rate advance not yet measured.', ['N11','R_CD']),
 'charger': ([12,15,25],[10,15,30], 'Remove an unmeasured50%/25% ramp; keep observed demand scale and explicit upside.',
  'CombinedICE+BEVQ3 3,679 implies14,716 annual units, rounding15k.2026 YTDpace11,728 is lower but includes the delivery ramp. Central15k assumes the current quarterly pace persists. The return of gasoline/two- and four-door choice creates upside; without orders or retail conversion evidence it does not itself establish20k/25k. This is a no-further-share-gain planning case, not proof demand is capped at15k.',
  'Low12k in2027 isYTDpace;25k/30k would require monthly deliveries2,083/2,500 vsQ3 1,226. Old Charger+Challenger demand is not preserved automatically across engines, prices and body styles.', ['N11','N13','R_CD']),
 'fiat_alfa': ([2.5,3,4],[2,3,5], 'Replace arbitrary percentage losses with small-brand current-rate cases.',
  'CurrentQ3pace2,492,TTM3,565 and2025-seasonality-adjustedYTD3,022 support3k. No separately underwritten majorUSlaunch is assumed through2028. This aggregation is proportionate to less than0.3% ofUSYTDsales.',
  '2027 range2.5–4k brackets currentQ3 andH1paces;2028 range2–5k is a broad retention/product-option stress, not a fitted trend.', ['R_CD']),
 'hornet': ([0,.1,.3],[0,0,.2], 'Retain small runoff, not a recovery.',
  'Q3only85units and official indefinite production pause support a small2027 stock tail, then zero central2028. GLH is tracked separately; it cannot be credited as Hornet retention without a dated replacement.',
  'Residual inventory unknown; upside is only200–300vehicles of runoff, not assumed restart.', ['R_CD']),
 'dodge_other': ([0,.05,.2],[0,0,.1], 'Retain explicit legacy tail.',
  'Latest Dodge brand less named models leaves159YTDvehicles and27Q3;50vehicles in2027 is an immaterial rundown convention. Zero2028 is an assumption about stock exhaustion, not reported inventory.',
  'KeepGLH separate to avoid hiding a potential launch inside legacy runoff.', ['N11','R_CD']),
}

# Launch scenarios: figures describe a specified calendar and uptake outcome.
# No probability is attached; central is a selected planning scenario, not expected value.
LAUNCHES = {
 'promaster_city': ([0,10,20],[5,13,25],
  'PlannedQ12027 dealer arrival, August2026 announced pricing, not observed orders.',
  'OldCity2018/19 sales13.8k/12.9k support a roughly13k established-franchise reference, not a guarantee for the larger/pricier replacement.2027 10k allows ramping;2028 13k represents recovery of that historical scale. Quarterly2027 1/2/3/4k is a scenario totaling10k, not sourced quarterly timing.',
  'Downside delays/weak fleet take-up; upside20–25k needs conquest beyond the former City franchise. Gross sales can divert ProMaster purchases.', ['R_RAM','N14']),
 'chrysler_new': ([0,10,20],[0,50,90],
  'Management explicitly links Chrysler launches/sales maturity with2028; individual delivery dates unknown. Secondary2028-model-year reporting is consistent, not definitive.',
  'Central assumes limitedH22027 sales totaling10k, then50k across ALL THREE crossovers in2028. Scale benchmark: Envista13,302 in its2023 launch year and51,316 in2024. We allocate one Envista-sized annual franchise across the Chrysler family, not three successes. Hornet9,336→20,559→9,365 is the internal failed-launch counterexample.50k is an analogy-based planning case, not a statistically estimated Chrysler outcome; its affordability, tariff and branding differences remain uncalibrated.',
  'Delayed=0/0; limited on-time uptake=5k/20k; central10k/50k; strong20k/90k.90k requires roughlytwo successful affordable franchises. Do not split50k among Airflow/Arrow/ArrowCross without evidence. Internal substitution explicitly stress-tested at portfolio level.', ['N01','N02','N03','N04','N05','N06','R_CD']),
 'ram_dakota': ([0,0,5],[0,20,40],
  'Platform plan2028SOP; Q&A references late2027–2029 and meaningful2028 pickup sales. Calendar uncertain.',
  'Central assumesH22028 UScustomer arrival with5k then15k quarter sales=20k. Comparison: Gladiator sold23,384 between itsMay2019 debut andSeptember, and40,047 throughDecember. Dakota20k over an assumed six-month window is below that enthusiast-launch scale; different price, competitive set and brand appeal make this a capacity/uptake scenario, not a transferable demand coefficient.',
  'Zero2027 central reflects platformSOP;5k early upside reconciles spoken cadence.2028 zero is delay,40k resembles Glads first partial year. Potential diversion from1500/Gladiator must be deducted when aggregating.', ['N01','N14','R_LAUNCH']),
 'ram_compact': ([0,0,5],[0,10,35],
  '2028SOP platform plan; exactUSprice/arrival and hybrid offering unverified.',
  'Central10k assumes laterH22028 entry with3k then7k quarterly. It is a weaker planning input than Dakota: no matched USlaunch benchmark was recovered in this pass. The truck addresses a different use case; Maverick hybrid success demonstrates the relevance of price/powertrain, not transferability to Rampage-based Ram. Treat the10k as explicitly low-confidence and removable, not a sourced estimate.',
  'Delayed0;strong35k approximatelya full small-pickup franchise, requiring evidence of price and consumer orders. No central2027units. Named and quantified scenario prevents a hidden omission; not yet a defensible narrow range.', ['N01','N09','R_LAUNCH']),
 'ram_suv': ([0,0,0],[0,0,10],
  'Appears in2030lineup; no firm through2028 customer delivery date.',
  'Explicit zero central through2028 is a timing decision, not cancellation or zero demand. Optional10k2028 sensitivity is an illustrative partial launch, not a model forecast calibrated from demand.',
  'Potential Wagoneer/Durango overlap; add only alongside a dated milestone.', ['R_LAUNCH']),
 'wagoneer_s': ([.5,.6,3],[0,.6,5],
  'Currently selling at very low reported volumes; broad restart/delivery improvement unverified.',
  'Q3 146 implies584annual units; round600 rather than leave blank. Prior2025 10,864 was not sustained. Central600 is a current-scale continuation; substantial restart remains upside, not another restored2025 cohort.',
  '2027up3k/2028up5k require demonstrated deliveries;zero2028 downside permits winddown. EV price/support and demand environment differ from gasolineWagoneer.', ['N11','R_JEEP']),
 'recon': ([0,.1,5],[0,.1,10],
  '82YTD and35Q3 reported units; broad retail launch versus limited early delivery scope unresolved. LaterICEtiming undated.',
  'Current annual pace109–140 supports only a100vehicle maintenance case. This is not a forecast of mature Recon demand.5k/10k upside is a broad launch sensitivity requiring evidence of scaled production and funded orders; no automatic Wrangler cannibalization rate.',
  'Material restart cannot be underwritten from the current tiny denominator. Maintain explicit scenario coverage rather than silently removing the nameplate.', ['N11','R_JEEP','R_LAUNCH']),
 'dodge_glh': ([0,0,0],[0,0,15],
  'Named in2030 productplan; no sufficiently established2028 customer arrival in this evidence set.',
  'Zero central is a timing assumption.15k partial-year2028 upside is a scenario of a modest launch, smaller than Hornet firstfull-year20,559; not proofGLHshares its demand. Track separately from Hornet and legacy runoff.',
  'Change central only with specific order/production/customer milestones. Possible Chrysler/Compass overlap.', ['R_LAUNCH','R_CD']),
}

def scenarios(v):return dict(zip(['downside','base','upside'],[round(x*1000) for x in v]))

def anchors(a):
    y,q=a.get('2026YTDQ3A'),a.get('2026Q3A');p,pq=a.get('2025A'),a.get('2025Q4A')
    z={}
    if y is not None:z['ytd_annualized']=y*4/3
    if q is not None:z['q3_annualized']=q*4
    if y is not None and q is not None:z['h1_annualized_latest_ytd_basis']=(y-q)*2
    if y is not None and pq is not None:z['trailing_four_quarters']=y+pq
    if p and pq is not None and p>pq and y is not None:
        z['prior_q4_share']=pq/p;z['ytd_adjusted_using_2025_pattern']=y/(1-pq/p)
    return z

ROWS=[]
for id,s in SPECS.items():
    old=BY_ID[id];dossier_file='ram-diligence.json' if old['brand']=='Ram' else 'jeep-diligence.json' if old['brand']=='Jeep' else 'chrysler-dodge-diligence.json'
    dossier=json.loads((HERE/'baseline'/dossier_file).read_text())
    ds=next((r for r in dossier.get('models',dossier.get('rows',dossier.get('families',[]))) if r['id']==id),{})
    ROWS.append({'id':id,'family':old['family'],'brand':old['brand'],'kind':'continuing','2027':scenarios(s[0]),'2028':scenarios(s[1]),'old_2027':old['2027F_units'],'old_2028':old['2028F_units'],'action':s[2],'construction':s[3],'range_basis':s[4],'sources':s[5],'historical_actuals':old['historical_actual_units'],'derived_anchors':anchors(old['historical_actual_units']),'old_method':old['method'],'old_method_evidence_verdict':'Descriptive source evidence may support direction or operating level; D097 forward coefficients were assumed and not independently calibrated.','historical_story':ds.get('historical_sequence'),'customer_mechanism':ds.get('customer_mechanism',ds.get('thesis',old['thesis'])),'dealer_mechanism':ds.get('dealer_mechanism','Ordering availability and commercial competitiveness matter; no representative model-level profit/reorder panel exists. See R_OPERATOR and the family source register.'),'action_status':ds.get('action_status'),'counterevidence':ds.get('counterevidence',ds.get('competing_mechanisms')),'price_mix':old['pricing_incentive_mix'],'falsifier':old['falsifier'],'magnitude_status':'Conditional judgment anchored to observed volumes; no fitted elasticity or independently validated2028 point estimate.','workbook_admission':'Proposed central operating case only, with full scenario range and conditions; not automatically approved.'})

for id,s in LAUNCHES.items():
    old=BY_ID.get(id)
    name=old['family'] if old else 'Dodge GLH possible replacement'
    brand=old['brand'] if old else 'Dodge'
    ROWS.append({'id':id,'family':name,'brand':brand,'kind':'launch_or_relaunch' if id not in ['wagoneer_s','recon'] else 'limited_current_delivery','2027':scenarios(s[0]),'2028':scenarios(s[1]),'old_2027':old['2027F_units'] if old else None,'old_2028':old['2028F_units'] if old else None,'action':'Replace missing allocation or unsupported ramp with explicitly conditional timing/uptake cases.','timing':s[2],'construction':s[3],'range_basis':s[4],'sources':s[5],'historical_actuals':old['historical_actual_units'] if old else {},'derived_anchors':anchors(old['historical_actual_units']) if old else {},'old_method':old['method'] if old else 'Not a distinct numerical forecast row.','old_method_evidence_verdict':'Product plan is evidenced; exact delivery dates, attainable volumes and substitution are not measured.','price_mix':old['pricing_incentive_mix'] if old else 'Affordable/performance positioning and actual manufacturer economics unresolved.','falsifier':'Dated launch milestones fail; observed order conversion or subsequent deliveries are materially outside the selected scenario; volumes require uneconomic sustained support.','magnitude_status':'Analogy or stated scenario, not management guidance or statistical expected value.','workbook_admission':'Scenario input; retain timing/uptake and substitution sensitivities. No unsupported model-level OEM revenue.'})

for id,brand,name in [('renegade','Jeep','Legacy Jeep / unlisted residual'),('chrysler_runoff','Chrysler','Chrysler legacy runoff')]:
    ROWS.append({'id':id,'family':name,'brand':brand,'kind':'runoff','2027':scenarios([0,.05,.2]),'2028':scenarios([0,0,.1]),'old_2027':None,'old_2028':None,'action':'Explicit immaterial legacy tail; no historical residual dropped.','construction':'50units in2027,zero2028 is a rundown convention. Actual residual inventory unavailable.','range_basis':'0–200/100vehicle tail; not a fitted decline.','sources':['N11','R_HISTORY'],'historical_actuals':{},'derived_anchors':{},'magnitude_status':'Assumed immaterial runoff.','price_mix':'Immaterial at portfolio scale; no price uplift.','falsifier':'Material residual deliveries or a distinct new product must be separated.','workbook_admission':'Explicit residual convention.'})

for r in ROWS:
    if r['id']=='dodge_other':r['family']='Dodge legacy runoff excluding GLH'
    if r['id']=='chrysler_new':r['family']='Chrysler Airflow / Arrow / Arrow Cross combined'
    r['evidence_support']={'observed_level':'Reported history or direct launch precedent where provided; tiny-volume and not-yet-launched rows cannot reveal mature demand.','direction':'Mechanisms and competing observations assessed in construction/history; no causal identification.','forward_magnitude':'Judgmental scenario, not independently calibrated. New compact Ram and optional undated launches particularly weak.'}
    r['2025_actual']=r['historical_actuals'].get('2025A') or 0
    if r['id']=='renegade':
        names=['Compass','Wrangler','Gladiator','Recon','Cherokee','Grand Cherokee','Wagoneer S','Wagoneer','Grand Wagoneer']
        r['2025_actual']=FY25['JEEP BRAND']['ytd_current']-sum(FY25[n]['ytd_current'] for n in names)
    if r['id']=='chrysler_runoff':
        r['2025_actual']=FY25['CHRYSLER BRAND']['ytd_current']-FY25['Pacifica']['ytd_current']-FY25['Voyager']['ytd_current']

# Current actual reconciliation: brand totals are authoritative; hidden residuals are retained.
ACTUAL_MAP={'ram_ld':['Ram LD PU'],'ram_hd':['Ram HD PU'],'promaster':['ProMaster Van'],'promaster_city':['ProMaster City'],'grand_cherokee':['Grand Cherokee'],'wrangler':['Wrangler'],'gladiator':['Gladiator'],'compass':['Compass'],'cherokee':['Cherokee HEV'],'wagoneer_family':['Wagoneer/G. Wagoneer'],'wagoneer_s':['Wagoneer S'],'recon':['Recon'],'minivans':['Pacifica'],'durango':['Durango'],'charger':['Charger ICE','Charger BEV'],'hornet':['Hornet'],'fiat_alfa':['FIAT BRAND','ALFA ROMEO']}
for r in ROWS:
    if r['id'] in ACTUAL_MAP:
        names=ACTUAL_MAP[r['id']];r['2026YTD_actual']=sum(RAW[n]['ytd_current'] for n in names);r['2026Q3_actual']=sum(RAW[n]['quarter_current'] for n in names)
    elif r['id']=='renegade':
        names=['Compass','Wrangler','Gladiator','Recon','Cherokee HEV','Grand Cherokee','Wagoneer S','Wagoneer/G. Wagoneer'];r['2026YTD_actual']=RAW['JEEP BRAND']['ytd_current']-sum(RAW[n]['ytd_current'] for n in names);r['2026Q3_actual']=RAW['JEEP BRAND']['quarter_current']-sum(RAW[n]['quarter_current'] for n in names)
    elif r['id']=='chrysler_runoff':
        r['2026YTD_actual']=RAW['CHRYSLER BRAND']['ytd_current']-RAW['Pacifica']['ytd_current'];r['2026Q3_actual']=RAW['CHRYSLER BRAND']['quarter_current']-RAW['Pacifica']['quarter_current']
    elif r['id']=='dodge_other':
        ns=['Hornet','Charger ICE','Charger BEV','Durango'];r['2026YTD_actual']=RAW['DODGE BRAND']['ytd_current']-sum(RAW[n]['ytd_current'] for n in ns);r['2026Q3_actual']=RAW['DODGE BRAND']['quarter_current']-sum(RAW[n]['quarter_current'] for n in ns)
    else:r['2026YTD_actual']=0;r['2026Q3_actual']=0;r['zero_actual_status']='No separate named model in reported table; not an independently disclosed explicit zero.'
    for year in ['2027','2028']:
        old=r.get('old_'+year);base=old.get('base') if isinstance(old,dict) else None
        r['delta_'+year+'_versus_old_base']=r[year]['base']-base if base is not None else None
    r['annual_base_yoy_2028_pct']=(r['2028']['base']/r['2027']['base']-1)*100 if r['2027']['base'] else None
    r['share_2026YTD_pct']=r['2026YTD_actual']/RAW['STELLANTIS US']['ytd_current']*100

PEERS = {
 'GM_HD_Q3_growth_pct':((44278+28604)/(49231+30723)-1)*100,
 'GM_HD_YTD_growth_pct':((133769+78246)/(153750+84753)-1)*100,
 'GM_LD_Q3_growth_pct':((100221+56325)/(88460+54713)-1)*100,
 'Ram_HD_Q3_growth_pct':(41107/43717-1)*100,
 'Ram_HD_YTD_growth_pct':(123201/119122-1)*100,
 'Ram_LD_Q3_growth_pct':(76650/44349-1)*100,
 'Ram_LD_Q2_Q3_annualized':(65669+76650)*2,
 'Envista_2023_to_2024_increase':51316-13302,
 'Encore_GX_2023_to_2024_change':58239-64149,
 'selected_four_GM_small_SUV_2023':13302+64149+109382+111014,
 'selected_four_GM_small_SUV_2024':51316+58239+200689+104398,
 'note':'SelectedGMbasket is not full segment or measured cannibalization. One sibling falling does not establish customers moved to another. GM observations calibrate alternatives, not forecast causality.'}
write('comparisons.json',PEERS)

# Small, clearly limited retrospective benchmark. Not a fit or a forecast validation.
BACKCHECK=[]
for id in ['ram_ld','ram_hd']:
    a=BY_ID[id]['historical_actual_units'];p=a['2024Q3A']*4;actual=a['2025A']
    BACKCHECK.append({'id':id,'information_anchor':'Q3 2024 annualized','benchmark_forecast_for_2025':p,'observed_2025':actual,'error_pct_of_actual':(p/actual-1)*100})
write('anchor-backcheck.json',{'method':'Freeze Q3 2024 quarterly pace and compare with FY2025 realization. Two available LD/HD observations only; no fitting, no confidence-interval inference, not a test of D098 itself.','rows':BACKCHECK,'lesson':'Even observed pace anchors can miss subsequent annual volumes materially. D098 replaces opaque coefficients with transparent operating cases, not with a proven forecasting model.'})

# Replicate observed phasing only where credible enough as an explicit convention.
# Other quarterly cells remain null: unsupported exact quarterly profiles are not invented.
PHASING=[]
for id in ['ram_hd','wrangler','minivans','promaster','wagoneer_family','durango']:
    r=next(x for x in ROWS if x['id']==id);a=r['historical_actuals'];qs=[a.get(f'2025Q{q}A') for q in range(1,5)]
    if all(x is not None for x in qs) and sum(qs)>0:
        shares=[x/sum(qs) for x in qs]
        for yr in ['2027','2028']:
            vals=[round(r[yr]['base']*x) for x in shares];vals[-1]+=r[yr]['base']-sum(vals)
            PHASING.append({'id':id,'year':int(yr),'quarter_units':vals,'method':'2025 observed quarterly distribution, normalized to its four-quarter sum; explicit repeat-seasonality convention, not a separate forecast.','source_quarters':qs,'source_annual':a.get('2025A'),'source_sum_minus_reported_annual':sum(qs)-a.get('2025A',sum(qs)),'limitation':'Only one recent annual cycle; product/channel changes can alter seasonality. Not independently validated quarterly demand.'})
for id,yr,vals in [('cherokee',2027,[10500,10500,12000,12000]),('cherokee',2028,[12000]*4),('chrysler_new',2027,[0,0,3000,7000]),('chrysler_new',2028,[8000,12000,14000,16000]),('ram_dakota',2028,[0,0,5000,15000]),('ram_compact',2028,[0,0,3000,7000]),('promaster_city',2027,[1000,2000,3000,4000])]:
    PHASING.append({'id':id,'year':yr,'quarter_units':vals,'method':'Explicit conditional launch/trim ramp. Quarter of arrival and intra-year distribution are assumptions; annual benchmarks do not verify each quarter.','limitation':'Scenario-only phasing; move quarters when milestones change.'})
write('quarterly-scenarios.json',{'rows':PHASING,'other_rows':'Quarterly inputs not populated where stable seasonality or a stated launch scenario is not established. Annual model does not require fabricating quarterly precision.'})

TOTALS={}
launch_pool=['promaster_city','chrysler_new','ram_dakota','ram_compact']
for yr in ['2027','2028']:
    TOTALS[yr]={s:sum(r[yr][s] for r in ROWS) for s in ['downside','base','upside']}
    gross_pool=sum(r[yr]['base'] for r in ROWS if r['id'] in launch_pool)
    TOTALS[yr]['launch_gross_pool_base']=gross_pool
    TOTALS[yr]['continuing_and_other_base']=TOTALS[yr]['base']-gross_pool
    TOTALS[yr]['net_total_substitution_sensitivities']=[{'assumed_internal_substitution_pct':p,'units_to_remove_from_incumbent_rows':round(gross_pool*p/100),'net_us_total':round(TOTALS[yr]['base']-gross_pool*p/100)} for p in [0,20,40,100]]
    TOTALS[yr]['selected_substitution_rate']=None
    TOTALS[yr]['old_quantified_subtotal']=BASE['totals']['quantified_'+yr]['base']
    TOTALS[yr]['gross_delta_vs_old_incomplete_subtotal']=TOTALS[yr]['base']-TOTALS[yr]['old_quantified_subtotal']
    TOTALS[yr]['variance_bridge']={
      'old_quantified_subtotal':TOTALS[yr]['old_quantified_subtotal'],
      'revisions_to_previously_quantified_rows':sum(r['delta_'+yr+'_versus_old_base'] or 0 for r in ROWS),
      'newly_allocated_rows':sum(r[yr]['base'] for r in ROWS if r['delta_'+yr+'_versus_old_base'] is None),
      'gross_new_total':TOTALS[yr]['base'],
      'substitution_deduction':'Unselected; sensitivities separate. Newly allocated does not mean observed incremental demand.'}
TOTALS['meaning']='Gross family planning cases before deduction of launch-induced incumbent losses. Sum of low/high cases is a common-condition stress, not a probability interval. No selected central net-US forecast: substitution is unresolved.20/40% are sensitivities, not researched coefficients;100% demonstrates full displacement. Expansion of already-selling Cherokee/Charger can cause further overlap not calibrated by this pool.'

write('proposed-forecast-inputs.json',{'as_of':'2026-10-14','decision':'D098','status':'Replaces D097 as current research proposal; conditional operating scenarios, not approved workbook forecasts.','scope':'US reported customer deliveries including retail and fleet; excludes Maserati, as does issuer sales table.','rows':ROWS,'totals':TOTALS,'country_rows':BASE['country_rows'],'country_status':'Unchanged stale-baseline flat Canada/Mexico placeholders; no combinedNA forecast claimed.','pricing':'No model-level wholesale RPU, incentive elasticity, dealer inventory allocation or OEM revenue generated.','substitution':'Keep gross launch and incumbent forecasts visible. Allocate an evidenced/chosen substitution adjustment to donor models before workbook import; do not subtract again from launch rows.','quarterly_file':'quarterly-scenarios.json'})

checks={
 'baseline_hashes_unchanged':all(hashlib.sha256((HERE/'baseline'/Path(x['snapshot']).name).read_bytes()).hexdigest()==x['sha256'] for x in json.loads((HERE/'baseline/manifest.json').read_text())['files']),
 'actual_ytd_sum':sum(r['2026YTD_actual'] for r in ROWS),
 'reported_ytd':RAW['STELLANTIS US']['ytd_current'],
 'actual_q3_sum':sum(r['2026Q3_actual'] for r in ROWS),
 'reported_q3':RAW['STELLANTIS US']['quarter_current'],
 'actual_2025_sum':sum(r['2025_actual'] for r in ROWS),
 'reported_2025':FY25['FCA US LLC']['ytd_current'],
 'all_scenario_bounds_ordered':all(r[y]['downside']<=r[y]['base']<=r[y]['upside'] for r in ROWS for y in ['2027','2028']),
 'unique_ids':len(ROWS)==len({r['id'] for r in ROWS}),
 'quarterly_reconciles':all(sum(p['quarter_units'])==next(r for r in ROWS if r['id']==p['id'])[str(p['year'])]['base'] for p in PHASING),
 'old_explicit_rows_accounted':set(BY_ID).issubset({r['id'] for r in ROWS}),
 'workbook_modified':False,
 'independent_validation':'Not claimed. Actual arithmetic and peer comparisons are distinct from judgmental forecast calibration.',
}
assert checks['actual_ytd_sum']==checks['reported_ytd'],checks
assert checks['actual_q3_sum']==checks['reported_q3'],checks
assert checks['actual_2025_sum']==checks['reported_2025'],checks
for y in ['2027','2028']:
    b=TOTALS[y]['variance_bridge'];assert b['old_quantified_subtotal']+b['revisions_to_previously_quantified_rows']+b['newly_allocated_rows']==b['gross_new_total']
assert all(checks[k] for k in ['baseline_hashes_unchanged','all_scenario_bounds_ordered','unique_ids','quarterly_reconciles','old_explicit_rows_accounted'])
write('validation.json',checks)

# Model concentration is calculated rather than assumed.
core=['ram_ld','ram_hd','grand_cherokee','wrangler','minivans']
write('assumption-audit.json',{'as_of':'2026-10-14','decision':'D098','core_five_ytd_units':sum(r['2026YTD_actual'] for r in ROWS if r['id'] in core),'core_five_ytd_share_pct':sum(r['share_2026YTD_pct'] for r in ROWS if r['id'] in core),'common_assumptions':[{'assumption':'market+1%annually','verdict':'Not a source-derived2027/28 forecast; removed from point construction. Neutral common market maintained as an explicit scenario condition; macro upside/downside remains unestimated.'},{'assumption':'segment/company tilts','verdict':'Sources describe direction but do not estimate the individual1–7%coefficients. Replaced with observable-level or explicit launch scenarios.'},{'assumption':'newproducts need exact dates or remain unallocated','verdict':'Rejected. Include transparent timing cases, including delays, without claiming point certainty.'},{'assumption':'flat2028 means no analysis','verdict':'Flat central levels now mean maintained observed franchise with no proven incremental gain. Scenario bounds, competitor events and separate substitution sensitivities capture uncertainty; not disguised offsetting point adjustments.'},{'assumption':'all gross launches are incremental','verdict':'Rejected. No selected nettotal until internal substitution is chosen/evidenced.'}],'rows':[{k:r.get(k) for k in ['id','old_2027','old_2028','old_method','old_method_evidence_verdict','action','2027','2028','delta_2027_versus_old_base','delta_2028_versus_old_base','construction','sources','magnitude_status']} for r in ROWS]})

def n(v):return '—' if v is None else f'{v/1000:,.1f}'
lines=['# Stellantis US vehicle forecast audit', '', 'As of14 October2026. D098. Units are US customer deliveries, retail plus fleet, in thousands unless specified. The prior research forecast is preserved in baseline/. No workbook changed.', '',
'The audit removes unsupported growth coefficients, makes launch scenarios explicit and leaves unresolved substitution visible. This improves traceability; it does not establish precisely identified2028 consumer demand. The central values below are conditional planning cases. Current sales do not independently validate future demand.', '',
'## What changed', '',
'- Chrysler2028 timing has stronger primary support than the previous answer acknowledged: management explicitly connected2028 with Chrysler launch and sales maturation [N01]. Exact individual dates remain unknown.',
'- Ram HD is not uniquely weak: GM combinedHD sales fell8.8% inQ3 and11.1%YTD, versus Ram−6.0%/+3.4%. This changes causal attribution, not automatically Ram’s forecast [N07].',
'- GM plans refreshed full-size pickups forQ42026, a specific competitive challenge to retaining RamLD gains [N08].',
'- The Pacifica update was planned forsummer2026 despite its2027modelyear. Do not book it again as a new calendar2027 event [N16].',
'- Current source data support levels better than growth slopes. RamLD285k,GC190k,Wrangler175k,HD170k and minivans140k are operating cases with explicit alternatives, not model-fitted estimates.',
'- Older favourable Asbury commentary is2025 evidence; the retrieved2026 release contains no Stellantis-specific confirmation. Profitable fresh replenishment remains unverified [R_OPERATOR,N15].', '',
'## Current proposal and variance', '',
'Gross family sales before portfolio substitution. A blank old value was unallocated, not zero. Bounds are scenarios, not confidence intervals.', '',
'|Family|Old2027|Proposed2027 low/base/high|Old2028|Proposed2028 low/base/high|2028 base change|',
'|---|---:|---:|---:|---:|---:|']
for r in ROWS:
    ob=lambda y:r.get('old_'+y,{}).get('base') if isinstance(r.get('old_'+y),dict) else None
    ss=lambda y:' / '.join(n(r[y][s]) for s in ['downside','base','upside'])
    lines.append(f"|{r['family']}|{n(ob('2027'))}|{ss('2027')}|{n(ob('2028'))}|{ss('2028')}|{n(r['delta_2028_versus_old_base'])}|")
lines+=['','## Portfolio coverage and substitution','',f"All reported2026 YTD sales reconcile: **{checks['actual_ytd_sum']:,}**; Q3 **{checks['actual_q3_sum']:,}**. Residuals retained explicitly. The five core families account for{sum(r['share_2026YTD_pct'] for r in ROWS if r['id'] in core):.1f}% ofYTDunits, not NA revenue.",'','|Year|Old incomplete subtotal|Gross central case|Launch pool included|Net at20% substitution|Net at40% substitution|','|---|---:|---:|---:|---:|---:|']
for y in ['2027','2028']:
 t=TOTALS[y];lines.append(f"|{y}|{n(t['old_quantified_subtotal'])}|{n(t['base'])}|{n(t['launch_gross_pool_base'])}|{n(t['net_total_substitution_sensitivities'][1]['net_us_total'])}|{n(t['net_total_substitution_sensitivities'][2]['net_us_total'])}|")
lines += ['', 'The20%/40% values are unselected sensitivities, not observed substitution. With no donor-model evidence, publishing the gross sum as a net company forecast would repeat the original error in a different form. The pool includes City, Chrysler crossovers and both new Ram pickups; existing Cherokee/Charger expansion may create additional overlap. Future RamSUV/GLH central zeros are explicit timing decisions, with optional volumes visible. Maserati is outside the issuerUSsales scope.', '',
'Canada115k and Mexico91k remain prior flat placeholders based on2025, not verified2026 exit estimates. No completeNAcustomer forecast or wholesale/revenue bridge is claimed from those figures.', '',
'## Model level underwriting','',
'Historical stories and mechanisms below preserve earlier evidence. Only the new construction, scenarios and audit verdict supersede old forecast reasoning. Source registers in the cited files remain necessary for primary locators.','','']
for r in ROWS:
    lines += [f"### {r['family']}",'']
    if r.get('historical_story'):
        story=r['historical_story'];lines+=['**History.** '+(' '.join(story) if isinstance(story,list) else story),'']
    if r.get('customer_mechanism'):lines+=['**Customer and dealer mechanism.** '+str(r['customer_mechanism'])+' '+str(r.get('dealer_mechanism','')),'']
    if r.get('action_status'):
        st=r['action_status'];lines+=['**Repair status.** '+('; '.join(f'{k.replace("_"," ")}: {v}' for k,v in st.items()) if isinstance(st,dict) else '; '.join(st) if isinstance(st,list) else st),'']
    if r.get('timing'):lines+=['**Timing.** '+r['timing'],'']
    lines+=['**Numerical construction.** '+r['construction'],'','**Alternative outcomes.** '+r['range_basis'],'']
    if r.get('counterevidence'):
        c=r['counterevidence'];lines+=['**Competing explanations.** '+(' '.join(c) if isinstance(c,list) else str(c)),'']
    lines+=['**Price and mix.** '+r['price_mix'],'','**Would change the view.** '+r['falsifier'],'','Evidence: '+', '.join(r['sources'])+'. '+r['magnitude_status'],'']
lines+=['## Forecast method and limits','',
'A small retrospective check illustrates the danger of the anchor method itself: Q3 2024 annualized would have underpredicted 2025 Ram LD sales by21.1% and overpredicted Ram HD by15.1%. Only two cases are available here; this is not an error distribution or validation of the new estimates. The audit cannot turn recent pace into certainty merely by removing percentage overlays.', '',
'Recent pace, trailing sales and a reused seasonal distribution are alternative transformations of overlapping observations. They are not three independent proofs. Annualizing the latest quarter is a scale check, especially weak around fleet batches or launch interruptions.2025-pattern calculations are explicitly labeled and should not be used as reliable seasonal adjustments where product transitions dominate.', '',
'Existing-product central forecasts assume a broadly stable market environment and continued competitive financing. This is a null planning condition, not a sourced macro forecast. No generic+1% industry tailwind or fitted interest-rate sensitivity is embedded. Product-specific downside/upside cases provide operating alternatives but are not a quantified recession/boom model.', '',
'The launch comparison is deliberately two-sided. Envista demonstrates meaningful uptake of an affordable new crossover; Hornet demonstrates that an announced product and dealer distribution can still fail. Trax is a stronger outcome but had an established Chevrolet franchise and a different starting price, so its200.7k2024 sales are not assigned to new Chrysler vehicles. SelectedGMsmallSUV sales grew in aggregate even while some siblings fell; this does not identify individual buyer substitution.', '',
'The compact Ram10k, Recon scaling upside, GLH/RamSUV sensitivities and Chrysler product allocation are the weakest numerical components. They remain explicit scenarios. A precise dealer-arrival month, price/trim availability and real retail orders would improve them more than additional general product commentary.', '',
'## Quarterly and financial use','',
'quarterly-scenarios.json repeats observed2025quarter distributions only for selected continuing families and separately identifies assumed launch ramps. Other quarter cells remain unpopulated. Quarterly sums reconcile to annual amounts, but that arithmetic is not validation of within-year timing.2026Q4 and prior2026full-year assumptions are preserved in the baseline, not silently presented as actuals.', '',
'Customer sales are not wholesale shipments. Genuine replenishment would make shipments track customer demand more closely; destocking or launch stocking can cause divergence. No model-level dealer-stock series or unmatched shipment-minus-sales residual is invented. Manufacturer netRPU remains an estimated financial input, not MSRP or dealer discount. More entry vehicles can improve units while diluting average selling price. No extra mix uplift or discount removal is automatically awarded.', '',
'## Management comparison','',
'Management provides a2030NAportfolio ambition; this audit produces2027/28USfamily scenarios. They are not directly comparable. The disagreement is primarily evidentiary: we accept that broader coverage can add buyers but have not established launch conversion, profitable replenishment or gross-to-net incremental units. The Chrysler timing claim is stronger than previously acknowledged. Management’s NAneutral-mix framing also cautions against assuming every added unit improves mix [N01].', '',
'## What remains necessary','',
'1. Asbury Q22026 earnings-call transcript datedJuly28 and brand-level supplemental commentary; Lithia Q22026 call counterpart. Seek Stellantis-specific order acceptance, stock age, margins and fresh replenishment, rather than all-brandGPU.',
'2. Model-level retail/fleet registrations or sales, especially RamLD,GC and minivans, acrossQ42025–Q32026. Useful if available through existing subscriptions; no paid purchase authorized.',
'3. Individual Chrysler/Ram launch order openings, SOP and actual dealer arrivals, plus trims/price and funded-order evidence. No new transcript substitutes for delivery evidence if it contains only aspirations.',
'4. Donor-model or conquest/loyalty evidence for internal substitution. Owner prior-brand shares are not the same as counterfactual cannibalization.', '',
'These gaps do not invalidate the observed histories. They limit the confidence and workbook readiness of precise forward numbers. The central operating cases can be reviewed now; a fully netted company forecast requires an explicit substitution decision.', '',
'## Provenance and checks','',
'D098 records the user’s intervention: challenge unsupported percentage overlays and missing launches; require numerical anchors and a symmetric treatment of uncertainty. Snapshot hashes preserveD097. Sources were searched selectively across issuer sales, management Q&A, competitor launches, dealer reporting and inventory providers. No subagents, bulk scraping, paid data or workbook edits. GMdirectPDFdownloads returned403; web table columns were checked, but local visual rendering was not completed. Hyundai and older Ford redirect/search results were not used as numerical anchors. Current Coxbrand inventory was not recovered, and2025data were not mislabeled2026.', '',
'Machine checks cover snapshot preservation, complete currentUSsales reconciliation, unique family IDs, ordered scenario bounds and quarterly/annual reconciliation. They do not validate consumer-demand forecasts. Legacy D093–D097 files remain historical; this directory is the current research proposal.', '',
'## Sources','']
for s in SOURCES:
    ref=s.get('url',s.get('path'));lines += [f"- **{s['id']}** [{s['type']}]({ref}). {s.get('date','Reused14 October2026')}; {s.get('locator','see source register')}. {s['finding']} Limitation: {s['limit']}"]
def readable(text):
    # Repair compact legacy prose for the reader, preserving URLs and product suffixes.
    parts=re.split(r'(https?://[^\s)]+|\]\([^)]*\))',text)
    for i,t in enumerate(parts):
        if t.startswith('http') or t.startswith(']('):continue
        t=re.sub(r'([QH][1-4])(20\d\d)',r'\1 \2',t)
        t=re.sub(r'(?<=[A-Za-z])(20\d{2})',r' \1',t)
        t=re.sub(r'(20\d{2})(?=[A-Za-z])',r'\1 ',t)
        t=re.sub(r'(?<=[a-z])(?=\d)', ' ',t)
        t=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',t)
        t=re.sub(r'(?<=[0-9%])(?=[A-Za-z])',lambda m:' ',t)
        t=t.replace('4 xe','4xe').replace('x 4','x4').replace('V 8','V8').replace('Pro Master','ProMaster')
        t=t.replace('full-size','full-size').replace('LD 285','LD 285')
        t=re.sub(r'(?<=[;:])(?=[A-Za-z0-9])',' ',t)
        t=re.sub(r'(?<=,)(?=[A-Za-z])',' ',t)
        t=re.sub(r'\b(YTD|NA|US|HD|LD|OEM|SOP)(?=[a-z])',r'\1 ',t)
        t=re.sub(r'([A-Z]{2,})(?=\d{3,})',r'\1 ',t)
        t=re.sub(r'(?<=\.)(?=20\d{2}\b)',' ',t)
        t=re.sub(r'\b\d{5,6}\b',lambda m:f'{int(m.group()):,}',t)
        t=re.sub(r'(?<=\.)(?=[A-Z])',' ',t)
        t=t.replace('forsummer','for summer').replace('modelyear','model year').replace('e Torque','eTorque')
        parts[i]=t
    return ''.join(parts)
(HERE/'audit.md').write_text(readable('\n'.join(lines))+'\n')
print(json.dumps({'rows':len(ROWS),'totals':TOTALS,'checks':checks},indent=2))
