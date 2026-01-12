# Program: Email Cleaning & Categorization System

print("===== EMAIL CLEANING & CATEGORIZER =====")

emails = [
    "john@gmail.com", "RITA@yahoo.com", "alex@gmail.com",
    "tom@outlook.com", "sara@GMAIL.com"
]

cleanedEmails = []          # will store trimmed, lowercase emails
gmailUser = []              # will store only gmail users
other = []                  # any other domain

# Clean emails and categorize them
for mail in emails:
    clean = mail.strip().lower()    # remove spaces + convert lowercase
    cleanedEmails.append(clean)

    if clean.endswith("@gmail.com"):
        gmailUser.append(clean)
    else:
        other.append(clean)

print("\n All Cleaned Emails:", cleanedEmails)
print("Gmail user:", gmailUser)
print("other domains:", other)