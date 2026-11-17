
import random

fortune = ["You will get cucked",
           "You will die",
           "You're safe... for now...",
           "You will find victory in your life",
           "The reason why you still live lies on what's ahead"]



choice = input('Hello! Would you like to snap open your fortune cookie (Y/N)? ')
while True:
    if choice == "Y":
        print(random.choice(fortune))
        choice = input('Would you like your fortune to be told again (Y/N)? ')
    elif choice == "N":
        print("Okay then...")
        break