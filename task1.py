
# University Scholarship Allocation

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Student name: ")
    marks = float(input("Aggregate marks: "))
    sub1 = float(input("Subject 1 marks: "))
    sub2 = float(input("Subject 2 marks: "))
    attendance = float(input("Attendance percentage: "))
    income = float(input("Family annual income: "))

    # Eligibility conditions
    if (marks >= 75 and sub1 >= 40 and sub2 >= 40
            and attendance >= 75 and income <= 200000):
        eligible = True
    else:
        eligible = False

    if eligible:
        students.append([name, marks, attendance, income])
        print(name, "is eligible")
    else:
        print(name, "is not eligible")

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students.")
else:
    for rank, student in enumerate(students, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])
        print("----------------------")
