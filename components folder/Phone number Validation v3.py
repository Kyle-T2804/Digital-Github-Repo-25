import re
#Customer details dictionary
customer_details = {}

#regular phone expression pattern for phone validation
pattern = r"^\d{8,12}$"
#while loop for validation of name

phone_number = input("Please enter your phone number: ")
if re.match(pattern, phone_number):
    customer_details["phone"] = phone_number
else:
    print("This is an invalid phone number")
    
#customer_details["phone"] = input("Please enter your phone number: ")

print(customer_details)