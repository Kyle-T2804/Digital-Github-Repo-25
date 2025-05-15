# List to store ordered Jollibee items
order_list = ['Chickenjoy', 'Jolly Spaghetti', 'Burger Steak', 'Jolly Hotdog']
# List to store item prices
order_cost = [5.99, 3.99, 4.99, 3.49]

# Display each ordered item with its cost
for count, item in enumerate(order_list):
    print("Ordered: {} Cost  ${:.2f}".format(item, order_cost[count]))