#Arithmetic Operators in python.

print("\n=====ARITHMETIC OPERATORS=====")

#Example values
a , b = 15 , 4
print("using a =" , a , "and b =" , b , "\n")

#Basic arithmetic operators
print("a + b =" , a + b)                #addition
print("a - b =" , a - b)                #subtraction
print("a * b =" , a * b)                #multiplication
print("a / b =" , a / b)                #division(float)
print("a // b =" , a // b)              #floor division
print("a % b =" , a % b)                #remainder
print("a ** b =" , a % b)               #exponent

#user input demonstration
num1 = int(input("\nEnter first number:"))
num2 = int(input("Enter second number:"))

print("Addition:" , num1 + num2)
print("Subtraction:" , num1 - num2)
print("Multiplication:" , num1 * num2)
print("Devision:" , num1 / num2)
print("Floor Devision:" , num1 // num2)
print("Modulus:" , num1 % num2)
print("Exponent:" , num1 ** num2)