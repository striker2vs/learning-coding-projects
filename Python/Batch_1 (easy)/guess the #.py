import random


print("Anson: Welcome to the Guess the Number Game!")
yon = input("Anson: Do you want to play?\n(yes/no)\nYou:  ").strip().lower()

while yon == "yes":
    print("Anson: Great! Let's start the game.")
    answer = random.randint(1,100)
    while True:
        guess = int(input("Anson: Now then, Guess a number between 1 and 100.\nYou: "))
        if guess == answer:
            print("Anson: Congratulations! You guessed the correct number!")
            break
        elif guess < answer:
            print("Anson: Your guess is too low. Try again.")
        elif guess > answer:
            print("Anson: Your guess is too high. Try again.")
        else:
            print("Anson: Invalid input. Please enter a number between 1 and 100.")
    yon = input("Anson: Do you want to play again?\n(yes/no)\nYou:  ").strip().lower()


while yon == "no".lower():
    while True:
        print("Anson: Alright! Maybe next time. Goodbye!")
        break
while yon != "yes" and yon != "no":
    while True:    
        yon = input("Anson: Come Again?\n(yes/no)\nYou:  ").strip().lower()
        break