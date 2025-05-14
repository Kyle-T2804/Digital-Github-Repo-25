# Dictionary to store customer details
customer_details = {}

# Loop to validate the customer's name input
while True:
    response = input("Please enter your name: ")
    # Check if the input contains only alphabetic characters
    if not response.isalpha():
        print("Input must only contain letters")
    else:
        # Convert valid input to title case and store in the dictionary
        customer_details["name"] = response.title()
        break

# Placeholder for additional customer details input (e.g., phone number)
# customer_details["phone"] = input("Please enter your phone number: ")

# Display the collected customer details
print("\nCustomer Details:")
print(f"Name: {customer_details['name']}")