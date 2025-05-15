# import pandas library
import pandas as pd

# create menu dictionary
menu_dict = {}

# format prices as currency
pd.options.display.float_format = '${:,.2f}'.format

# add item numbers
menu_dict['Number'] = list(range(1, 26))

# add Jollibee menu items
menu_dict['Item'] = [
    "Chickenjoy", "Jolly Spaghetti", "Burger Steak", "Yumburger", "Jolly Hotdog", "Palabok Fiesta", "Jolly Crispy Fries", "Jolly Burger Steak",
    "Jolly Kiddie Meal", "Jolly Sundae", "Jolly Twirl", "Jolly Float", "Jolly Hot Choco", "Jolly Coffee", "Jolly Breakfast Joys", "Jolly Tuna Pie",
    "Jolly Shanghai Rolls", "Jolly Macaroni Soup", "Jolly Cheesy Classic", "Jolly Cheesy Bacon Mushroom", "Jolly Cheesy Deluxe", "Jolly Cheesy Bacon",
    "Jolly Cheesy Classic Hotdog", "Jolly Cheesy Bacon Hotdog", "Jolly Cheesy Spaghetti"
]

# add blank line to dictionary for spacing (optional, can be removed if not needed)
menu_dict[""] = [""] * 25

# add menu prices
menu_dict['Price'] = [
    5.99, 3.99, 4.99, 2.99, 3.49, 4.49, 1.99, 4.99, 3.49, 1.49, 1.29, 2.49, 1.99, 1.49, 3.99, 2.49, 2.99, 2.49, 3.49, 3.99, 3.79, 3.49, 3.99, 4.29, 3.99
]

# display menu dataframe
df = pd.DataFrame(menu_dict)
blankIndex = [''] * len(df)
df.index = blankIndex

print("Jollibee Menu\n\n", df)