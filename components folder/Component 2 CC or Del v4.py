low = 1
high = 2
num = 0

print("Would you like to Click and collect your order or want your order to be Delivered?")
print("Enter 1 for Click and collect")
print("Enter 2 for Delivery")
while True:
    try:
        num = int(input("Please enter 1 or 2: "))
        if num == low:
            print("Click and collect")
            break
        elif num == high:
            print("Delivery")
            break
        else: num = int(input("Invalid number, please enter 1 or 2: "))
    except ValueError:
        print("Invalid input, please enter the options between 1 or 2")

print("Continue")