#python program : IntegerDataType
import sys

integerNumber = 100
print ("Integer value:" , integerNumber)
print ("Type:" , type (integerNumber))
print("Size:" , sys . getsizeof(integerNumber) , "bytes")

bigInteger = 10**100
print ("Type:",bigInteger, type(bigInteger), sys.getsizeof(bigInteger) , "bytes")