# Constants for the range of valid inputs
LOW = 1
HIGH = 2

# Function to validate integer input within a specified range
def integer_validation(low, high, question):
    while True:  # Loop until valid input is provided
        try:
            # Prompt the user for input and convert it to an integer
            num = int(input(question))
            # Check if the input is within the valid range
            if num >= low and num <= high:
                return num  # Return the valid input
            else:
                # Inform the user if the input is out of range
                print(f"Please enter {LOW} or {HIGH}")   
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input, please enter the options between 1 or 2")
            print(f"Please enter {LOW} or {HIGH}")

# Function to handle the pickup or delivery selection
def pickup_delivery():
    # Display the main question to the user
    print("Would you like to Click and collect your order or do you want your order to be delivered?")
    # Define the question prompt
    question = f"Please enter {LOW} or {HIGH}: " 
    # Provide the user with options
    print("Enter 1 for Click and collect")
    print("Enter 2 for Delivery")
    # Call the integer validation function to get the user's choice
    del_pick = integer_validation(LOW, HIGH, question)

    if del_pick == 1:
        print("Click and collect") 
    elif del_pick == 2:
        print("Delivery")  

# Call the pickup_delivery function to execute the program
pickup_delivery()