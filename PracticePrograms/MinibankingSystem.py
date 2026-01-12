# Program: Mini Banking System

print("===== MINI BANKING SYSTEM =====")

account = {
    "Jash": 5000,
    "Rohit": 3000,
    "Neha": 7000
}

def deposit(user, amount):
    account[user] += amount
    return f"{amount} added.New Balance = {account[user]}"

def withdraw(user, amount):
    if amount > account[user]:
        return "Insufficient balance."
    account[user] -= amount
    return f"withdraw {amount}.New Balance = {account[user]}"

def transfer (src, dst, amount):
    if amount > account[src]:
        return"Not enough balance to transfer."
    account[src] -= amount
    account [dst] += amount
    return f"Transferred {amount} to {dst}"

while True:
    print("\n1.Deposit\n2.withdraw\n3.transfer\n4. Exit")
    ch = int(input("choose:"))

    if ch == 4:
        break

    user = input("Enter username:").title()

    if user not in account:
        print("User not fount.")
        continue

    if ch == 1:
        amt = float(input("Amount:"))
        print(deposit(user, amt))

    elif ch == 2:
        amt = float(input("Amount:"))
        print(withdraw(user, amt))

    elif ch == 3:
        dst = input("Transfer to:").title()
        amt = float(input("Amount:"))
        print(transfer(user, dst, amt))


