from random import randint
# ANSI escape codes for bold text
bold = "\033[1m"
reset = "\033[0m"



bot_names = ["Elrick", "Mateo", "Edward", "River", "Kyle",  
             "Sean Combs", "Faustino", "Gallegos"]


def welcome():
    num = randint(0,7)
    name = (bot_names[num])
    print(f"{bold}***Welcome to Jollibee***{reset}")
    print(f"{bold}***My name is {name}***{reset}")
    print(f"{bold}***I will be here to help you order your delicious Jollibee meal***{reset}")
welcome()