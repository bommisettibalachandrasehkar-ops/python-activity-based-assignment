
# Multi-Currency Travel Budget Analysis

n = int(input("Enter number of expense categories: "))

budget = float(input("Enter total travel budget in INR: Rs. "))
fee_percent = float(input("Enter currency conversion fee (%): "))

total_expense = 0
largest_amount = 0
largest_category = ""

print("\n========== TRAVEL EXPENSES ==========")

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter category (Hotel/Food/Transport/Shopping): ")
    amount = float(input("Enter expense amount in foreign currency: "))
    rate = float(input("Enter exchange rate (INR per 1 foreign currency): "))

    # Convert foreign currency to INR
    converted_amount = amount * rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Total expense including fee
    final_amount = converted_amount + conversion_fee

    total_expense += final_amount

    print("\nCategory:", category)
    print("Foreign Amount:", round(amount, 2))
    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(conversion_fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))

    # Find largest expense category
    if final_amount > largest_amount:
        largest_amount = final_amount
        largest_category = category

# Compare budget
remaining = budget - total_expense

print("\n========== TRAVEL SUMMARY ==========")
print("Total Budget    : Rs.", round(budget, 2))
print("Total Expenses  : Rs.", round(total_expense, 2))

if remaining >= 0:
    print("Remaining Budget: Rs.", round(remaining, 2))
    print("Status: WITHIN BUDGET")
else:
    print("Budget Exceeded : Rs.", round(abs(remaining), 2))
    print("Status: OVER BUDGET")

print("Largest Expense :", largest_category)
print("Expense Amount  : Rs.", round(largest_amount, 2))
print("====================================")
