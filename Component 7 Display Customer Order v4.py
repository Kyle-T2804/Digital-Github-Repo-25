from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# List to store ordered Jollibee items
order_list = ['Chickenjoy', 'Jolly Spaghetti', 'Burger Steak', 'Jolly Hotdog']
# List to store item prices
order_cost = [5.99, 3.99, 4.99, 3.49]
# Customer details
customer_details = {
    'name': 'Kyle',
    'phone': '01234567',
    'house': '1',
    'street': 'Sample Street',
    'suburb': 'Manurewa'
}

def print_order():
    print()
    # Print customer order
    print(Fore.GREEN + "Customer Details")
    print(f"Customer Name: {customer_details['name']}")
    print(f"Customer Phone: {customer_details['phone']}")
    print(f"Customer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print(Fore.GREEN + "Order Details")
    for count, item in enumerate(order_list):
        print(Style.BRIGHT + "Ordered: {} Cost  ${:.2f}".format(item, order_cost[count]))
    # Calculate the total cost of the order
    total_cost = sum(order_cost)
    print(Style.BRIGHT + "Total Cost: ${:.2f}".format(total_cost))
    print()

print_order()