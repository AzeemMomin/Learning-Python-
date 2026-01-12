# Program: check if entered time is morning, afternoon, evening, or night

print("===== CURRENT TIME OF DAY =====")

hour = int(input("Enter hour (0-23):"))

if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 21:
    print("good Morning")
elif 17 <= hour < 21:
    print("Good morning")
else:
    print("Good Night!")