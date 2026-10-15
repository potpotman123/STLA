"""Read-only inspection: never saves, recalculates or exports the workbook."""
import hashlib,json
from pathlib import Path
import openpyxl
P=Path('/Users/kwu/Downloads/FINAL KW STLA MODEL.xlsx')
OUT=Path(__file__).resolve().parent
before=hashlib.sha256(P.read_bytes()).hexdigest()
f=openpyxl.load_workbook(P,read_only=True,data_only=False)
v=openpyxl.load_workbook(P,read_only=True,data_only=True)
specs={
 'NA AOI Bridge': ['D6:R10','D13:R16','D19:R32'],
 'NA Volume Build':['D67:R79'],
 'NA Volume Inputs':['G49:G75','A181:A182'],
 'NA RPU Build':['C255:E260','F283:R289'],
 'Model Assumptions':['G7:S20','H65:S67'],
 'VCP Build':['C51:O53','A60:A66'],
 'NA_AOI_Bridge':['A16:C25']}
snapshot={}
for sheet,ranges in specs.items():
    rows={}
    for ran in ranges:
        for row in f[sheet][ran]:
            for c in row:
                if c.value is not None:
                    rows[c.coordinate]={'formula_or_input':c.value,'cached_value':v[sheet][c.coordinate].value}
    snapshot[sheet]=rows
summary={}
for year,col in [('2026','H'),('2027','M'),('2028','R')]:
    summary[year]={k:v['NA AOI Bridge'][f'{col}{r}'].value for k,r in [('revenue_eurm',6),('shipments',8),('aoi_eurm',31),('margin',32)]}
ao=v['NA AOI Bridge']
calc={}
for col in ['F','G']:
    rebuilt=sum(ao[f'{col}{r}'].value for r in [13,15,16,21,26,28,29])
    assert abs(rebuilt-ao[f'{col}31'].value)<1e-7
    calc[col+'31_rebuilt']=rebuilt
assert abs(sum(ao[f'{c}31'].value for c in 'DEFG')-ao['H31'].value)<1e-7
assert abs(ao['R31'].value-ao['M31'].value-3212.0955)<1e-7
calc['2027_aoi_delta_eurm']=ao['M31'].value-ao['H31'].value
calc['annual_us_shipments_2027_cached']=v['NA RPU Build']['M285'].value
calc['annual_us_shipments_2027_sum_quarters']=sum(v['NA RPU Build'][f'{c}285'].value for c in 'IJKL')
calc['annual_us_shipments_2027_error']=calc['annual_us_shipments_2027_cached']-calc['annual_us_shipments_2027_sum_quarters']
calc['wagoneer_S_annual_revenue_overallocation_2028_eurm']=600*(61000-48000)/1e6
calc['wagoneer_S_annual_revenue_overallocation_2027_eurm']=calc['wagoneer_S_annual_revenue_overallocation_2028_eurm']*.98
calc['H2_2026_cached_aoi_eurm']=ao['F31'].value+ao['G31'].value
calc['H2_2026_shipments']=ao['F8'].value+ao['G8'].value
# Reference test, not a replacement forecast: freeze H1 unit economics and all non-volume conditions.
calc['H2_2026_sequential_constant_economics_test_eurm']=547+(calc['H2_2026_shipments']-824000)*.005
calc['anchor_method_gap_eurm']=calc['H2_2026_sequential_constant_economics_test_eurm']-calc['H2_2026_cached_aoi_eurm']
calc['2028_AOI_if_only_anchor_method_changed_eurm']=ao['R31'].value+calc['anchor_method_gap_eurm']
calc['2028_margin_if_only_anchor_method_changed']=calc['2028_AOI_if_only_anchor_method_changed_eurm']/ao['R6'].value
f.close();v.close()
assert hashlib.sha256(P.read_bytes()).hexdigest()==before
out={'source':str(P),'sha256':before,'read_only_verified':True,'cache_warning':'Cached workbook values inspected; selected equations independently rebuilt. No Excel recalculation or full formula-engine validation.', 'summary':summary,'checks_and_sensitivities':calc,'snapshot':snapshot}
(OUT/'inspection.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({k:out[k] for k in ['sha256','read_only_verified','summary','checks_and_sensitivities']},indent=2))
