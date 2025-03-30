import random
from random import randint

bot_names = ["Elrick", "Mateo", "Edward", "River", "Kyle",  "Sean Combs", "Faustino", "Gallegos"]

def welcome():
    num = randint(0,7)
    name = (bot_names[num])
    print("***Welcome to Jollibee ***")
    print("***My name is",name,"***")
    print("***I will be here to help you order your delicious Jollibee meal***")    