#Program to display product details and calculate total price

productName = input ("Enter the product name: ")
productprice = float (input("Enter the price of the product: "))
quantity = int(input("Enter the quantity you want to buy: "))

total_cost = productprice * quantity

print ("\nproduct summary: ")
print ("Product:" , productName)
print ("Price per unit:" , productprice)
print ("Quantity:" , quantity)
print("Total cost:" , total_cost)