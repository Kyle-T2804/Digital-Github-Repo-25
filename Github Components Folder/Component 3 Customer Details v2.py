# Prompt the user for their details and store them in a dictionary
customer_details = {}

customer_details["name"] = input("Please enter your name: ")
customer_details["phone"] = input("Please enter your phone number: ")

# Display the collected customer details in a neat format
print("\nCustomer Details:")
print(f"Name: {customer_details['name']}")
print(f"Phone: {customer_details['phone']}")