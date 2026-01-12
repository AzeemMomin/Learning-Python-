# Program: Loan eligibility Check

print("===== LOAN ELIGIBILITY =====")

salary = float(input("Enter your monthly salary:"))
cibil = int(input("Enter your CIBIL score:"))

if salary >= 30000 and cibil >= 700:
    print("Loan Approved")
else:
    print("Loan Rejected")

