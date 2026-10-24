
# Employee Payroll and Deduction Analysis

emp_name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Calculate salary components
overtime_pay = overtime_hours * overtime_rate
gross_salary = basic + allowances + overtime_pay + incentives

# Calculate progressive deductions
if gross_salary <= 20000:
    deduction = gross_salary * 0.05
elif gross_salary <= 40000:
    deduction = 20000 * 0.05 + (gross_salary - 20000) * 0.10
else:
    deduction = (20000 * 0.05) + (20000 * 0.10) + (gross_salary - 40000) * 0.15

# Calculate net salary
net_salary = gross_salary - deduction

# Print salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name :", emp_name)
print("Employee ID   :", emp_id)
print("--------------------------------------")
print(f"Basic Pay     : Rs. {basic:.2f}")
print(f"Allowances    : Rs. {allowances:.2f}")
print(f"Overtime Pay  : Rs. {overtime_pay:.2f}")
print(f"Incentives    : Rs. {incentives:.2f}")
print("--------------------------------------")
print(f"Gross Salary  : Rs. {gross_salary:.2f}")
print(f"Deduction     : Rs. {deduction:.2f}")
print(f"Net Salary    : Rs. {net_salary:.2f}")
print("======================================")
