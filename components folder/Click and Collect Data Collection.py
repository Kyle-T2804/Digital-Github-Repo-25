# Importing the required libraries
import re                       

# Customer details dictionary
customer_details = {}
        
# Collect Click and collect data
def click_collect():
    #regular phone expression pattern for phone validation
    pattern = r"^\d{8,12}$"
    #while loop for valdation for name
    while True:
        name = input("Please enter your name: ")
        #removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", name)
        #checking if input is alphabetical
        x = no_blanks.isalpha()
        if x == False:
            # if not then print error message
            print("Input must only contain letters")
        else:
            #if alpha converts to title case and append to dictionary
            customer_details["name"] = name.title()
            break



    #while loop for validation of phone number
    while True:
        phone = input("Please enter your phone number: ")
        #removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", phone)
        if re.match(pattern, no_blanks):
            customer_details["phone"] = no_blanks
            break
        else:
            print("This is an invalid phone number.")


# Collect customer details
click_collect()

# Display the collected customer details
print("\nCustomer Details:")
print(f"Name: {customer_details['name']}")
print(f"Phone: {customer_details['phone']}")
