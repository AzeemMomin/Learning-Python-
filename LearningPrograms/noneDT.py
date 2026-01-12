#python program : None Data Type

import sys

#Declaration
emptyValue = None

#output
print("Value of emptyValue:" , emptyValue)

#Type Checking
print("Type of emptyValue:" , type(emptyValue))

#Comparision
if emptyValue is None:
    print("emptyValue has no value (it's None)")

#Input Example
userInput = input("Enter something (leave blank for None):")
if userInput == "":
    userValue = None
else:
    userValue = userInput
print("You entered:" , userValue , "I Type:" , type(userValue))

#Storage
print("Memory size of emptyValue:" , sys.getsizeof(emptyValue) , "bytes")