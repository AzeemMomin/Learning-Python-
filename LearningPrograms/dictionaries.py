# Distionaries in python

# Creating dictionaries
student = {"name": "Aditya", "age": 23, "course": "cs"}
person = dict(name = "sneha", age = 21)
empty = {}
school = {"s1": {"name": "Asha", "marks": 82}}

print(student, person, empty, school)

# Accessing values
print(student ["name"])
print(student.get ("course"))
print(student.get ("phone", "not provided"))

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# Adding 7 updating
student["phone"] = "98765"
student["age"] = 24
student.update({"city": "pune"})
student.setdefault("dept", "Engineering")
print(student)

# Removing elements
student.pop ("phone", None)
student.popitem()
if "city" in student:
    del student["city"]
print(student)

# Iterating
emp = {"id": 101, "name": "Rine", "role": "Engineer"}
for K in emp: print(K)
for V in emp .values(): print(V)
for k, V in emp.items(): print(K,V)

# Nested dictionary access
company = {"d1": {"manager": "Amit"}}
print(company["d1"]["manager"])

# Frequncy counter (short)
text = input ("Enter text:").split()
freq = {}
for w in text:
    freq[w] = freq.get (w, 0) + 1
print (freq)