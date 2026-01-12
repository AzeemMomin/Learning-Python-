#python program : StringDataType
import sys

stringText = "Hello , python!"
print ("single - line string:" , stringText)

multilineString = """This is a multi-line string example
It can span multiple lines 
HI
BYe
                Aditya"""

print ("\nmulti - line string:" , multilineString)

userString = input("\nEnter a string:")
print("You entered:" , userString)

stringFromInt = str(123)
stringFromFloat = str(45>76)
print("\nString from int:" , stringFromInt)
print("string fron float:" , stringFromFloat)

print("\nSize of stringText:" , sys.getsizeof(stringText) , "bytes")
print("size of multiLinestring:" , sys.getsizeof(multilineString) , "bytes")