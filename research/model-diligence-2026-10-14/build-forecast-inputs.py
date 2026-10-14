from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
P=Path(__file__).resolve().parent
V=R/'research/volume-recovery-2026-10-14'
def read(p):return json.loads(p.read_text())
def save(n,d): (P/n).write_text(json.dumps(d,indent=2)+'\n')
raw=read(V/'normalized-source-observations.json')['tables']
hist={r['id']:r for r in read(V/'historical-sales-ledger.json')['rows']}
prior=read(V/'proposed-volume-inputs.json');pri={r['id']:r for r in prior['rows']}
root=read(P/'chrysler-dodge-diligence.json')
ram=read(P/'ram-diligence.json')['families'];jeep=read(P/'jeep-diligence.json')['models']
def trip(v):return v if isinstance(v,dict) or v is None else dict(zip(['downside','base','upside'],v))
allrows=[]
for group,rr in [('ram',ram),('jeep',jeep),('chrysler-dodge',root['rows'])]:
 for r in rr:
  id=r['id'];oldid='charger_family' if id=='charger' else id
  h=dict(hist.get(oldid,{}).get('annual_and_quarterly_sales_units',{}))
  if id=='charger':
   for year in ['2018A','2019A','2023A','2024A']:h[year]=None
   h['2018A']=raw['fy_2019']['Charger']['ytd_prior'];h['2019A']=raw['fy_2019']['Charger']['ytd_current'];h['2025A']=9562
   # Previous transition-family quarters included Challenger; rebuild Charger-only quarters.
   for q in [1,2]:
    for year,col in [(2026,'quarter_current'),(2025,'quarter_prior')]:
     table=raw[f'q{q}_2026'];h[f'{year}Q{q}A']=table['Charger'][col]+table['Charger BEV'][col]
   for year,col in [(2025,'quarter_current'),(2024,'quarter_prior')]:
    table=raw['fy_2025'];h[f'{year}Q4A']=table['Charger'][col]+table['Charger BEV'][col]
   for x in read(V/'support/2023-2024-model-sales.json')['rows']:
    if x['model']=='Charger':h['2023A']=x['units_2023'];h['2024A']=x['units_2024']
  brand=('Ram' if group=='ram' else 'Jeep') if group!='chrysler-dodge' else r['brand']
  q4=trip(r.get('q4_2026_units_down_base_up'));a27=trip(r.get('scenario_2027_units_down_base_up',r.get('annual_2027_units_down_base_up',r.get('units_2027_down_base_up'))));a28=trip(r.get('scenario_2028_units_down_base_up',r.get('annual_2028_units_down_base_up',r.get('units_2028_down_base_up'))))
  if id=='dodge_other':h={'2025A':raw['fy_2025']['DODGE BRAND']['ytd_current']-81168-9562-9365,'2026Q3A':27,'2026YTDQ3A':129}
  if id=='chrysler_new':
   # Keep new products unallocated; legacy residual is separate, not zero or a new launch.
   h={}
  actual_ytd=h.get('2026YTDQ3A');fy26={k:actual_ytd+v for k,v in q4.items()} if q4 is not None and actual_ytd is not None else None
  old=pri.get(oldid);old27=old['2027_units']['base'] if old else None;old28=old['2028_units']['base'] if old else None
  def growth(f,b):return {k:(v/b[k]-1)*100 if b[k] else None for k,v in f.items()} if f and b else None
  x={'id':id,'family':r['family'],'brand':brand,'historical_actual_units':h,'2026Q4F_units':q4,'2026FY_A_plus_F_units':fy26,'2027F_units':a27,'2028F_units':a28,'2026FY_yoy_pct':growth(fy26,{k:h.get('2025A') for k in fy26}) if fy26 and h.get('2025A') else None,'2027_yoy_pct':growth(a27,fy26),'2028_yoy_pct':growth(a28,a27),'2028_base_delta_vs_2026_base':a28['base']-fy26['base'] if a28 and fy26 else None,'2028_base_delta_vs_2025':a28['base']-h['2025A'] if a28 and h.get('2025A') is not None else None,'prior_2027_base':old27,'prior_2028_base':old28,'revision_2027_base':a27['base']-old27 if a27 and old27 is not None else None,'revision_2028_base':a28['base']-old28 if a28 and old28 is not None else None,'pricing_incentive_mix':r['pricing_mix_view'],'thesis':r['thesis'],'method':r['forecast_method'],'confidence':r['confidence'],'falsifier':r['falsifier'],'dossier':group+'-diligence.md','classification':'Actual source counts; forecast/price direction analyst judgments; null means not allocated','source_ids':r.get('evidence_ids',r.get('supporting_evidence_ids',[]))}
  if id=='promaster_city':x['2026FY_yoy_pct']=None;x['2027_yoy_pct']=None;x['growth_note']='Returning different product; percentage growth from one runoff unit is not economically useful.'
  allrows.append(x)
# Named main model mapping includes all requested rows without duplicate minivan or variant forecasts.
mapping=[{'requested_row':'Pacifica','treatment':'Use combined minivans family'},{'requested_row':'Voyager','treatment':'Included in minivans; standalone forward cell null/included, never added again'},{'requested_row':'Jeep other/new','treatment':'Wagoneer S and Recon unallocated; legacy/unlisted residual kept separately'},{'requested_row':'Ram other/new','treatment':'City quantified; Dakota, compact and SUV separately unallocated'},{'requested_row':'Dodge other/runoff','treatment':'Small legacy-tail scenario; GLH unallocated alongside, not included in legacy count'},{'requested_row':'Chrysler other/new/runoff','treatment':'New crossovers unallocated; 16-unit YTD brand residual separately preserved'}]
# Brand source reconciliation from exactly the latest same-vintage table.
t=raw['q3_2026'];groups={'Ram':['Ram LD PU','Ram HD PU','ProMaster Van','ProMaster City'],'Jeep':['Grand Cherokee','Wrangler','Gladiator','Compass','Cherokee HEV','Wagoneer/G. Wagoneer','Wagoneer S','Recon'],'Chrysler':['Pacifica'],'Dodge':['Durango','Charger ICE','Charger BEV','Hornet'],'Fiat':['500e','500X'],'Alfa':['Giulia','Stelvio','Tonale']};bn={'Ram':'RAM BRAND','Jeep':'JEEP BRAND','Chrysler':'CHRYSLER BRAND','Dodge':'DODGE BRAND','Fiat':'FIAT BRAND','Alfa':'ALFA ROMEO'}
recon=[]
for b,names in groups.items():
 rec={'brand':b}
 for period,col in [('2026Q3','quarter_current'),('2026YTD','ytd_current')]:
  named=sum(t[n][col] for n in names);total=t[bn[b]][col];rec[period]={'named':named,'unlisted_residual':total-named,'reported':total}
 recon.append(rec)
quant=[r for r in allrows if r['2026FY_A_plus_F_units'] and r['2027F_units'] and r['2028F_units']]
core=[r for r in quant if ('charger_family' if r['id']=='charger' else r['id']) in pri]
def sums(rr,key):return {k:sum(r[key][k] for r in rr) for k in ['downside','base','upside']}
tot={'quantified_2026':sums(quant,'2026FY_A_plus_F_units'),'quantified_2027':sums(quant,'2027F_units'),'quantified_2028':sums(quant,'2028F_units'),'core_13_2026':sums(core,'2026FY_A_plus_F_units'),'core_13_2027':sums(core,'2027F_units'),'core_13_2028':sums(core,'2028F_units'),'quantified_2025_actual':sum(r['historical_actual_units'].get('2025A',0) for r in quant),'quantified_2026YTD_actual':sum(r['historical_actual_units'].get('2026YTDQ3A',0) for r in quant),'all_reported_2025':1260344,'all_reported_2026YTD':958463,'warning':'Quantified subtotal excludes future unallocated launches and selected EVs; scenario sums are common-condition stresses, not confidence intervals or a complete company forecast. Core comparison moves Challenger from old transition family to runoff.'}
tot['quantified_2025_coverage_pct']=tot['quantified_2025_actual']/1260344*100;tot['quantified_2026YTD_coverage_pct']=tot['quantified_2026YTD_actual']/958463*100
for r in quant:
 r['share_quantified_2026_base_pct']=r['2026FY_A_plus_F_units']['base']/tot['quantified_2026']['base']*100;r['share_quantified_2028_base_pct']=r['2028F_units']['base']/tot['quantified_2028']['base']*100
# Exposure buckets are arithmetic, not mutually-exclusive causal loss assignments.
buckets={'continuing_partial_recovery':['ram_ld','grand_cherokee','compass','gladiator','charger'],'defend_recovered_or_stable_level':['ram_hd','promaster','wrangler','minivans','wagoneer_family','durango','fiat_alfa'],'returning_product_ramps':['cherokee','promaster_city'],'runoff':['hornet','dodge_other']}
bridge=[]
for bucket,ids in buckets.items():
 rr=[r for r in quant if r['id'] in ids];bridge.append({'bucket':bucket,'ids':ids,'2026_base':sum(r['2026FY_A_plus_F_units']['base'] for r in rr),'2028_base':sum(r['2028F_units']['base'] for r in rr),'change':sum(r['2028_base_delta_vs_2026_base'] for r in rr)})
checks={'brand_reconciliation':recon,'q3_brand_sum':sum(x['2026Q3']['reported'] for x in recon),'q3_reported_us':t['STELLANTIS US']['quarter_current'],'ytd_brand_sum':sum(x['2026YTD']['reported'] for x in recon),'ytd_reported_us':t['STELLANTIS US']['ytd_current'],'historical_vintage_adjustments':read(V/'historical-sales-ledger.json')['period_reconciliations'],'cherokee_prior_quarters_minus_latest_ytd':2489+8112+10344-20914,'quarter_forecast_policy':'2026 actual YTD plus Q4F exactly. Forecast years2027/28 are annual because seasonality/launch timing insufficient; no implicit quarterly model. For quarterly workbook later, explicit mechanical allocation may be approved; not done here.'}
checks['charger_2026_quarters_sum_exact']=sum(next(r for r in allrows if r['id']=='charger')['historical_actual_units'][f'2026Q{q}A'] for q in [1,2,3])==8796
checks['all_brand_reconcile']=checks['q3_brand_sum']==checks['q3_reported_us'] and checks['ytd_brand_sum']==checks['ytd_reported_us']
checks['scenarios_ordered']=all(r[k]['downside']<=r[k]['base']<=r[k]['upside'] for r in quant for k in ['2026Q4F_units','2027F_units','2028F_units'])
checks['q4_to_annual_exact']=all(r['2026FY_A_plus_F_units'][k]==r['historical_actual_units']['2026YTDQ3A']+r['2026Q4F_units'][k] for r in quant for k in ['downside','base','upside'])
checks['growth_bridge_exact']=sum(x['change'] for x in bridge)==tot['quantified_2028']['base']-tot['quantified_2026']['base']
assert all(checks[k] for k in ['all_brand_reconcile','scenarios_ordered','q4_to_annual_exact','growth_bridge_exact','charger_2026_quarters_sum_exact'])
obj={'as_of':'2026-10-14','status':'Research forecasts updated with Grand Cherokee stabilization base of 190000 in 2027 and 2028; not workbook-adopted','scope':'US issuer retail plus fleet sales, excluding Maserati. Maserati financial segment/reclassification scope must be handled separately in the regional financial reconciliation.','rows':allrows,'requested_row_mapping':mapping,'totals':tot,'growth_bridge':bridge,'country_rows':prior['country_rows'],'country_caveat':'Canada115k/Mexico91k remain flat rounded2025-baseline conventions;2026actual exit unrefreshed. Do not label them a new calibrated NA forecast. Customer sales and wholesale shipments remain separate.','unallocated':['Wagoneer S','Recon','Jeep legacy/unlisted residual','Chrysler legacy/unlisted residual','Dakota','compact Ram/Rampage-based','Ram SUV','Chrysler Airflow/Arrow/Arrow Cross','GLH successor'],'price_input_gate':'Directions and dated offers supported; numerical OEM pre-incentive RPU, incentive cost and within-family mix assumptions remain explicit analyst inputs pending regional reconciliation. No model-level actual price inferred.','checks_file':'validation.json'}
save('proposed-forecast-inputs.json',obj);save('validation.json',checks)
# Readable table keeps main numerical facts compact; row reasoning lives in dossiers.
def n(v):return '—' if v is None else f'{v/1000:,.1f}'
def tr(v):return 'unallocated' if v is None else ' / '.join(n(v[k]) for k in ['downside','base','upside'])
md=['# Proposed US model forecasts through 2028','As of 14 October 2026. Updated: Grand Cherokee 2027 and 2028 bases revised to 190,000 following causal review; all other scenario unit inputs unchanged. Units in thousands; D/B/U = downside/base/upside. These are rounded analyst scenarios, not measured demand estimates, management guidance or approved workbook inputs. Null/unallocated is not zero. All actual sales include retail and fleet and exclude Maserati.','## Model scenarios','|Family|2025 actual|2026 YTD actual|Q4 2026 D/B/U|FY2026 base|2027 D/B/U|2028 D/B/U|2028 base change vs prior|','|---|---:|---:|---:|---:|---:|---:|---:|']
for r in allrows:
 h=r['historical_actual_units'];fy=r['2026FY_A_plus_F_units'];md.append('|'+ '|'.join([r['family'],n(h.get('2025A')),n(h.get('2026YTDQ3A')),tr(r['2026Q4F_units']),n(fy['base']) if fy else 'unallocated',tr(r['2027F_units']),tr(r['2028F_units']),n(r['revision_2028_base'])])+'|')
md+=['','The quantified rows cover '+f"{tot['quantified_2025_coverage_pct']:.2f}% of2025 and {tot['quantified_2026YTD_coverage_pct']:.2f}% of latest 2026 YTD sales"+'. Historical unlisted residuals are reconciled separately. Future launch omissions can be much more material than their current sales shares.','## Growth and mix arithmetic','|Bucket|2026 base|2028 base|Change|','|---|---:|---:|---:|']
for b in bridge:md.append('|'+b['bucket'].replace('_',' ')+'|'+n(b['2026_base'])+'|'+n(b['2028_base'])+'|'+n(b['change'])+'|')
md+=['','Quantified subtotal: 2026 '+n(tot['quantified_2026']['base'])+'k, 2027 '+n(tot['quantified_2027']['base'])+'k, 2028 '+n(tot['quantified_2028']['base'])+'k. These sums exclude unallocated rows and are not full US forecasts.','## Growth rates and pricing conditions','|Family|2026 base YoY|2027 base YoY|2028 base YoY|2028 delta vs2026 k|2026→2028 unit weight|','|---|---:|---:|---:|---:|---:|']
def pct(x):return 'n.m.' if x is None else f'{x:+.1f}%'
for r in quant:
 md.append('|'+r['family']+'|'+'|'.join([pct(r.get(k,{}).get('base') if r.get(k) else None) for k in ['2026FY_yoy_pct','2027_yoy_pct','2028_yoy_pct']])+'|'+n(r['2028_base_delta_vs_2026_base'])+'|'+f"{r['share_quantified_2026_base_pct']:.1f}% → {r['share_quantified_2028_base_pct']:.1f}%"+'|')
md+=['','Unit weights cover only the quantified customer-sales set; they are mix proxies, not observed regional wholesale weights. Powertrain and trim changes remain within each family. No extra aggregate mix uplift is added.','## Conditions for each forecast']
for r in allrows:md+=['### '+r['family'],r['thesis'],r['method'],'Pricing and mix: '+r['pricing_incentive_mix'],'Falsification: '+r['falsifier'],'Details: ['+r['dossier']+']('+r['dossier']+').']
md+=['## Geography and model admission','Canada and Mexico retain one flat placeholder row each:115k and91k. Those are rounded2025 anchors, not refreshed2026 results. Regional wholesale must be forecast independently and constrained by customer sales and inventory; no model-level inventory history is manufactured. No consolidated revenue or AOI is calculated from consumer MSRP.','2026 YTD is actual; Q4 is forecast.2027/28 quarterly estimates are intentionally not fabricated. Growth rates are derived from units; City growth off one runoff unit is suppressed as not meaningful. Side-by-side base changes are judgments about evidence and required pace, not estimates of precisely how many sales each mechanism causes.','Read [validation](validation.json), [portfolio view](README.md), and the three dossiers before using any number. The required main Pacifica/Voyager rows map to one combined family; a separate Voyager growth forecast would double count renaming.']
table_text='\n\n'.join(md).replace('\n\n|','\n|')
import re
table_text=re.sub(r'(^## .+\n)(\|)',r'\1\n\2',table_text,flags=re.M)
table_text=table_text.replace('Pro Master','ProMaster').replace('on2030map','on 2030 map').replace('pickups;2500','pickups; 2500').replace('of2025','of 2025').replace('oflatest','of latest').replace('through2028','through 2028').replace('2026YTD','2026 YTD')
table_text=re.sub(r'\n{3,}','\n\n',table_text)
(P/'proposed-forecast-inputs.md').write_text(table_text+'\n')
print(json.dumps({'totals':tot,'bridge':bridge,'checks':{k:checks[k] for k in ['all_brand_reconcile','scenarios_ordered','q4_to_annual_exact','growth_bridge_exact']}},indent=2))
