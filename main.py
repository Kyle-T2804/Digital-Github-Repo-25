# Jollibee Bot
# Bot that takes customers orders for Jollibee
# Programmer: Kyle Tamani
# Known Bugs: None

import pandas as pd
import re
import random
import sys
from random import randint
from colorama import Fore, Style, init

# List of bot names used by bot
bot_names = [
    "Elrick", "Mateo", "Edward", "River", "Kyle",
    "Sean Combs", "Faustino", "Gallegos"
]

# Jollibee menu items and prices
menu_items = [
    "Chickenjoy", "Jolly Spaghetti", "Burger Steak", "Yumburger", "Jolly Hotdog", "Palabok Fiesta", "Jolly Crispy Fries", "Jolly Burger Steak",
    "Jolly Kiddie Meal", "Jolly Sundae", "Jolly Twirl", "Jolly Float", "Jolly Hot Choco", "Jolly Coffee", "Jolly Breakfast Joys", "Jolly Tuna Pie",
    "Jolly Shanghai Rolls", "Jolly Macaroni Soup", "Jolly Cheesy Classic", "Jolly Cheesy Bacon Mushroom", "Jolly Cheesy Deluxe", "Jolly Cheesy Bacon",
    "Jolly Cheesy Classic Hotdog", "Jolly Cheesy Bacon Hotdog", "Jolly Cheesy Spaghetti"
]
menu_prices = [
    5.99, 3.99, 4.99, 2.99, 3.49, 4.49, 1.99, 4.99, 3.49, 1.49, 1.29, 2.49, 1.99, 1.49, 3.99, 2.49, 2.99, 2.49, 3.49, 3.99, 3.79, 3.49, 3.99, 4.29, 3.99
]

# Lists to store ordered items and their prices
order_list = []
order_cost = []

# Customer details dictionary
customer_details = {}

# Constant variables for low and high numbers for menus
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
    """
    while True:
        response = input(question)
        no_blanks = re.sub(r"\s+", "", response)
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
    print("***Welcome to Jollibee***")
    print(f"***My name is {name}***")
    print("***I will be here to help you order your delicious Jollibee meal***")

# Function for pickup or delivery selection
def pickup_delivery():
    """
    Asks the user if they want click and collect or delivery.
    Collects the appropriate customer details.
    Returns 1 for click and collect, 2 for delivery.
    """
    print("Would you like to Click and collect your order or do you want your order to be delivered?")
    print("Enter 1 for Click and collect")
    print("Enter 2 for Delivery")
    question = f"Please enter {LOW} or {HIGH}: "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        click_collect()
    elif del_pick == 2:
        click_collect()
        delivery_info()
    return del_pick

# Collect Click and Collect data
def click_collect():
    """
    Collects and validates the customer's name and phone number for click and collect or delivery.
    """
    pattern = r"^\d{8,12}$"
    # Name validation
    while True:
        name = input("Please enter your name: ")
        no_blanks = re.sub(r"\s+", "", name)
        if not no_blanks.isalpha():
            print("Input must only contain letters")
        else:
            customer_details["name"] = name.title()
            break
    # Phone number validation
    while True:
        phone = input("Please enter your phone number: ")
        no_blanks = re.sub(r"\s+", "", phone)
        if re.match(pattern, no_blanks):
            customer_details["phone"] = no_blanks
            break
        else:
            print("This is an invalid phone number.")

# Collect delivery data
def delivery_info():
    """
    Collects and validates the customer's address for delivery orders.
    """
    while True:
        house = input("Please enter your house or apartment number: ")
        if house == "":
            print("Cannot be left blank")
        else:
            customer_details["house"] = house.title()
            break
    street = validate_alpha("Please enter your street name: ")
    customer_details["street"] = street.title()
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
    print("Jollibee Menu\n\n", df)
    print()

# Customer order process
def jollibee_order():
    """
    Handles the process of taking the customer's order.
    Allows the user to order between 1 and 5 menu items.
    """
    while True:
        try:
            num_items = int(input("How many menu items do you want to order? "))
            if 1 <= num_items <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print("That is not a valid number")
    print(num_items)
    print("Please choose menu items by number from the menu")
    for item in range(num_items):
        while num_items > 0:
            while True:
                try:
                    item_ordered = int(input())
                    if 1 <= item_ordered <= 25:
                        break
                    else:
                        print("Your menu choice must be between 1 and 25")
                except ValueError:
                    print("That is not a valid number")
            item_ordered = item_ordered - 1
            order_list.append(menu_items[item_ordered])
            order_cost.append(menu_prices[item_ordered])
            print("{} ${:.2f}".format(menu_items[item_ordered], menu_prices[item_ordered]))
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
    if del_pick == 2:  # 2 means delivery
        if total <= 50:
            delivery_charge = 14.00
            total += delivery_charge
    return total, delivery_charge

# Display customer order
def print_order(del_pick):
    """
    Prints the customer's details and order summary.
    Shows different details depending on click and collect or delivery.
    Adds delivery charge if applicable.
    """
    print()
    print(Fore.GREEN + "Customer Details")
    if del_pick == 1:
        print("Click and Collect")
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}")
    else:
        print("Delivery")
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print(Fore.GREEN + "Order Details")
    for count, item in enumerate(order_list):
        print(Style.BRIGHT + "Ordered: {} Cost  ${:.2f}".format(item, order_cost[count]))
    total_cost, delivery_charge = calculate_total(order_cost, del_pick)
    if del_pick == 2 and delivery_charge > 0:
        print(Style.BRIGHT + f"Delivery Charge: ${delivery_charge:.2f} (Orders over $50 get free delivery)")
    print(Style.BRIGHT + "Total Cost: ${:.2f}".format(total_cost))
    print()

# Confirm or cancel order
def continue_cancel():
    """
    Asks the user to confirm or cancel their order.
    """
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

# Exit program or start a new order
def new_exit():
    """
    Asks the user if they want to start a new order or exit the program.
    """
    print("Do you want to continue with the order?")
    print("Enter 1 for new order")
    print("Enter 2 for exit")
    question = f"Please enter {LOW} or {HIGH}: "
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("New Order")
        order_list.clear()
        order_cost.clear()
        main()
    elif del_pick == 2:
        print("Thank you for using Jollibee BOT")
        exit()

def main():
    """
    Main function to run the Jollibee ordering bot.
    """
    welcome()
    del_pick = pickup_delivery()
    jollibee_menu()
    jollibee_order()
    print_order(del_pick)
    continue_cancel()
    new_exit()

# Start the program
main()
print(customer_details)