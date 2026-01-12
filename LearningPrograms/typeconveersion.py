#python program : Type Conversion

#------------Implicity Type Conversion---------------
print("------Implicit Type Conversion------------")
numInt = 10             #integer value
numFloat = 3.5          #float value

#int is automatically converted to float during arithmetic operation
result = numInt + numFloat

print("value of result:" , result)
print("Type of result:" , type(result))         #result is float


#-------------Explicit Type Conversion-----------------
print("\n----------Explicit Type Conversion------------")

#float to int (decimal part is removed)
floatNum = 9.99
intNum = int(floatNum)
print("Float" , floatNum, "I after int():" , intNum)

#int to string
age = 21
ageStr = str(age)
print("Integer:" , age , "I After str():" , ageStr , "I Type:" , type(ageStr))

#atring to float
strNumber = "45.67"
floatNumber = float(strNumber)
print("string:" , strNumber, "I After float():" , floatNumber , "I Type:" , type(floatNumber))