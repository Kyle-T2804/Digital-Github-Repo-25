#import pandas library
import pandas as pd

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

def jollibee_menu():
    # Create menu dictionary
    menu_dict = {}
    # Format prices as currency
    pd.options.display.float_format = '${:,.2f}'.format
    # Add item numbers
    menu_dict['Number'] = list(range(1, 26))
    # Add menu items
    menu_dict['Item'] = menu_items
    # Add blank line to dictionary for spacing (optional)
    menu_dict[""] = [""] * 25
    # Add menu prices
    menu_dict['Price'] = menu_prices

    # Display menu dataframe
    df = pd.DataFrame(menu_dict)
    blankIndex = [''] * len(df)
    df.index = blankIndex

    print()
    print("Jollibee Menu\n\n", df)
    print()

jollibee_menu()

def jollibee_order():
    num_items = 0
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
    # Choose items from menu
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

    print(order_list)
    print(order_cost)

jollibee_order()