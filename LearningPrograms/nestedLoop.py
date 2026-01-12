# Nested Loops in Python

print ("\n===== NESTED LOOPS in Python =====")

# For_For nested loop
for i in range (1, 3):
    for j in range (1, 4):
        print (i, j, end = "")
    print ()

# Nested loop for 20 list
matrix = [[1 , 2] , [3 , 4]]
for row in matrix:
    for val in row:
        print (val , end="")
    print ()

# Generating combinations
colors = ["Red" , "Blue"]
sizes = ["S" , "M"]
for c in colors:
    for s in sizes:
        print (c , s)

print("\nInner loop runs fully for  each outer loop iteration.\n")



