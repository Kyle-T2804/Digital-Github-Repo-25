#Customer details dictionary
customer_details = {}


#while loop for validation of name

while True:
    question = "Please enter your name: "
    response = input(question)
    #checking if input is alphabetical
    x = response.isalpha()
    if x == False:
        # if not then print error message
        print("Input must only contain letters")
    else:
        #if alpha converts to title case and append to dictionary
        customer_details["name"] = response.title()
        break


#ask user for input

#customer_details["phone"] = input("Please enter your phone number: ")

print(customer_details)