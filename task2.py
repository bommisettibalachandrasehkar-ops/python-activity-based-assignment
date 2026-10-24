
# Progressive Electricity Billing System

def calculate_bill(units):
    bill = 0

    # Progressive consumption slabs
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5)
        bill = bill + (units - 300) * 7

    fixed_charge = 50
    surcharge = bill * 0.05
    total = bill + fixed_charge + surcharge

    # Rebate for low consumption
    if units <= 100:
        rebate = total * 0.10
    else:
        rebate = 0

    final_bill = total - rebate

    return bill, fixed_charge, surcharge, rebate, final_bill


# Compare bills across several months
n = int(input("Enter number of months: "))
monthly_bills = []

for i in range(n):
    print("\nMonth", i + 1)
    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    bill, fixed, surcharge, rebate, total = calculate_bill(units)

    monthly_bills.append([month, units, total])

    print("Energy Charge:", round(bill, 2))
    print("Fixed Charge:", fixed)
    print("Surcharge:", round(surcharge, 2))
    print("Rebate:", round(rebate, 2))
    print("Final Bill:", round(total, 2))

# Identify unusual increases
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print(monthly_bills[i][0],
          "- Units:", monthly_bills[i][1],
          "- Bill: Rs.", round(monthly_bills[i][2], 2))

    if i > 0:
        previous = monthly_bills[i - 1][2]
        current = monthly_bills[i][2]

        increase = current - previous

        if previous > 0 and increase / previous >= 0.30:
            print("WARNING: Unusual bill increase of",
                  round(increase, 2), "rupees!")
        elif increase > 0:
            print("Bill increased by Rs.", round(increase, 2))
        elif increase < 0:
            print("Bill decreased by Rs.", round(-increase, 2))
        else:
            print("Bill unchanged.")
