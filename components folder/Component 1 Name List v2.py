from random import randint  # Import randint to select a random bot name

# ANSI escape codes for bold text formatting
bold = "\033[1m"
reset = "\033[0m"

# List of bot names to randomly choose from
bot_names = ["Elrick", "Mateo", "Edward", "River", "Kyle",  
             "Sean Combs", "Faustino", "Gallegos"]

# Function to display a welcome message with a random bot name
def welcome():
    num = randint(0, 7)  # Generate a random index
    name = bot_names[num]  # Select a bot name
    print(f"{bold}***Welcome to Jollibee***{reset}")
    print(f"{bold}***My name is {name}***{reset}")
    print(f"{bold}***I will be here to help you order your delicious Jollibee meal***{reset}")

# Call the welcome function to display the message
welcome()