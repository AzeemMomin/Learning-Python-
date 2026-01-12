# Program: Login System with 3 attempts

print("===== LOGIN SYSTEM  =====")

password = "admin123"
attempts = 3

# User gets 3 tries
while attempts > 0:
    entered = input("enter password:")

    if entered == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Word password Attempts left:", attempts)

if attempts == 0:
    print("Account locked. Try again later.")