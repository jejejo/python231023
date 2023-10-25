import re

# Regular expression pattern for matching email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#pattern = r'^[\w\.-]+@[\w\.-]+[a-zA-Z]+$

# List of sample email addresses
sample_emails = [
    "user@example.com",
    "john.doe123@email.co.uk",
    "alice.smith@subdomain.example.org",
    "info@my-website.com",
    "support@123-456.com",
    "user@localhost",
    "invalid_email@.com",
    "missingatdomain.com",
    "@missingusername.com",
    "user@inva@lid.com"
]

# Check if each email is valid
for email in sample_emails:
    if re.search(email_pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
