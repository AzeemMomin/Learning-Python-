#Control Flow in Python

print("control flow change the order in which code executes.\n")

#Types of control flow
print ("1 . conditional statements -> if , elif , else")
print ("2 . Looping statement -> for , while")
print ("3 . jump Statement -> break , continue , pass\n")

#Example values
temperature = 30
count = 3
weather = "sunny"

#Conditional example
if weather == "sunny":
    print ("Bright day:")
elif weather == "rainy":
    print ("Carry umbrella.")
else :
    print ("stay warm.")

#Looping examples
print ("\nnumber 1 to 5:")
for i in range (1 , 6):
    print (i , end = "")

    print("\nCondown")
while count > 0:
    print (count , end = "")
    count -= 1

#jump statement
print ("\n\nJump statement demo:")
for i in range (1 , 6):
    if i == 2:
        continue
    if i == 4:
        break
    print ("Number:" , i)

#Pass example
for j in range(3):
    pass

print ("\nControl flow helps python make decisions and repeat tasktasks.\n")