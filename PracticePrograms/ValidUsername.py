# Program: Check if a username meets rules (length & no spaces)

print("===== VALID USERNAME =====")

username = input("enter username:")

if " " in username:
    print("Invalid: Username should not contain spaces.")
elif len(username) < 5:
    print("Invalid: username must be at least 5 characters.")
else:
    print("Username is valid.")