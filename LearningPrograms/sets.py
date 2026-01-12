# Sets in python

# Creating sets
num = {10, 20, 30}
mixed = {10, "python", 3.14}
empty = set()
dup = {1, 2, 2, 3}

print (num, mixed, empty, dup)

# Adding & removing
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grapes")        # safe
print(fruits)

item = fruits.pop()
print("popped:", item)

# Set operation
A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

# Relationship methods
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))

# update() and copy()
A.update (B)
print (A)
copyA = A.copy()
print (copyA)