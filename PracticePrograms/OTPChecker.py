# Program: Check OTP matches or not

print("===== OTP VERIFICATION =====")

correctotp = "5678"
attempt = ""

# Keep asking until matching OTP
while attempt != correctotp:
    attempt = input("Enter OTP:")

print("OTP verification successfully")
