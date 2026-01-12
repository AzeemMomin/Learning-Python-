# Program: Password Validator

print("===== PASSWORD VALIDATION =====")

password = input("enter password:")

# Validation rules
hasDigit = any(ch.isdigit() for ch in password)
hasUpper = any(ch.isupper() for ch in password)
hasLower = any(ch.islower() for ch in password)
hasSpecial = any(ch in "!@#$%^&*()-_=+[]{};:/?,.<>" for ch in password)
hasLength = len(password) >= 8

# Check all conditions
if hasDigit and hasLength and hasLower and hasSpecial and hasUpper:
    print("password is strong and valid.")
else:
    print("Weak password.must include:")
    print("- At least 8 characters")
    print("- At least one digit")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one special character (!@#$ etc.)")
