#Python Keywords and Identifiers

import keyword   #module to check Python Keywords

#--------------- Keywords -------------
print("=== Keywords in python ===")
print("Some Keywords sre:", keyword.kwlist[:10])
print("Totle number of Keywoeds:",len(keyword.kwlist),"\n")

#--------------- IDENTIFIERS ----------------
print("=== Identifiers in python ===")

name="Alice"
age1=21
_student="John"
print("Valid identifiers_>",name,age1,_student)

city="Mumbai"
city="Delhi"
print("\ncity:",city)
print("city:",city)

print("\nCheck if a word is identifier or Keywords:")
words=["name","2abc","class","valu_1"]
for w in words:
    print(w,"_> isidentifier?",w.isidentifier(),"| iskeywords?",keyword.iskeyword(w))
