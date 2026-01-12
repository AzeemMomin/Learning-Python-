#python program : floatDataType
import sys

floatNumber = 12.75
print("Float value:" , floatNumber)
print("Type:" , type (floatNumber))
print("Size:" , sys.getsizeof(floatNumber) , "bytes")
print("Max float value:" , sys.float_info.max)