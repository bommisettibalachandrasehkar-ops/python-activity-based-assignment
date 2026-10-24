
# Manufacturing Cost and Profitability Analysis

product_name = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost per unit: Rs. "))
labour_cost = float(input("Enter labour cost per unit: Rs. "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost: Rs. "))
selling_price = float(input("Enter selling price per unit: Rs. "))
profit_target = float(input("Enter target profit percentage: "))

# Calculate manufacturing costs
total_material = material_cost * quantity
wastage_cost = total_material * wastage_percent / 100
total_labour = labour_cost * quantity
total_machine = machine_cost

total_cost = total_material + wastage_cost + total_labour + total_machine
total_revenue = selling_price * quantity

profit = total_revenue - total_cost

if total_cost > 0:
    profit_percent = (profit / total_cost) * 100
else:
    profit_percent = 0

# Display report
print("\n====== MANUFACTURING REPORT ======")
print("Product Name       :", product_name)
print("Production Quantity:", quantity)
print("Material Cost     : Rs.", round(total_material, 2))
print("Wastage Cost      : Rs.", round(wastage_cost, 2))
print("Labour Cost       : Rs.", round(total_labour, 2))
print("Machine Cost      : Rs.", round(total_machine, 2))
print("----------------------------------")
print("Total Cost        : Rs.", round(total_cost, 2))
print("Total Revenue     : Rs.", round(total_revenue, 2))
print("Profit / Loss     : Rs.", round(profit, 2))
print("Profit Percentage :", round(profit_percent, 2), "%")

if profit >= 0:
    print("Status            : PROFIT")
else:
    print("Status            : LOSS")

if profit_percent >= profit_target:
    print("Target Status     : TARGET ACHIEVED")
else:
    print("Target Status     : TARGET NOT ACHIEVED")

print("==================================")
