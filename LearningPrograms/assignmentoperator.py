#Assignment Operators in python

print("\n=====ASSIGNMENT OPERATORS IN PYTHON=====")

#Simple assignment
a = 10
print("Initial a =" , a)

#Arithmetic assignment operators
a += 5          #add and assign
a -= 3          #subtract and assign
a *= 2          #multiply and assign
a /= 4          #divide and assign
a %= 3          #modulus assign
print("After various arithmetic assignments , a =" , a)

#Floor division and exponent
a = 10
a //= 3
a **= 2
print("After floor division and exponent assignment , a =" , a)

#Bitwise assignment operators
a = 5
a &= 3
a  = 2
a ^= 1
a <<= 1
a >>= 2
print("Final value after bitwise assignment , a =" , a)

#User input example
x = int(input("\nEnter a number:"))
x += 10
x *= 2
x //= 2
print("Final x after assignment operators =" , x)

