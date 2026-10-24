
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event expenses
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering_per_person = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate_per_person = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected number of participants: "))
contribution = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter available sponsorship amount: Rs. "))

# Calculate costs
fixed_cost = venue + equipment + transport
variable_cost = participants * (catering_per_person + certificate_per_person)
total_cost = fixed_cost + variable_cost

# Calculate income
registration_income = participants * contribution
total_income = registration_income + sponsorship

# Sponsorship shortfall
sponsorship_needed = max(0, total_cost - registration_income)
sponsorship_shortfall = max(0, sponsorship_needed - sponsorship)

# Break-even registration count
income_per_person = contribution
cost_per_person = catering_per_person + certificate_per_person
balance_per_person = income_per_person - cost_per_person

if balance_per_person > 0:
    break_even = (fixed_cost - sponsorship) / balance_per_person

    if break_even < 0:
        break_even = 0

    # Round up to the next whole participant
    break_even = int(break_even)
    if break_even * balance_per_person < fixed_cost - sponsorship:
        break_even += 1
elif fixed_cost <= sponsorship:
    break_even = 0
else:
    break_even = -1

# Display report
print("\n========== EVENT BUDGET REPORT ==========")
print("Venue Cost             : Rs.", round(venue, 2))
print("Equipment Cost         : Rs.", round(equipment, 2))
print("Transport Cost         : Rs.", round(transport, 2))
print("Catering Cost          : Rs.", round(participants * catering_per_person, 2))
print("Certificate Cost       : Rs.", round(participants * certificate_per_person, 2))
print("-----------------------------------------")
print("Total Event Cost       : Rs.", round(total_cost, 2))
print("Registration Income    : Rs.", round(registration_income, 2))
print("Sponsorship Received   : Rs.", round(sponsorship, 2))
print("Total Income           : Rs.", round(total_income, 2))
print("Sponsorship Required   : Rs.", round(sponsorship_needed, 2))
print("Sponsorship Shortfall  : Rs.", round(sponsorship_shortfall, 2))

if total_income >= total_cost:
    print("Financial Status       : BUDGET BALANCED")
else:
    print("Financial Status       : DEFICIT")

if break_even == -1:
    print("Break-even Participants: Not possible at this fee")
else:
    print("Break-even Participants:", break_even)

print("=========================================")
