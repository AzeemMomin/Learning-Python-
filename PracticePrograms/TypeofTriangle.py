# Program: Triangle Type checker

print("===== TRIANGLE TYPE CHECKER =====")

a = float(input("side 1:"))
b = float(input("side2:"))
c = float(input("side3:"))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle.")