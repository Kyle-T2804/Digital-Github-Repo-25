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
                print(f"Please enter {LOW} or {HIGH}")
        except ValueError:
            print("Invalid input, please enter the options between 1 or 2")
            print(f"Please enter {LOW} or {HIGH}")

def new_exit():
    print("Do you want to continue with the order?")
    print("Enter 1 for new order")
    print("Enter 2 for exit")
    question = f"Please enter {LOW} or {HIGH}: "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("New Order")
    elif del_pick == 2:
        print("Exit")

new_exit()