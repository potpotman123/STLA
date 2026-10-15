"""Transparent benchmark-transfer scenario; EUR millions, frozen 2025 cost pools."""
import json
from pathlib import Path
root=Path(__file__).parent
rows=[
 ('components',35000,.09,'Nissan FY2001 purchasing result transferred to STLA components'),
 ('manufacturing_cash',7000,.083,'Nissan 180 three-year result transferred to cash plant/labor'),
 ('logistics',1500,.17,'4flow selected inbound project extended to logistics pool'),
 ('other_indirect',1000,None,'Unestimated; zero credited, not zero expected'),
 ('warranty',3000,None,'Unestimated; zero credited, not zero expected')]
# 2026: assumed equivalent of one quarter at 2027's average annual rate.
# 2027: management group 2.4/6 shape transferred to each NA driver.
# 2028: full-year delivery assumption, not implied solely by exit-run-rate guidance.
factors={'2026':.10,'2027':.40,'2028':1.0}
out={'status':'AI-proposed conditional benchmark-transfer case, not user-approved or independently underwritten base case','baseline':'Frozen estimated 2025 NA cost pools and comparable output/content; no automatic volume scaling','factors':factors,'drivers':[]}
for key,pool,rate,rationale in rows:
 terminal=pool*rate if rate is not None else 0
 annual={y:round(terminal*f,6) for y,f in factors.items()}
 out['drivers'].append(dict(driver=key,pool_eurm=pool,terminal_rate=rate,terminal_credited_savings_eurm=terminal,rationale=rationale,annual_recognized_savings_eurm=annual,quarterly_recognized_savings_eurm={y:v/4 for y,v in annual.items()}))
tot={y:round(sum(r['annual_recognized_savings_eurm'][y] for r in out['drivers']),6) for y in factors}
out['annual_total_eurm']=tot
out['annual_yoy_aoi_increment_eurm']={'2027':round(tot['2027']-tot['2026'],6),'2028':round(tot['2028']-tot['2027'],6)}
out['quarterly_yoy_aoi_increment_eurm']={y:v/4 for y,v in out['annual_yoy_aoi_increment_eurm'].items()}
out['two_year_cumulative_recognized_2027_2028_eurm']=tot['2027']+tot['2028']
terminal=tot['2028']
out['timing_sensitivity']={'2026_credit_zero_yoy2027_eurm':tot['2027'],'2026_credit_20pct_yoy2027_eurm':tot['2027']-terminal*.2,'2028_recognition_70pct_eurm':terminal*.7,'2028_recognition_70pct_yoy_eurm':terminal*.7-tot['2027']}
assert abs(terminal-3986)<1e-8
assert abs(tot['2026']+sum(out['annual_yoy_aoi_increment_eurm'].values())-terminal)<1e-8
assert all(abs(sum(r['quarterly_recognized_savings_eurm'][y]*4 for r in out['drivers'])-tot[y])<1e-6 for y in factors)
(root/'schedule.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['annual_total_eurm','annual_yoy_aoi_increment_eurm','quarterly_yoy_aoi_increment_eurm','timing_sensitivity']},indent=2))
