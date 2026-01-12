# Program: Inventory Management System

print("===== INVENTORY MANAGEMENT =====")

inventory = {
    "shoes": 10,
    "Jeans": 5,
    "T-shirts": 20,
    "Caps": 2
}

print("Current stock:\n", inventory)

item = input("\nEnter item to purchase:").title()
quantity = int(input("emter quantity needed:"))

# Check stock availability
if item in inventory:
    if quantity <= inventory[item]:
        inventory[item] -= quantity
        print("\nOrder Confirmed!")
        print("Remaining Stock:", inventory[item])
    else:
        print("\nOnly", inventory[item], "pcs available.Cannot fulfill order.")
else:
    print("\nItem not found in inventory.")