#Conditinoal Statement in Python - If

print ("\n===== IF STATEMENT IN PYTHON ======")

#Example 1: basic If
age = int(input("Enter your age:"))
if age >= 18:
    print ("Eligible to vote.")

#Example 2 : temperature check
tem = float (input("\nEnter temperature:"))
if tem > 30:
    print ("It's not today.")

#Example 3 : boolean condition
is_student = True
if is_student:
    print("\nstudent discount available.")

#Example 4 : independent Ifs
marks = int(input("\nEnter marks:"))
if marks >= 90: print ("Grade A+")
if marks >= 75: print ("Grade A")
if marks >= 60: print ("Grade B")
if marks >= 40: print ("Grade C")
if marks <  40: print ("Fail")

#Example 5: even/odd
num = int(input("\nEnter a number:"))
if num % 2 == 0 : print ("Even number")
if num % 2 != 0 : print ("odd number")

print ("\nIf executes only when Condition is True.\n")

















