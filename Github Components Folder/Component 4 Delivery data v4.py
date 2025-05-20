import re

# Dictionary to store customer details for delivery
customer_details = {}

def validate_alpha(question):
    """
    Prompt the user for input and ensure the response contains only alphabetic characters.
    Used for validating street and suburb names.
    """
    while True:
        response = input(question)
        # Remove all whitespace from the response
        no_blanks = re.sub(r"\s+", "", response)
        # Check if the input contains only letters
        if not no_blanks.isalpha():
            print("Input must only contain letters")
        else:
            # Return the original response (with spaces) if valid
            return response

def delivery_info():
    """
    Collects and validates customer delivery address details:
    - House/apartment number (must not be blank)
    - Street name (letters only)
    - Suburb name (letters only)
    """
    # Validate house/apartment number (must not be blank)
    while True:
        question = "Please enter your house or apartment number: "
        response = input(question)
        if response == "":
            print("Cannot be left blank")
        else:
            # Remove spaces (if any) and store the value
            no_blanks = re.sub(r"\s+", "", response)
            customer_details["house"] = response.title()
            break

    # Validate street name (letters only)
    question = "Please enter your street name: "
    response = validate_alpha(question)
    customer_details["street"] = response.title()   

    # Validate suburb name (letters only)
    question = "Please enter your suburb name: "
    response = validate_alpha(question)
    customer_details["suburb"] = response.title()

# Run the delivery info collection and print the results
delivery_info()
print(customer_details)