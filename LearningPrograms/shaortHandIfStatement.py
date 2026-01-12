# Short - hand IF / Conditional Expressions

print ("\n===== SHORT - HAND IF / TERNARY =====")

#Single - line IF
x = 10
if x > 5: print ("x > 5")

# Short - hand IF - ELSE (ternary)
a, b = 7, 12
max_val = a if a > b else b
print ("Max value:", max_val)

# Nested ternary
num = int (input("\nEnter a number: "))
result = "Positive" if num > 0 else "Negative"if num < 0 else "Zero"
print ("the number is:", result)

print ("\nShort - hand IF is best for Simple , single decision.\n")