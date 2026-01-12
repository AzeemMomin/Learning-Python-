#Program : Calculate Car Fuel Effiency (Mileage)

print ("===== CAR MILEAGE CALCULATOR =====")

#iNPUT FROM USER
distance = float (input(" total distance traveled (in km):" ))
fuel_used = float(input("Enter fuel used (in liters): "))

#Mileage Calculation
mileage = distance / fuel_used

print (f"\nYour car's milage is {mileage} km/litre.")