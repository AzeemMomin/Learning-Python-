# Program: Temperature Converter

print("===== TEMPERATURE CONVERTER =====")

def c_to_f(c):
    return(c * 9/5) + 32

def f_to_c(f):
    return(f - 32) * 5/9

choice = input("Convert (C/F):").upper()

if choice == "C":
    C = float(input("Enter Celsius:"))
    print("fahrenheit:", c_to_f(C))

elif choice == "F":
    f = float(input("enter Fahrenheit:"))
    print("Celsius:", f_to_c(f))

else:
    print("Invalid option.")