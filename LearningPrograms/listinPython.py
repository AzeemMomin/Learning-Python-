# List in python

# Creating list
nums = [10, 20, 30]
mixed = [10, "python", 3.14]
nested = [[1,2], [3,4]]

print(nums)
print(mixed)
print(nested)

# Indexing & slicing
print(nums[0], nums[-1])
print(nums[1:3], nums[::-1])

# List methods
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "grapes")
fruits.remove("banana")
print(fruits)

# Iterating
for f in fruits:
    print(f)

# Nested list access
matrix = [[1,2] , [3,4]]
print(matrix [1] [0])
