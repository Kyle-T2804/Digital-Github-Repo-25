import re
#Customer details dictionary
customer_details = {}

#regular phone expression pattern for phone validation
pattern = r"^\d{8,12}$"
#while loop for validation of name
while True:
    phone_number = input("Please enter your phone number: ")
    if re.match(pattern, phone_number):
        customer_details["phone"] = phone_number
        break
    else:
        print("This is an invalid phone number")
        

print(customer_details)