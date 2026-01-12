# Nested IF-ELSE in python

print ("\n===== NESTED IF-STATEMENT =====")

# Grading example
marks = int(input("Enter marks: "))

if marks >= 40:
    print ("pass")
    if marks >= 90:
        print ("Grade A+")
    elif marks >= 75:
        print ("Grade A")
    elif marks >= 60:
        print ("Grade B")
    else:
        print ("Grade C")
else:
    print ("Fail")

# Temperature example
temp = float (input("\nEnter temperature: "))

if temp >= 0:
    print ("Above freezing")
    if temp > 35:
        print ("Very hot")
    else:
        print ("Normal")
else:
    print ("Freezing")

print ("\nNested IF checks inner conditions only if the outer condition is True.\n")