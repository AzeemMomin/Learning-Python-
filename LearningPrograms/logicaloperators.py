#Logical Operators in Python

print("\n=====LOGICAL OPERATORS PYTHON=====")

#Example values
a , b , c = 10 , 20 , 5
print("Using a =" , a ," ,b =" , b ," , c =", c , "\n")

#Logical AND
print("a > b and b > c ->" , (a > b) and (b > c))

#Logical OR
print("not(a > b) ->" , not(a>b))

#Logical NOT
print("(a > b) or (a < c and b > c) ->" , (a > b) or (a < c and b > c))

#Combined expression
print("(a > b) or (a < c and b > c) ->" , (a > b) or (a < c and b > c))

#Boolean value example
x , y = True , False
print("\nBoolean example:")
print("x and y ->" , x or y)
print("x or y ->" ,x or y)
print("not x ->" , not x)

#user input example
num = int(input("\nenter a number:"))

if num > 0 and num < 10:
     print("Number is between 1 and 9")
elif num <= 0 or num >= 10:
    print("Number is not in the range 1-9")

print("\nLogical operators: and / or / not\n")