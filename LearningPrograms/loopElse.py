# Loops Else in Python

print ("\n===== LOOPS ELSE =====")

# for loop search example
nums = [2, 4, 6, 8]
for n in nums:
    if n == 5:
        print ("Found 5")
        break
else:
    print ("5 not found in list")

# While loop example
print ()
x = 3
while x > 0:
    print (x, end = "")
    x -= 1
else:
    print ("\nCountdown finished")

users = ["Harry", "Ayan", "Azeem"]
target = "Harry"

for user in users:
    if user == target:
        print ("user found")
        break
else:
    print ("User not found")

print ("\nElse rune only when loop completes without break,\n")