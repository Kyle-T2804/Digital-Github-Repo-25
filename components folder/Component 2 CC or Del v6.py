LOW = 1
HIGH = 2

def integer_validation(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                (f"Please enter {LOW} or {HIGH} ")   
        except ValueError:
            print("Invalid input, please enter the options between 1 or 2")
            (f"Please enter {LOW} or {HIGH}")
        
        



def pickup_delivery():
    print("Would you like to Click and collect your order or do you want your order to be delivered?")
    question = (f"Please enter {LOW} or {HIGH}: ") 
    print("Enter 1 for Click and collect")
    print("Enter 2 for Delivery")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("Click and collect")    
        
    elif del_pick == 2:
        print("Delivery")
        


pickup_delivery()