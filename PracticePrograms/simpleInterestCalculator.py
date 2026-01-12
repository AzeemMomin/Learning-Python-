#Program : Simple Interest Calculator

print ("===== SIMPLE INTEREST CALCULATOR =====")

#Formula : SI = (P x R x T) /100
principal = float (input("Enter principal amount (₹): "))
rate = float (input("Enter Rate of Interest (%): "))
time = float (input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("\nprincipal Amount: ₹ , principal")
print ("Rate of Interest: " , rate , "%")
print ("Time:" , time , "years")
print ("Simple Interest:   " , simple_interest)
print ("Total Amount after interest: ₹ , principal + simple_interest")