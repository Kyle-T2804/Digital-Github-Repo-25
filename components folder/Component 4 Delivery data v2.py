import re

#Customer details dictionary
customer_details = {}

#while loop for validation of street name
while True:
    question = "Please enter your street name: "
    response = input(question)
    #removes blank spaces from response
    no_blanks = re.sub(r"\s+", "", response)
    #checking if input is alphabetical
    x = no_blanks.isalpha()
    if x == False:
        # if not then print error message
        print("Input must only contain letters")
    else:
        #if alpha converts to title case and append to dictionary
        customer_details["street"] = response.title()
        break


#while loop for validation of suburb
while True:
    question = "Please enter your suburb name: "
    response = input(question)
    #removes blank spaces from response
    no_blanks = re.sub(r"\s+", "", response)
    #checking if input is alphabetical
    x = no_blanks.isalpha()
    if x == False:
        # if not then print error message
        print("Input must only contain letters")
    else:
        #if alpha converts to title case and append to dictionary
        customer_details["suburb"] = response.title()
        break


print(customer_details)