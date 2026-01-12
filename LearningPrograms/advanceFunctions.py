#Type of Finctions & lambda

#Lambda functions
squar = lambda x: x * x
add = lambda a, b: a + b

print(squar(4))
print(add(5, 6))

#map()
nums = [1,2,3,4,5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

#filter()
evens = list(filter(lambda x : x % 2 == 0, nums))
print(evens)

#reduce()
from functools import reduce
total = reduce(lambda a, b : a + b, nums)
print(total)

#Combined example
scores = [45, 67, 89, 32]
bonus = list(map(lambda x : x + 5, scores))
passed = list(filter(lambda x : x >= 50, bonus))
final_total = reduce(lambda a, b : a + b, passed)

print(bonus)
print(passed)
print(final_total)