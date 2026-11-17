import random

charlotte = ["Rock", "Paper", "Scissors"]

choice = input("Charlotte: Let's play Rock Paper Scissors (Okay/Nah): ")

while True:
    if choice == "Okay":
        print("Charlotte: Alright Let's Begin")
        play = input("Charlotte\nPick from your options below:\nRock\nPaper\nScissors\nYou Played: ")
        charlotte_play = random.choice(charlotte)
        if play == "Rock" and charlotte_play == "Rock":
            print(f"Charlotte played: {charlotte_play}")
            print("It's a Tie")
            choice = input("Run it back? (Okay/Nah)")
        elif play == "Rock" and charlotte_play == "Scissors":
            print(f"Charlotte played: {charlotte_play}")
            print("You Win!")
            choice = input("Run it back? (Okay/Nah)")
        elif play == "Rock" and charlotte_play == "Paper":
            print(f"Charlotte played: {charlotte_play}")
            print("You Lose!")
            choice = input("Run it back? (Okay/Nah)")
        elif play == "Paper" and charlotte_play == "Paper":
            print(f"Charlotte played: {charlotte_play}")
            print("It's a Tie")
            choice = input("Run it back? (Okay/Nah)")
        elif play == "Paper" and charlotte_play == "Rock":
            print(f"Charlotte played: {charlotte_play}")
            print("You Win!")
            choice = input("Run it back? (Okay/Nah)")            
        elif play == "Paper" and charlotte_play == "Scissors":
            print(f"Charlotte played: {charlotte_play}")
            print("You Lose!")
            choice = input("Run it back? (Okay/Nah)")            
        elif play == "Scissors" and charlotte_play == "Paper":
            print(f"Charlotte played: {charlotte_play}")
            print("You Win!")
            choice = input("Run it back? (Okay/Nah)")                
        elif play == "Scissors" and charlotte_play == "Rock":
            print(f"Charlotte played: {charlotte_play}")
            print("You Lose!")
            choice = input("Run it back? (Okay/Nah)")            
        elif play == "Scissors" and charlotte_play == "Scissors":
            print(f"Charlotte played: {charlotte_play}")
            print("It's a Tie")
            choice = input("Run it back? (Okay/Nah)")
        elif play not in charlotte:
            print('Please pick Rock, Paper, or Scissors')
            continue
    elif choice == "Nah":
        print("Oh alright, See you!")    
        break
    else:
        choice = input("Sooo Okay or Nah...? :")

