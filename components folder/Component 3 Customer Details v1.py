
order_type = input("Is your order for pickup or delivery? ").lower()

if order_type == "pickup":
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    print("Thanks", name, "we'll text you when your order is ready.")
elif order_type == "delivery":
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    print("Thanks", name)