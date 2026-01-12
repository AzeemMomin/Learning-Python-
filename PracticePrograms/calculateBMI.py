#program : Body Mass Index (BMI) calculator

print("===== BODY MASS INDEX (BMI) CALCULATOR =====")

#Index
name = input ("Enter your name: ")
weight = float (input("Enter your weight in kilograms: "))
height = float (input("Enter your height in meters: "))

#Formula : BMI = weight / (height * height)
bmi = weight / (height ** 2)

print (f"\n {name} , your BMI is : {bmi}")