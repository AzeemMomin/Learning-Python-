# String in python
from ctypes import pythonapi

# Creating string
s1 = "python"
msg = """ Learning 
strings in pythonapi"""
print(s1)
print(msg)

# Indexing and slicing
print(s1 [0], s1 [-1])     # first & last char
print(s1[1:4], s1[:: -1])   # slice & reverse

# Useful methods
t = " Hello Python "
print(t.strip(), t.lower(), t.replace("python", "java"))

# Formatting
name, age = "John", 23
print (f"{name} is {age} years old")        # f-strin
print ("Name: {}, Age : {}".format(name, age))      # format