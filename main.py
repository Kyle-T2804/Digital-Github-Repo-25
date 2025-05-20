# Jollibee Bot
# Bot that takes customers orders for Jollibee
# Programmer: Kyle Tamani
# Known Bugs: None

# --- Imports ---
import pandas as pd  # For displaying menu as a table
import re            # For input validation
import random        # For random bot name
import sys
from random import randint
from colorama import Fore, Style, Back, init  # For colored terminal output

# --- Bot Names ---
# List of bot names used for a friendly greeting
bot_names = [
    "Elrick", "Mateo", "Edward", "River", "Kyle",
    "Sean Combs", "Faustino", "Gallegos"
]

# --- Menu Data ---
# Jollibee menu items and their corresponding prices
menu_items = [
    "Chickenjoy", "Jolly Spaghetti", "Burger Steak", "Yumburger", "Jolly Hotdog", "Palabok Fiesta", "Jolly Crispy Fries", "Jolly Burger Steak",
    "Jolly Kiddie Meal", "Jolly Sundae", "Jolly Twirl", "Jolly Float", "Jolly Hot Choco", "Jolly Coffee", "Jolly Breakfast Joys", "Jolly Tuna Pie",
    "Jolly Shanghai Rolls", "Jolly Macaroni Soup", "Jolly Cheesy Classic", "Jolly Cheesy Bacon Mushroom", "Jolly Cheesy Deluxe", "Jolly Cheesy Bacon",
    "Jolly Cheesy Classic Hotdog", "Jolly Cheesy Bacon Hotdog", "Jolly Cheesy Spaghetti"
]
menu_prices = [
    17.99, 11.99, 15.99, 7.99, 9.49, 12.49, 4.99, 12.99, 9.49, 3.49, 3.29, 6.49, 3.99, 3.49, 9.99, 6.49, 6.99, 6.49, 9.49, 9.99, 9.79, 9.49, 9.99, 12.29, 9.99
]

# --- Order State ---
order_list = []      # Stores ordered items
order_cost = []      # Stores cost of each ordered item
customer_details = {}  # Stores customer info for the current order

# --- Constants ---
LOW = 1
HIGH = 2

# --- Colorama Setup ---
init(autoreset=True)  # Automatically reset color after each print

# --- Input Validation Functions ---

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
                (f"Please enter {LOW} or {HIGH}")
        except ValueError:
            print("Invalid input, please enter the options between 1 or 2")
            print(f"Please enter {LOW} or {HIGH}")

def validate_alpha(question):
    """
    Prompts the user for input and ensures it only contains alphabetic characters.
    Used for validating street and suburb names.
    """
    while True:
        response = input(question)
        no_blanks = re.sub(r"\s+", "", response)
        if not no_blanks.isalpha():
            print("Input must only contain letters")
        else:
            return response

# --- Main Bot Functions ---

def welcome():
    """
    Prints a welcome message and introduces the bot with a random name.
    """
    name = random.choice(bot_names)
    print(Fore.YELLOW + Style.BRIGHT + "***Welcome to Jollibee***" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + f"***My name is {name}***" + Style.RESET_ALL)
    print(Fore.MAGENTA + "***I will be here to help you order your delicious Jollibee meal***" + Style.RESET_ALL)

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
        click_collect()      # Collect name and phone for pickup
    elif del_pick == 2:
        click_collect()      # Collect name and phone for delivery
        delivery_info()      # Collect address for delivery
    return del_pick

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

def delivery_info():
    """
    Collects and validates the customer's address for delivery orders.
    """
    # House/apartment number validation (must be an integer and cannot be blank)
    while True:
        house = input("Please enter your house or apartment number: ")
        if house == "":
            print("Cannot be left blank")
        elif not house.isdigit():
            print("House or apartment number must be a number")
        else:
            customer_details["house"] = house
            break
    # Street and suburb validation
    street = validate_alpha("Please enter your street name: ")
    customer_details["street"] = street.title()
    suburb = validate_alpha("Please enter your suburb name: ")
    customer_details["suburb"] = suburb.title()

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

def jollibee_order():
    """
    Handles the process of taking the customer's order.
    Allows the user to order between 1 and 10 menu items.
    """
    # Ask user how many items they want to order, must be between 1 and 10
    while True:
        try:
            num_items = int(input(Fore.YELLOW + "How many menu items do you want to order? " + Style.RESET_ALL))
            if 1 <= num_items <= 10:
                break
            else:
                print(Fore.RED + "Your order must be between 1 and 10" + Style.RESET_ALL)
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
    if del_pick == 2:
        if delivery_charge > 0:
            print(Style.BRIGHT + Fore.MAGENTA + f"Delivery Charge: ${delivery_charge:.2f} (Orders over $50 get free delivery)" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.MAGENTA + "You get FREE delivery since your order is over $50!" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + "Total Cost: ${:.2f}".format(total_cost) + Style.RESET_ALL)
    print()

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
    welcome()              # Show welcome message and bot name
    del_pick = pickup_delivery()  # Ask for pickup or delivery and collect details
    jollibee_menu()        # Show menu
    jollibee_order()       # Take the customer's order
    print_order(del_pick)  # Print order summary and total
    continue_cancel()      # Ask to confirm or cancel order
    new_exit()             # Ask to start new order or exit

# --- Program Entry Point ---
main()
# Print customer details at the end for reference/debugging
print(customer_details)