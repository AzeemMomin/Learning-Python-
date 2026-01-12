#=====MEMBERSHIP OPERATORA IN PYTHON=====

#Membership operators help check if a value exists inside sequences
#Operators : 'in' -> true if value does Not exist
#               'not in' -> True if value does Not exist

#---- String Example ----
text = "python programming"
print("'java' not in text:" , 'java' not in text)       #Checks character
print("'java' not in text:" , 'java' not in text)       #substring not found

#----- List Example -----
fruits = ["apple" , "banana" , "cherry"]
print("'banana' in fruits:" , 'banana' in fruits)       #element exists

#----- Tuple Example -----
nums = (10 , 20 , 30)
print("20 in nums:" , 20 in nums)       #tuple membership check

#-----Dictionary Example-----
student = {"name": "john" , "age" : 23}          #check keys only
print("'name' in student:" , 'name' in student)

#---- set Example -----
color = {"red" , "green" , "blue"}
print("'yellow' not in color" , 'yellow' not in color)          #Fast lookup

#-----User Input Example-----
word = input("Enter a word:")
if 'a' in word:
    print("The letter 'a' is  present.")
else:
    print("The letter 'a' is not present")

    print("\nUse 'in' or 'not in' to test membership in string , lists , tuples , sets , and dictionary")