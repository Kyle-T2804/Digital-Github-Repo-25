from random import randint  # Import randint to select a random bot name


# Constants for the range of valid inputs
LOW = 1
HIGH = 2


# ANSI escape codes for bold text formatting
bold = "\033[1m"
reset = "\033[0m"

# List of bot names to randomly choose from
bot_names = ["Elrick", "Mateo", "Edward", "River", "Kyle",  
             "Sean Combs", "Faustino", "Gallegos"]

# Function to display a welcome message with a random bot name
def welcome():
    num = randint(0, 7)  # Generate a random index
    name = bot_names[num]  # Select a bot name
    print(f"{bold}***Welcome to Jollibee***{reset}")
    print(f"{bold}***My name is {name}***{reset}")
    print(f"{bold}***I will be here to help you order your delicious Jollibee meal***{reset}")


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






# Calls both the welcome function and the pickup_delivery functions

def main():
    welcome()
    pickup_delivery()
    
main()