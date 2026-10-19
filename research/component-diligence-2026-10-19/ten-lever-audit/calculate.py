"""Transcribe user-provided Exhibit 1; filter contributions, not denominators."""
import json
from pathlib import Path

ranges = {1:(2.4,6.4),2:(2.3,6.1),3:(1.6,4.3),4:(0.7,1.9),5:(0.6,1.6),6:(0.5,1.4),7:(0.5,1.4),8:(0.3,0.8),9:(0.3,0.8),10:(0.2,0.6)}
sets = {'all_displayed_rows':list(ranges),'broadly_transferable':[2,5,7,8,9,10],'plus_conditional_system_integration':[2,4,5,7,8,9,10],'all_except_battery_sizing_and_technology':[2,4,5,6,7,8,9,10]}
out = {'source':'User-provided McKinsey Exhibit 1 screenshot, 19 October 2026','units':'percentage points of original EV material-cost denominator','warning':'Illustrative filtered EV benchmark, not an ICE estimate, expected value, or realized STLA savings. Printed total 9.5–25.3%; displayed low rows sum to 9.4%, consistent with rounding. Footnote 1 text is cropped in supplied image.','ranges':ranges,'subtotals':{}}
for name,ids in sets.items():
    low=round(sum(ranges[i][0] for i in ids),2)
    high=round(sum(ranges[i][1] for i in ids),2)
    out['subtotals'][name]={'included':ids,'low':low,'high':high,'arithmetic_midpoint':round((low+high)/2,3)}
Path(__file__).with_name('calculations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['subtotals'],indent=2))
