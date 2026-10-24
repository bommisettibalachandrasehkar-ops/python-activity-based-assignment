
# Hospital Billing and Patient Classification

def calculate_bill(consultation, diagnostic, treatment, age):
    total = consultation + diagnostic + treatment

    # Apply concession
    if age >= 60:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession
    return total, concession, final_bill


# Input patient details
n = int(input("Enter number of patients: "))
patients = []

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    consultation = float(input("Consultation charges: "))
    diagnostic = float(input("Diagnostic charges: "))
    treatment = float(input("Treatment charges: "))
    payment = float(input("Amount paid: "))

    # Validate billing constraints
    if (age < 0 or consultation < 0 or
            diagnostic < 0 or treatment < 0 or payment < 0):
        print("Invalid input! Charges, age and payment cannot be negative.")
        continue

    total, concession, final_bill = calculate_bill(
        consultation, diagnostic, treatment, age
    )

    # Classify patient according to payment
    if payment >= final_bill:
        status = "Fully Paid"
    elif payment > 0:
        status = "Partially Paid"
    else:
        status = "Unpaid"

    balance = final_bill - payment

    patients.append([name, final_bill, payment, balance, status])

    # Display bill
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Amount Paid: Rs.", round(payment, 2))
    print("Balance: Rs.", round(balance, 2))
    print("Patient Classification:", status)

# Summary report
print("\n--- Hospital Summary ---")

for patient in patients:
    print("Name:", patient[0],
          "| Bill:", round(patient[1], 2),
          "| Paid:", round(patient[2], 2),
          "| Balance:", round(patient[3], 2),
          "| Status:", patient[4])
