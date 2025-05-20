# Constant variables for low and high numbers for menu options
LOW = 1
HIGH = 2

# Function to validate integer input within a range
def integer_validation(low, high, question):
    # Loop until correct input is received, then return input
    while True:
        try:
            num = int(input(question))
            if low <= num <= high:
                return num
            else:
                (f"Please enter {LOW} or {HIGH}")
        except ValueError:
            print("Invalid input, please enter the options between 1 or 2")
            print(f"Please enter {LOW} or {HIGH}")

def continue_cancel():
    print("Do you want to continue with the order?")
    print("Enter 1 to continue")
    print("Enter 2 to cancel")
    question = f"Please enter {LOW} or {HIGH}: "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("Thank you for your order")
        print("Your order has been sent to the kitchen")
        print("You will receive a text when it is ready to pickup or for delivery")
    elif del_pick == 2:
        print("Your order has been cancelled")

continue_cancel()