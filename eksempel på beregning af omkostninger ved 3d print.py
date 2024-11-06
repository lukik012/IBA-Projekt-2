all_materials = [{"Process": "FDM", "Machine": "Ultimaker3", "Material": "ABS", "Cost": "66.66", "Unit": "$/kg", "Density": "1.1"},
    {"Process": "FDM", "Machine": "Fortus 350mc", "Material": "Ultem", "Cost": "343", "Unit": "unit", "Density": "1.27"},
    {"Process": "SLA", "Machine": "Form2", "Material": "Clear Resin", "Cost": "149", "Unit": "$/L", "Density": "1.18"},
    {"Process": "SLA", "Machine": "Form2", "Material": "Dental Model Resin", "Cost": "149", "Unit": "$/L", "Density": "1.18"},
    {"Process": "SLA", "Machine": "ProX 950", "Material": "Accura Xtreme", "Cost": "2800", "Unit": "$/10kg", "Density": "1.18"},
    {"Process": "SLA", "Machine": "Form2", "Material": "Casting Resin", "Cost": "299", "Unit": "$/L", "Density": "1.18"},
    {"Process": "SLS", "Machine": "EOSINT P800", "Material": "PA2200", "Cost": "67.5", "Unit": "$/kg", "Density": "0.93"},
    {"Process": "SLS", "Machine": "EOSINT P800", "Material": "PA12", "Cost": "60", "Unit": "$/kg", "Density": "1.01"},
    {"Process": "SLS", "Machine": "EOSINT P800", "Material": "Alumide", "Cost": "50", "Unit": "$/kg", "Density": "1.36"},
    {"Process": "SLM", "Machine": "EOSm100 or 400-4", "Material": "Ti6Al4V", "Cost": "400", "Unit": "$/kg", "Density": "4.43"},
    {"Process": "SLM", "Machine": "EOSm100 or 400-4", "Material": "SSL316", "Cost": "30", "Unit": "$/kg", "Density": "8"},
    {"Process": "DLP", "Machine": "3D Systems Figure 4", "Material": "Problack 10", "Cost": "250", "Unit": "$/kg", "Density": "1.07"}]

#beregning af pris
def calculate_price(process, machine, material, amount):
    for item in all_materials:
         if item["Process"] == process and item["Machine"] == machine and item["Material"] == material:
            cost_per_unit = float(item["Cost"])
            unit = item["Unit"]
            density = item.get("Density")
            if unit == "$/kg":
                total_cost = cost_per_unit * amount  
            elif unit == "$/L" and density:
                liters = amount / density 
                total_cost = cost_per_unit * liters
            elif unit == "unit":
                total_cost = cost_per_unit * amount  
            else:
                return "false unit or data"

            return f"The total cost for {amount} kg of {material} using {machine} is ${total_cost:.2f}" #2 decimaltal

    return "Material or machine not found"
#Eksempel
print(calculate_price("DLP", "3D Systems Figure 4", "Problack 10", 1))

    
