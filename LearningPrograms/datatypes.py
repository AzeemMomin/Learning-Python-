#python program : DataTypes
import sys

#Basic Data Types
integerVar = 10
floatVar = 3.14
complexVar = 2+5j
stringVar = "Hello Python"
boolVar = True
noneVar = None
listVar = [1,2,3]
tupleVar = (1,2,3)
setVar = {1,2,3}
dictVar = {"one" : 1 , "two" : 2}

print("Integer:" , type (integerVar))
print("Float:" , type (floatVar))
print("Complex:" , type (complexVar))
print("String:" , type (stringVar))
print("Boolearn:" , type (boolVar))
print("None:" , type (noneVar))
print("Tuple:" , type (tupleVar))
print("Set:" , type (setVar))
print("Dictionary:" , type (dictVar))

#Storage Information
print ("\n-----Data type Sizes-----")
print("Boolean:" , sys.getsizeof (boolVar) , "bytes")
print("Integer:" , sys.getsizeof (integerVar) , "bytes")
print("Float:" , sys.getsizeof (floatVar) , "bytes")
print("Complex:" , sys.getsizeof (complexVar) , "bytes")
print("string:" , sys.getsizeof (stringVar) , "bytes")
print("None:" , sys.getsizeof (noneVar) , "bytes")



