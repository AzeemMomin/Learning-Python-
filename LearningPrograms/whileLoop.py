# WHILE LOOP in PYTHON

print ("\n===== WHILE LOOP =====")

# Counting 1 to 5
i = 1
while i <= 5:
    print (i, end = "")
    i += 1

# Countdown
print ("\n")
x = 5
while x > 0:
    print (x, end = "")
    x -= 1

# Repeat until correct password
print ("\n")
pwd = ""
while pwd != "python" : pwd = input ("Enter password:")
# Sum of N natural numbers

print ()
n = int (input("Enter a number: "))
sum_n, j = 0, 1
while j <= n:
    sum_n += j
    j += 1
print ("sum:", sum_n)

print ("\nwhile loop repeats as long as the condition remains True.\n")
