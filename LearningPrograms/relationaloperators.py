#Relational (Comparision) Operators in python

print("\n=====RELATIONAL OPERATORS IN PYTHON")

#Example value
a , b = 10 , 20
print("using a =" , a , "and b =" , b , "\n")

#Basic comparision
print("a == b -> " , a==b)      # equal to
print("a != b -> " , a!=b)      # not equal
print("a > b  -> " , a>b)       #greater than
print("a < b  -> " , a<b)       #less than
print("a >= b -> " , a>=b)      #greater than equal
print("a <= b -> " , a<=b)      #less or equal

#User comparision example
x = int(input ("\nEnter first number:"))
y = int(input ("Enter second number:"))

print(x , "==" , y , "->" , x == y)
print(x , "!=" , y , "->" , x != y)
print(x , ">"  , y , "->" , x > y)
print(x , "<"  , y , "->" , x < y)
print(x , "<=" , y , "->" , x == y)

# string compound demo
print("\nstring compound example")
print("'apple' == 'apple' ->" , "apple" == "apple")
print("'apple' <  'banana' ->" , "apple" == "banana")
print("'cat'   >   'bat'   ->" , "cat" == "bat")