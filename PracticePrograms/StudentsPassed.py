# Program: Court how many student scored 40 or more

print("===== STUDENT RESULT ANALYZER =====")

# List of student marks
score = [33, 78, 55, 12, 90, 41, 39, 60]

passed = 0      # counter

# Count marks >= 40
for s in scores:
    if s >= 40:
        passed += 1

print("total student passed:", passed)
