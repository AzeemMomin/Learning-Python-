#operators in python

print("\n=====OPERATORS IN PYTHON=====")
print("operators perform action on values. Example : +, -, *, ==, and, or , etc.\n")

#list of operators categories
print("Type of operators")
print("1.Arithmatic               -> + - * / % // **")
print("2.Relation                 -> == ! = > < >= <=")
print("3.Assignment               -> = += -= *= /= %= //= **=")

print("4.Logical                  -> and or not")
print("5.Bitwise                  -> & | ^ ~ << >>")
print("6.Membership               -> in not in")
print("7.Identity                 -> is is not")

#Example variables
a , b = 10 , 5
x, y = True , False
text = "python"

print("\nExample variables:")
print("a =" , a , " , b=" , b)
print("x=" , x , " , y=" , y)
print("text =" , text)

#small demonstration
print("\nQuick example:")
print("a>b =" , a+b)        #arithmetic
print("a>b =" , a>b)        #comparison
print("x and y=" ,x and y)  #logical
print("'p' in text =" , 'p' in text)    #membership
print("a is b =", a is b)