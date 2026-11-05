
# Student Scholarship Eligibility System

print("======================================")
print("   STUDENT SCHOLARSHIP ELIGIBILITY")
print("======================================")

# Taking student information
name = input("Enter Student Name: ")

marks = float(input("Enter Academic Marks (%): "))
attendance = float(input("Enter Attendance Percentage (%): "))
income = float(input("Enter Monthly Family Income (Rs.): "))

# Validating information
if marks < 0 or marks > 100:
    print("Invalid Marks! Marks must be between 0 and 100.")

elif attendance < 0 or attendance > 100:
    print("Invalid Attendance! Attendance must be between 0 and 100.")

elif income < 0:
    print("Invalid Income! Income cannot be negative.")

else:
    print("\n========== SCHOLARSHIP REPORT ==========")

    print("Student Name:", name)
    print("Academic Marks:", marks, "%")
    print("Attendance:", attendance, "%")
    print("Monthly Family Income: Rs.", income)

    # Checking scholarship eligibility
    if marks >= 80 and attendance >= 85 and income <= 50000:

        print("\nEligibility Status: Eligible")

        if marks >= 90:
            print("Scholarship Type: Full Scholarship")

        elif marks >= 80:
            print("Scholarship Type: Partial Scholarship")

    else:
        print("\nEligibility Status: Not Eligible")
        print("Reason for Ineligibility:")

        if marks < 80:
            print("- Academic marks are below 80%.")

        if attendance < 85:
            print("- Attendance is below 85%.")

        if income > 50000:
            print("- Monthly family income is above Rs. 50,000.")

    print("======================================")
    print("       Evaluation Completed")
    print("======================================")
