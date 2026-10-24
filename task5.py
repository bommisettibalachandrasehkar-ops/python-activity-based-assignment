
# Multi-Plan Telecommunications Cost Optimization

usage_gb = float(input("Enter monthly data usage (GB): "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

plans = [
    ["Plan A", 199, 1, 28, 2],
    ["Plan B", 299, 2, 28, 5],
    ["Plan C", 399, 2, 56, 10],
    ["Plan D", 499, 3, 84, 15]
]

best_plan = None
lowest_cost = float("inf")

print("\n------ PLAN COMPARISON ------")

for plan in plans:
    name = plan[0]
    price = plan[1]
    daily_data = plan[2]
    validity = plan[3]
    extra_charge_per_gb = plan[4]

    total_data = daily_data * validity
    excess_data = max(0, usage_gb - total_data)
    excess_charge = excess_data * extra_charge_per_gb
    total_cost = price + excess_charge

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Total Data:", total_data, "GB")
    print("Excess Data:", excess_data, "GB")
    print("Excess Charges: Rs.", round(excess_charge, 2))
    print("Total Cost: Rs.", round(total_cost, 2))

    if validity >= validity_needed and total_cost <= budget:
        if best_plan is None or total_cost < lowest_cost:
            best_plan = name
            lowest_cost = total_cost

print("\n------ BEST PLAN ------")

if best_plan is not None:
    print("Most Economical Plan:", best_plan)
    print("Total Cost: Rs.", round(lowest_cost, 2))
else:
    print("No plan satisfies the given budget and validity.")
