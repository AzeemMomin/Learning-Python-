# IF-ELIF-ELSE Ladder in python

print ("\n===== IF-ELIF-ELSE LADDER =====")

# Grading example
marks = int(input("Enter marks: "))

if marks >= 90:
    print ("Grade A+")
elif marks >= 75:
    print ("Grade A")
elif marks >= 60:
    print ("Grade B")
elif marks >= 40:
    print ("Grade C")
else:
    print ("Fail")

# Temperature example
temp = float (input("\nEnter temperature: "))

if temp > 35:
    print ("Too hot")
elif temp > 25:
    print ("Warm")
elif temp > 15:
    print ("Pleasant")
elif temp > 5:
    print ("Cold")
else:
    print ("Freezing")

    print ("\nOnly one block runs based on the first true condition.\n")
