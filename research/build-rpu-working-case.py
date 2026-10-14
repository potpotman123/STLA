"""Small reproducible RPU calibration; no workbook edits or network calls."""
import json
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parent
BOOK = Path('/Users/kwu/Downloads/FINAL KW STLA MODEL.xlsx')
wb = openpyxl.load_workbook(BOOK, data_only=True)
s = wb['NA Volume Build']
proposal = json.loads((ROOT/'forecast-audit-2026-10-14/proposed-forecast-inputs.json').read_text())
# Relative net-price assumptions in USD, not observed wholesale averages.
usd = dict(ram_ld=54000, ram_hd=65000, grand_cherokee=45000, wrangler=46000,
           minivans=43000, promaster=43000, gladiator=42000, compass=30000,
           cherokee=33000, wagoneer_family=70000, durango=42000, charger=45000,
           fiat_alfa=38000, hornet=28000, dodge_other=32000, promaster_city=33000,
           chrysler_new=32000, ram_dakota=37000, ram_compact=30000, ram_suv=65000,
           wagoneer_s=55000, recon=55000, dodge_glh=30000, renegade=26000,
           chrysler_runoff=32000)
fx = 1.13  # FY2025 USD per EUR; only sets seed scale, cancelled by calibration.
raw = {k:v/fx for k,v in usd.items()}
rows = {7:'ram_ld',9:'ram_hd',11:'promaster',13:'promaster_city',20:'grand_cherokee',
        22:'wrangler',24:'gladiator',26:'compass',28:'cherokee',30:'wagoneer_family',
        32:'renegade',39:'minivans',41:'minivans',43:'chrysler_runoff',50:'durango',
        52:'charger',54:'hornet',56:'dodge_other',63:'fiat_alfa'}
ca_rel, mx_rel = .90, .70
input_rows={7:6,9:7,11:8,13:9,20:12,22:13,24:14,26:15,28:16,30:17,32:18,
            39:21,41:22,43:23,50:26,52:27,54:28,56:29,63:32,70:35,71:36}
def actual(r,c):
    if c==3:
        return sum(wb['NA Volume Inputs'].cell(input_rows[r],q).value for q in range(3,7))
    return s.cell(r,c).value
def history(cols):
    vols={r:sum(actual(r,c) for c in cols) for r in rows if r not in (39,41)}
    # Combine family; Q2 published family total avoids relying on estimated Voyager split.
    vols[39]=sum(41704 if c==5 else actual(39,c)+actual(41,c) for c in cols)
    vols[41]=0
    us=sum(vols.values()); ca=sum(actual(70,c) for c in cols)
    mx=sum(actual(71,c) for c in cols)
    us_price=sum(vols[r]*raw[k] for r,k in rows.items())/us
    na_price=us_price*(us+ca*ca_rel+mx*mx_rel)/(us+ca+mx)
    return dict(us_units=us,canada_units=ca,mexico_units=mx,raw_us_rpu=us_price,raw_na_rpu=na_price,
                workbook_row_sales_snapshot=vols)
h25=history([3]); h26=history([4,5])
target25=61165e6/1474000; target26=34307e6/824000
f25=target25/h25['raw_na_rpu']; f26=target26/h26['raw_na_rpu']
ref25={k:v*f25 for k,v in raw.items()}; ref26={k:v*f26 for k,v in raw.items()}
# Countries held at fixed reference effective RPU after H1 2026, not floated with US model mix.
ca26=h26['raw_us_rpu']*f26*ca_rel; mx26=h26['raw_us_rpu']*f26*mx_rel
def forecast(year, prices=None, us_incentive=0, ca_price=ca26, mx_price=mx26):
    prices=prices or ref26
    us=sum(r[str(year)]['base'] for r in proposal['rows'])
    dollars=sum(r[str(year)]['base']*(prices[r['id']]-us_incentive) for r in proposal['rows'])
    na=(dollars+115000*ca_price+91000*mx_price)/(us+206000)
    return dict(us_customer_sales=us,na_customer_sales=us+206000,us_effective_rpu=dollars/us,na_effective_rpu=na,
                revenue_at_hypothetical_1_6m_na_shipments_EURm=na*1.6)
base={y:forecast(y) for y in [2027,2028]}
tests=[]
for delta in [500,1000]:
    q=forecast(2028,us_incentive=delta)
    tests.append(dict(test=f'Extra EUR{delta} support per US vehicle',na_rpu=q['na_effective_rpu'],
                      change_na_rpu=q['na_effective_rpu']-base[2028]['na_effective_rpu']))
for group,ids in [('Ram LD and HD',['ram_ld','ram_hd']),('Grand Cherokee and Wrangler',['grand_cherokee','wrangler'])]:
    for shock in [-.1,.1]:
        p={k:v*(1+shock if k in ids else 1) for k,v in ref26.items()}
        q=forecast(2028,prices=p)
        tests.append(dict(test=f'{group} relative RPU {shock:+.0%}; no recalibration',change_na_rpu=q['na_effective_rpu']-base[2028]['na_effective_rpu']))
for factor in [.9,1.1]:
    q=forecast(2028,ca_price=ca26*factor,mx_price=mx26*factor)
    tests.append(dict(test=f'Canada and Mexico RPU {factor-1:+.0%}',change_na_rpu=q['na_effective_rpu']-base[2028]['na_effective_rpu']))
for shock in [-.2,.2]:
    p=dict(ref26); p['chrysler_new']*=1+shock
    q=forecast(2028,prices=p)
    tests.append(dict(test=f'New Chrysler family RPU {shock:+.0%}',change_na_rpu=q['na_effective_rpu']-base[2028]['na_effective_rpu']))
rounded={k:round(v/500)*500 for k,v in ref26.items()}
rounded_forecasts={y:forecast(y,prices=rounded,ca_price=round(ca26/500)*500,mx_price=round(mx26/500)*500) for y in [2027,2028]}
allrows=[]
for r in proposal['rows']:
    k=r['id']
    allrows.append(dict(id=k,model=r['family'],seed_net_price_USD_assumed=usd[k],
                        effective_reference_FY2025_EUR=ref25[k],effective_reference_H12026_EUR=ref26[k],
                        rounded_2027_2028_RPU_EUR=round(ref26[k]/500)*500,
                        forecast_units_2027=r['2027']['base'],forecast_units_2028=r['2028']['base']))
out=dict(as_of='2026-10-14',status='Recommended practical working case; not observed model wholesale revenue',
         method='All regional revenue allocated to effective RPU; no separately added non-vehicle revenue. Customer mix proxies wholesale mix.',
         historical_workbook=str(BOOK),source_evidence='rpu-evidence-2026-10-14.json',
         fx_source='https://data.ecb.europa.eu/data/datasets/EXR/EXR.A.USD.EUR.SP00.A',
         FX_note='1.13 USD/EUR seed conversion cancels in calibrated level. Forecasts hold calibrated EUR prices fixed; not a currency forecast.',
         canada_relative_price_assumed=ca_rel,mexico_relative_price_assumed=mx_rel,
         history_2025=h25,history_H12026=h26,reported_effective_rpu_2025=target25,reported_effective_rpu_H12026=target26,
         calibration_factor_2025=f25,calibration_factor_H12026=f26,
         implied_common_rebase_H12026_vs_2025=f26/f25-1,
         rebase_warning='Composite calibration residual includes FX, channel mix, trim mix and other revenue; NOT identified price or incentive movement; never pass this mechanically into price-only AOI.',
         forecasts=base,rounded_input_forecasts=rounded_forecasts,canada_forecast_rpu=ca26,mexico_forecast_rpu=mx26,model_rows=allrows,tests=tests,
         annual_same_model_net_price_growth_2027=0,annual_same_model_net_price_growth_2028=0,
         incremental_incentives_vs_H12026_reference_EUR=0,
         total_brand_incentives_EUR=None,
         other_regional_revenue_EURm=0,
         residual_note='Zero is a modeling allocation convention; other revenues embedded in effective RPU are not economically zero.',
         limits=['FY2025 and H12026 fit by construction, not independent validation.',
                 'Historical Wagoneer workbook grouping includes Wagoneer S; split not reconstructed for this low-materiality calibration.',
                 'Pacifica/Voyager use a common effective family RPU; no invented trim split.',
                 'D098 forecast volumes are gross before launch substitution; these are price tests, not endorsement of final shipment forecasts.',
                 'Customer-sales weighting assumes wholesale mix similarity; country price ratios are judgment.',
                 'Q3/Q4 2026 use H1 reference scenario pending reported financial results, not inferred actuals.',
                 'Round to EUR500 for model entry and recalculate aggregates; exact values retained only to reproduce arithmetic.',
                 'Blank historical model rows for future launches are hypothetical price equivalents, not actual 2025 model revenue.'])
assert abs(h25['us_units']-1260344)<1
assert abs(target25*1474000/1e6-61165)<1e-8
assert abs(target26*824000/1e6-34307)<1e-8
(ROOT/'rpu-working-assumptions-2026-10-14.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['reported_effective_rpu_2025','reported_effective_rpu_H12026','calibration_factor_2025','calibration_factor_H12026','implied_common_rebase_H12026_vs_2025','forecasts','canada_forecast_rpu','mexico_forecast_rpu','tests']},indent=2))
print([(r['id'],r['rounded_2027_2028_RPU_EUR']) for r in allrows])
