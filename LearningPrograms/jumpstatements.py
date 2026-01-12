# Jump statement: break, continue, pass

print ("\n===== JUMP STATEMENTS =====")

# break example
for i in range (1 , 10):
    if i == 5:
        break
        print (i, end = "")

# Continue example
print ("\n")
for i in range (1 , 10):
    if i % 2 == 0:
        continue
        print (i, end = "")

# Pass example
print ("\n")
for ch in "Hi":
    if ch == "i":
        pass
    print (ch, end = "")

print ("\n\nbreak stops, continue skips, pass does nothing.\n")