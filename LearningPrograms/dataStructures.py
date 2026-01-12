# Data Structures in python
from inspect import stack

print ("\n===== DATA STRUCTURES =====")

# Built - in examples
s = "Python"                        # String
l = [10, 20, 30]                    # List
t = (1, 2, 3)                       # Tuple
st = {10, 20, 20, 30}               # set (duplicates removed)
d = {"name": "John", "age": 23}     # Dictionary

print (s)
print (l)
print (t)
print (st)
print (d)

# User - define Data Structures: Stack (using class)
class Stack:
    def __int__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()

# Using the (stack
stk = Stack()
stk.push(100)
stk.push(200)
print ("\n stack pop:", stk.pop())     # Last in, first out
