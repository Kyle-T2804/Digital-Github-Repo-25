import re

#Customer details dictionary
customer_details = {}
#while loop for validation of house number
while True:
    question = "Please enter your house or apartment number: "
    response = input(question)
    if response == "":
        print("Cannot be left blank")
    else:
        #remove any spaces or blanks
        no_blanks = re.sub(r"\s+", "", response)  
        customer_details["house"] = response.title()
        break









print(customer_details)