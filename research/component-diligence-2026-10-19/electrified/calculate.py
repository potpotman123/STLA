"""Reproduce partial battery engineering comparisons. Never reads/writes a workbook."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "battery-benchmarks.json").read_text())
out = {"units": "constant2023USD per battery pack", "actual_Stellantis_prices": False,
       "A_2030_modeled_frontier_vs2026": [], "B_economic_hurdles": [],
       "C_2028_illustrative_timing_not_company_guidance": [],
       "D_delay_to_after2028": [], "NA_2028_verified_recurring_saving": None,
       "NA_2028_missing_inputs": ["eligible soldvehicle counts", "configurationmatch", "supplierinvoice capture", "incremental adoption vs baseline", "OEM implementationexpense", "EUR conversion and priceyear alignment"]}
for r in data["rows"]:
    e = r["energy_rated_kWh"]
    c26, c30 = e*r["usd_per_kWh_2026"], e*r["usd_per_kWh_2030"]
    saving = c26-c30
    out["A_2030_modeled_frontier_vs2026"].append({"id":r["id"], "pack2026_usd":round(c26,3), "pack2030_usd":round(c30,3), "annual_unit_saving_if_path_realized_usd":round(saving,3), "percent_of_pack":round(100*saving/c26,4),"full_vehicle_component_cost":None})
    # Timing assumption only: report supplies2026/2030 endpoints, not this2028 midpoint.
    mid = (c26+c30)/2
    out["C_2028_illustrative_timing_not_company_guidance"].append({"id":r["id"],"assumption":"half of2026-to2030 dollar improvement delivered by2028", "pack2028_usd":round(mid,3),"saving_per_pack_usd":round(c26-mid,3),"annual_saving_per10000_eligible_vehicles_usd":round((c26-mid)*10000,2),"actual_Stellantis_eligible_vehicles":None})
    out["B_economic_hurdles"].append({"id":r["id"],"meaning":"Undiscounted max incremental implementation budget for200000 lifetime eligible packs at full supplierprice capture, before any other downside", "assumed_lifetime_eligible_packs":200000,"investment_ceiling_at2030_unit_saving_usd":round(saving*200000,2),"actual_implementation_investment_usd":None,"validated_payback_years":None})
    out["D_delay_to_after2028"].append({"id":r["id"],"assumption":"2026 cost persists through2028; no incremental technical step in horizon", "2028_pack_cost_usd":round(c26,3),"2028_incremental_saving_usd":0})
byid={x["id"]:x for x in data["rows"]}
out["alternative_2026_chemistry_comparisons_not_additive"]=[]
for a,b in [("PHEV24_NMC","PHEV24_LFP"),("BEV90_NMC","BEV90_LFP"),("BEV105_NMC","BEV105_LFP")]:
    x,y=byid[a],byid[b]
    base=x["energy_rated_kWh"]*x["usd_per_kWh_2026"]
    alt=y["energy_rated_kWh"]*y["usd_per_kWh_2026"]
    out["alternative_2026_chemistry_comparisons_not_additive"].append({"from":a,"to":b,"saving_usd":round(base-alt,3),"percent":round(100*(base-alt)/base,4),"constraint":"Same modeled energy/power does not prove samevehicle mass,range,packaging,towing or coldperformance; requires vehicleintegration validation."})
assert all(x["annual_unit_saving_if_path_realized_usd"]>=0 for x in out["A_2030_modeled_frontier_vs2026"])
(ROOT / "calculated.json").write_text(json.dumps(out,indent=2)+"\n")
print("Wrote calculated.json; NA verified savings remain unknown, not zero.")
