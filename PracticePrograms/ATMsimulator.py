# Program: ATM withdrawl Simulator

print("===== ATM WITHDRAWAL AIMULATOR =====")

balance = 5000

# Loop unit user enter valid amount
while True:
    amt = int(input("Enter amount to withdraw:"))

    if amt <= 0:
        print("Invalid amount.Try again.")
    elif amt > balance:
        print("Insufficient balance.")
    else:
        balance -= amt
        print("withdrawal auccessful.Remaining balance:", balance)
        break