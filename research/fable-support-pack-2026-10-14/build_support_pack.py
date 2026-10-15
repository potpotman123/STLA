"""Consolidate existing research into CSV/JSON; never opens or edits Excel."""
import csv, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parents[1]
specs=[
 ('CURRENT_CASE','research/forecast-resolution-2026-10-14/proposal.json','research/forecast-resolution-2026-10-14/README.md','research/forecast-resolution-2026-10-14/calculate.py','Current proposed implementation; mixed reported/derived/assumed. Read inputs.source_types.'),
 ('VCP','research/vcp-schedule-2026-10-14/schedule.json','research/vcp-schedule-2026-10-14/README.md','research/vcp-schedule-2026-10-14/calculate.py','Estimated pools and transferred historical benchmarks; not STLA guidance.'),
 ('RPU_CALIBRATION','research/rpu-working-assumptions-2026-10-14.json','docs/RPU-WORKING-ASSUMPTIONS.md','research/build-rpu-working-case.py','Calibrated effective RPUs, not observed manufacturer revenue by model. Gross volumes superseded by CURRENT_CASE net volumes.'),
 ('VOLUME_EVIDENCE','research/forecast-audit-2026-10-14/proposed-forecast-inputs.json','research/forecast-audit-2026-10-14','', 'Gross model forecasts and evidence; apply CURRENT_CASE donor deductions once.')]
rows=[]; manifest=[]
def walk(obj,path):
 if isinstance(obj,dict):
  for k,v in obj.items(): yield from walk(v,path+[str(k)])
 elif isinstance(obj,list):
  for i,v in enumerate(obj): yield from walk(v,path+[str(i)])
 else: yield '.'.join(path),obj
for section,source,evidence,calc,status in specs:
 raw=(ROOT/source).read_bytes(); data=json.loads(raw)
 manifest.append(dict(section=section,source=source,sha256=hashlib.sha256(raw).hexdigest(),evidence=evidence,calculation=calc,status=status))
 for key,value in walk(data,[]):
  rows.append(dict(section=section,metric_path=key,value='' if value is None else value,value_type='null' if value is None else type(value).__name__,source_file=source,evidence_notes=evidence,calculation_file=calc,status=status))
with (P/'support-data.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
case=json.loads((ROOT/specs[0][1]).read_text())
model_rows=[]
for y,models in case['model_inputs'].items():
 ratio=.98 if y=='2027' else 1.0
 for r in models:
  model_rows.append(dict(year=y,**r,wholesale_sales_ratio=ratio,shipments=r['net_customer_sales']*ratio,revenue_eurm=r['net_customer_sales']*ratio*r['net_rpu_eur']/1e6))
with (P/'model-calculations.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(model_rows[0]));w.writeheader();w.writerows(model_rows)
for y in ('2027','2028'):
 selected=[r for r in model_rows if r['year']==y]
 assert abs(sum(r['net_customer_sales'] for r in selected)-case['annual'][y]['us_customer_sales'])<1e-6
 assert abs(sum(r['shipments'] for r in selected)+206000-case['annual'][y]['shipments'])<1e-6
 assert abs(sum(r['revenue_eurm'] for r in selected)+115000*38500/1e6+91000*30000/1e6-case['annual'][y]['revenue'])<1e-6
print(f'Wrote {len(rows)} support records, {len(model_rows)} model/year calculations; sales, shipment and revenue checks passed.')
