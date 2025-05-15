import re

# Dictionary to store customer details
customer_details = {}

# Regular expression pattern for phone number validation (8 to 12 digits)
pattern = r"^\d{8,12}$"

# Prompt the user for their phone number and validate it
phone_number = input("Please enter your phone number: ")
if re.match(pattern, phone_number):
    customer_details["phone"] = phone_number
else:
    print("This is an invalid phone number.")

# Display the collected customer details
print("\nCustomer Details:")
print(customer_details)