import random

dice = [1,
        2,
        3,
        4,
        5,
        6]

yn = input("Yo! You wanna roll some dice? (Y/N): ")

while True:
    if yn == "Y":
        print(random.choice(dice))
        yn = input("Roll once more? (Y/N): ")
    elif yn == "N":
        print("Gotcha, See Ya Later!")
        break    
    else:
        yn = input("Whatcha say?? I don't get it so tell me again (Y/N):")