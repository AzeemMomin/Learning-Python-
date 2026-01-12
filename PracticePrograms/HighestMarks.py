# Program: highest Marks

print("===== HIGHEST MARKS FINDER =====")

student = []    # empty list

count = int(input("How many student?"))

# Taking student name & marks
for i in range(count):
    name = input(f"Enter name of student {i + 1}:").title()
    marks = float(input(f"Enter marks of {name}:"))
    student.append((name, marks))

# Finding topper
top = max(student, key = lambda x: x[1])

print("\nTopper:", top[0], "-", top[1])