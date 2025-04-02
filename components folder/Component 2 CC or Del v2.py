
print("Would you like to Click and collect your order or want your order to be Delivered?")
print("Enter 1 for Click and collect")
print("Enter 2 for Delivery")
choice = int(input("Please enter 1 or 2: "))
if choice == 1:
    print("Click and collect")
elif choice == 2:
    print("Delivery")
else:
    print("Error invalid input!")