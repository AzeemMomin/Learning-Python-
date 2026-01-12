# Program: Service Eligibility Checker

print("===== SERVICE ELIBILITY CHECKER =====")

age = int(input("enter your age:"))
citizen = input("Are you an Indian citizen? (yes/no):").lower()

if age >= 18 and citizen == "yes":
    print("you are eligible to apply.")
else:
    print("you are not eligible to apply.")
