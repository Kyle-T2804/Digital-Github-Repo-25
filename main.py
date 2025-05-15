# Jollibee Bot
# Bot that takes customers orders for Jollibee
# Programmer: Kyle Tamani
# Known Bugs: None

# Import required libraries for data handling, validation, and colored output
import pandas as pd
import re
import random
import sys
from random import randint
from colorama import Fore, Style, Back, init

# List of bot names used by bot for a friendly greeting
bot_names = [
    "Elrick", "Mateo", "Edward", "River", "Kyle",
    "Sean Combs", "Faustino", "Gallegos"
]

# Jollibee menu items and their corresponding prices
menu_items = [
    "Chickenjoy", "Jolly Spaghetti", "Burger Steak", "Yumburger", "Jolly Hotdog", "Palabok Fiesta", "Jolly Crispy Fries", "Jolly Burger Steak",
    "Jolly Kiddie Meal", "Jolly Sundae", "Jolly Twirl", "Jolly Float", "Jolly Hot Choco", "Jolly Coffee", "Jolly Breakfast Joys", "Jolly Tuna Pie",
    "Jolly Shanghai Rolls", "Jolly Macaroni Soup", "Jolly Cheesy Classic", "Jolly Cheesy Bacon Mushroom", "Jolly Cheesy Deluxe", "Jolly Cheesy Bacon",
    "Jolly Cheesy Classic Hotdog", "Jolly Cheesy Bacon Hotdog", "Jolly Cheesy Spaghetti"
]
menu_prices = [
    5.99, 3.99, 4.99, 2.99, 3.49, 4.49, 1.99, 4.99, 3.49, 1.49, 1.29, 2.49, 1.99, 1.49, 3.99, 2.49, 2.99, 2.49, 3.49, 3.99, 3.79, 3.49, 3.99, 4.29, 3.99
]

# Lists to store ordered items and their prices for the current order
order_list = []
order_cost = []

# Dictionary to store customer details for the current order
customer_details = {}

# Constant variables for low and high numbers for menu options
LOW = 1
HIGH = 2

# Set autoreset to true so that coloured text automatically stops at end of print statement
init(autoreset=True)

# Function to validate integer input within a range
def integer_validation(low, high, question):
    """
    Validates that the user enters an integer within the specified range.
    Keeps prompting until valid input is received.
    """
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

# Function to validate alphabetic input (no numbers or special characters)
def validate_alpha(question):
    """
    Prompts the user for input and ensures it only contains alphabetic characters.
    Used for validating street and suburb names.
    """
    while True:
        response = input(question)
        # Remove all whitespace from the input
        no_blanks = re.sub(r"\s+", "", response)
        # Check if input is alphabetic
        if not no_blanks.isalpha():
            print("Input must only contain letters")
        else:
            return response

# Welcome message with random bot name
def welcome():
    """
    Prints a welcome message and introduces the bot with a random name.
    """
    name = random.choice(bot_names)
    print(Fore.YELLOW + Style.BRIGHT + "***Welcome to Jollibee***" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + f"***My name is {name}***" + Style.RESET_ALL)
    print(Fore.MAGENTA + "***I will be here to help you order your delicious Jollibee meal***" + Style.RESET_ALL)

# Function for pickup or delivery selection
def pickup_delivery():
    """
    Asks the user if they want click and collect or delivery.
    Collects the appropriate customer details.
    Returns 1 for click and collect, 2 for delivery.
    """
    print(Fore.GREEN + "Would you like to Click and collect your order or do you want your order to be delivered?" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 1 for Click and collect" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 2 for Delivery" + Style.RESET_ALL)
    question = f"{Fore.YELLOW}Please enter {LOW} or {HIGH}:{Style.RESET_ALL} "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        # Collect details for click and collect
        click_collect()
    elif del_pick == 2:
        # Collect details for delivery (includes address)
        click_collect()
        delivery_info()
    return del_pick

# Collect Click and Collect data (name and phone)
def click_collect():
    """
    Collects and validates the customer's name and phone number for click and collect or delivery.
    """
    pattern = r"^\d{8,12}$"
    # Name validation loop
    while True:
        name = input("Please enter your name: ")
        no_blanks = re.sub(r"\s+", "", name)
        if not no_blanks.isalpha():
            print("Input must only contain letters")
        else:
            customer_details["name"] = name.title()
            break
    # Phone number validation loop
    while True:
        phone = input("Please enter your phone number: ")
        no_blanks = re.sub(r"\s+", "", phone)
        if re.match(pattern, no_blanks):
            customer_details["phone"] = no_blanks
            break
        else:
            print("This is an invalid phone number.")

# Collect delivery data (address)
def delivery_info():
    """
    Collects and validates the customer's address for delivery orders.
    """
    # House/apartment number validation (cannot be blank)
    while True:
        house = input("Please enter your house or apartment number: ")
        if house == "":
            print("Cannot be left blank")
        else:
            customer_details["house"] = house.title()
            break
    # Street name validation
    street = validate_alpha("Please enter your street name: ")
    customer_details["street"] = street.title()
    # Suburb name validation
    suburb = validate_alpha("Please enter your suburb name: ")
    customer_details["suburb"] = suburb.title()

# Display Jollibee menu using pandas
def jollibee_menu():
    """
    Displays the Jollibee menu in a formatted table using pandas.
    """
    menu_dict = {}
    pd.options.display.float_format = '${:,.2f}'.format
    menu_dict['Number'] = list(range(1, 26))
    menu_dict['Item'] = menu_items
    menu_dict[""] = [""] * 25
    menu_dict['Price'] = menu_prices
    df = pd.DataFrame(menu_dict)
    blankIndex = [''] * len(df)
    df.index = blankIndex
    print()
    print(Fore.RED + Style.BRIGHT + "Jollibee Menu" + Style.RESET_ALL)
    print(df)
    print()

# Customer order process
def jollibee_order():
    """
    Handles the process of taking the customer's order.
    Allows the user to order between 1 and 5 menu items.
    """
    # Ask user how many items they want to order, must be between 1 and 5
    while True:
        try:
            num_items = int(input(Fore.YELLOW + "How many menu items do you want to order? " + Style.RESET_ALL))
            if 1 <= num_items <= 5:
                break
            else:
                print(Fore.RED + "Your order must be between 1 and 5" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "That is not a valid number" + Style.RESET_ALL)
    print(Fore.CYAN + f"{num_items}" + Style.RESET_ALL)
    print(Fore.GREEN + "Please choose menu items by number from the menu" + Style.RESET_ALL)
    # Loop for each item the user wants to order
    for item in range(num_items):
        while num_items > 0:
            # Validate menu item selection
            while True:
                try:
                    item_ordered = int(input(Fore.YELLOW + "Menu item number: " + Style.RESET_ALL))
                    if 1 <= item_ordered <= 25:
                        break
                    else:
                        print(Fore.RED + "Your menu choice must be between 1 and 25" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "That is not a valid number" + Style.RESET_ALL)
            item_ordered = item_ordered - 1  # Adjust for zero-based index
            # Add selected item and its price to order lists
            order_list.append(menu_items[item_ordered])
            order_cost.append(menu_prices[item_ordered])
            print(Fore.BLUE + "{} ${:.2f}".format(menu_items[item_ordered], menu_prices[item_ordered]) + Style.RESET_ALL)
            num_items = num_items - 1

# Calculate total cost and apply delivery charge if needed
def calculate_total(order_cost, del_pick):
    """
    Calculates the total cost of the order.
    Adds a $14 delivery charge if the order is for delivery and the total is $50 or less.
    Returns the final total and delivery charge.
    """
    total = sum(order_cost)
    delivery_charge = 0
    # Only add delivery charge if order is for delivery and total is $50 or less
    if del_pick == 2:  # 2 means delivery
        if total <= 50:
            delivery_charge = 14.00
            total += delivery_charge
    return total, delivery_charge

# Display customer order and summary
def print_order(del_pick):
    """
    Prints the customer's details and order summary.
    Shows different details depending on click and collect or delivery.
    Adds delivery charge if applicable.
    """
    print()
    print(Fore.GREEN + Style.BRIGHT + "Customer Details" + Style.RESET_ALL)
    if del_pick == 1:
        # Print details for click and collect
        print(Fore.CYAN + "Click and Collect" + Style.RESET_ALL)
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}")
    else:
        # Print details for delivery
        print(Fore.CYAN + "Delivery" + Style.RESET_ALL)
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print(Fore.GREEN + Style.BRIGHT + "Order Details" + Style.RESET_ALL)
    # Print each ordered item and its cost
    for count, item in enumerate(order_list):
        print(Style.BRIGHT + Fore.YELLOW + "Ordered: {} Cost  ${:.2f}".format(item, order_cost[count]) + Style.RESET_ALL)
    total_cost, delivery_charge = calculate_total(order_cost, del_pick)
    # Show delivery charge if applicable
    if del_pick == 2 and delivery_charge > 0:
        print(Style.BRIGHT + Fore.MAGENTA + f"Delivery Charge: ${delivery_charge:.2f} (Orders over $50 get free delivery)" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + "Total Cost: ${:.2f}".format(total_cost) + Style.RESET_ALL)
    print()

# Confirm or cancel order
def continue_cancel():
    """
    Asks the user to confirm or cancel their order.
    """
    print(Fore.YELLOW + "Do you want to continue with the order?" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 1 to continue" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 2 to cancel" + Style.RESET_ALL)
    question = f"{Fore.YELLOW}Please enter {LOW} or {HIGH}:{Style.RESET_ALL} "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print(Fore.GREEN + "Thank you for your order" + Style.RESET_ALL)
        print(Fore.GREEN + "Your order has been sent to the kitchen" + Style.RESET_ALL)
        print(Fore.GREEN + "You will receive a text when it is ready to pickup or for delivery" + Style.RESET_ALL)
    elif del_pick == 2:
        print(Fore.RED + "Your order has been cancelled" + Style.RESET_ALL)

# Exit program or start a new order
def new_exit():
    """
    Asks the user if they want to start a new order or exit the program.
    Clears the order lists if starting a new order.
    """
    print(Fore.YELLOW + "Do you want to continue with the order?" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 1 for new order" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter 2 for exit" + Style.RESET_ALL)
    question = f"{Fore.YELLOW}Please enter {LOW} or {HIGH}:{Style.RESET_ALL} "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print(Fore.GREEN + "New Order" + Style.RESET_ALL)
        # Clear previous order data for a fresh start
        order_list.clear()
        order_cost.clear()
        main()  # Restart the ordering process
    elif del_pick == 2:
        print(Fore.MAGENTA + "Thank you for using Jollibee BOT" + Style.RESET_ALL)
        exit()

def main():
    """
    Main function to run the Jollibee ordering bot.
    Calls all the main steps in order.
    """
    welcome()  # Show welcome message and bot name
    del_pick = pickup_delivery()  # Ask for pickup or delivery and collect details
    jollibee_menu()  # Show menu
    jollibee_order()  # Take the customer's order
    print_order(del_pick)  # Print order summary and total
    continue_cancel()  # Ask to confirm or cancel order
    new_exit()  # Ask to start new order or exit

# Start the program by calling main()
main()
# Print customer details at the end for reference/debugging
print(customer_details)