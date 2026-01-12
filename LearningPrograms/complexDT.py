#python program : ComplexDataType
import sys

complexNumber = 3 + 4j
print("Complex Valu:" , complexNumber)
print("Type:" , type (complexNumber))
print("Size:" , sys.getsizeof(complexNumber) , "bytes")

complexFromInt = complex(5)
complexFromFloat = complex(2.5)
print("Complex from int:" , complexFromInt)
print("Complex from float:" , complexFromFloat)


