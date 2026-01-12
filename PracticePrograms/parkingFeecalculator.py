# Program: Parking Fee Calculator

print("===== PARKING FEE CALCULATOR =====")

hours = float(input("enter parking duration in hourse:"))

if hours <= 1:
    fee = 20
elif hours <= 3:
    fee = 50
elif hours <= 6:
    fee = 100
else:
    fee = 150

print("parking Fee =", fee, "INR")































    