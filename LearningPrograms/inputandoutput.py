#pyhton program : Input and Output

#-------------Basic print()-------------
print("Hello , World!")
print("Number:" , 10,20,30)     #multiple values
print()     #blank line

#------------print() with sep and end--------------
print("A" , "B" , "C" , sep="-")        #custom
print("Line without newline ->" ,end="")
print("Continues same line")

#--------------Basic input()-------------
name = input("\nEnter your name:")
print("Hi ," , name + "!")

#--------------Type casting--------------
age = int(input("Enter youe age:"))     #string -> float
height = float(input("Enter height in meters:"))        #string -> float
print("Age:" , age , "I Height:" , height)

#-----------Multiple input-----------
a , b = input("Enter two integers separated by space:").split()
a , b = int(a) , int(b)
print("Sum =" , a + b)

#------------Handling empty input-------------
color = input("Favorite color (press Enter to skip):").strip()
if color == "":
    color = "Not provided"
    print("color:" , color)

#-----------Formatted output----------
item , price , qty = "book" , 120.5,2
print(f"using f-string -> {item} , {price} , {qty} Total = {price * qty:.2f}")

#-----------Escape sequences-----------
print("Newline ->\\n\nTab     ->\\t\tExample\tTab")

