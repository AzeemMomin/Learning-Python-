#python program : Boolean (bool) Data Type

import sys

#Declaration
is_active = True
is_verified = False

#output
print("value of is_active:" , is_active)
print("value of is_verified:" , is_verified)

#Input
user_input = input("Enter True or False:")
user_bool = user_input == "True"
print("You entered:" , user_bool)

#Type checking
print("type of is_active:" , type(is_active))
print("Type of is _ verified:" , type(is_verified))

#Type casting
print("Boolean from int(0):" , bool(0))
print("Boolean from int(5):" , bool(-00000))
print("Boolean form empty string:" , bool(""))
print("boolean from 'Hello'p:" , bool ("Hello"))
print("Boolean from float(0.0):" , bool(0.0))
print("Boolean from float(3.14):" , bool(3.14))

#storage
print("Memory size of is_active:" , sys.getsizeof(is_active) , "bytes")
print("Memory size of is_verified:" , sys.getsizeof(is_verified) , "bytes")
