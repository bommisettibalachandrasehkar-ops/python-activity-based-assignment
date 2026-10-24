
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0
total_discount = 0
max_concession = 500

print("\n========== PRODUCT DETAILS ==========")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    price = float(input("Enter price per unit: Rs. "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 0.05
    elif category == "clothing":
        tax_rate = 0.05
    elif category == "electronics":
        tax_rate = 0.18
    else:
        tax_rate = 0.10

    tax = amount * tax_rate

    # Threshold-based discount
    if amount >= 5000:
        discount_rate = 0.15
    elif amount >= 2000:
        discount_rate = 0.10
    elif amount >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = amount * discount_rate

    subtotal += amount
    total_tax += tax
    total_discount += discount

    print("\nProduct:", name)
    print("Quantity:", quantity)
    print("Amount: Rs.", round(amount, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Discount: Rs.", round(discount, 2))

# Apply maximum concession limit
if total_discount > max_concession:
    total_discount = max_concession

# Calculate final bill
final_bill = subtotal + total_tax - total_discount

print("\n========== ITEMIZED INVOICE ==========")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Total Discount : Rs.", round(total_discount, 2))
print("--------------------------------------")
print("Final Bill     : Rs.", round(final_bill, 2))
print("======================================")
