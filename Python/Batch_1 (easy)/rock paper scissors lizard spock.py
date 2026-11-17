import random

yuumi = [
    "Rock",
    "Paper",
    "Scissor",
    "Lizard",
    "Spock",
]

choice = input("Yuumi: Let's play Rock Paper Scissor Lizard Spock!\n(Sure/Nah)\nYou: ")

while True:
    if choice == "Sure":
        print("Yuumi: Without further ado...\nLet's Begin")
        play = input(
            "Yuumi:\n" \
            "Pick from your options below:\n" \
            "Rock\n" \
            "Paper\n" \
            "Scissor\n" \
            "Lizard\n" \
            "Spock\n" \
            "You: "
        )
        if play not in yuumi:
            print("Please pick Rock, Paper, Scissor, Lizard, Spock")
            continue
        yuumi_play = random.choice(yuumi)
        print(f"Yuumi played {yuumi_play}")

        if play == yuumi_play:
            print("It's a Tie!")
            choice = input("Yuumi: Woahhh Great minds think alike am I right?\n" \
            "Well then,\n" \
            "Wanna go again?\n" \
            "(Sure/Nah)\n" \
            "You: ")
        elif (
            (play == "Rock" and yuumi_play in ["Scissor", "Lizard"])
            or(play == "Scissor" and yuumi_play in ["Paper", "Lizard"])
            or(play == "Paper" and yuumi_play in ["Rock", "Spock"])
            or(play == "Lizard" and yuumi_play in ["Spock", "Paper"])
            or(play == "Spock" and yuumi_play in ["Scissor", "Rock"])
        ):
            print("You Win!")
            choice = input("Yuumi: Aw man, you beat me! Wanna go again?\n(Sure/Nah)\nYou: ")
        elif (
            (play == "Rock" and yuumi_play in ["Paper", "Spock"])
            or(play == "Scissor" and yuumi_play in ["Rock", "Spock"])
            or(play == "Paper" and yuumi_play in ["Scissor", "Lizard"])
            or(play == "Lizard" and yuumi_play in ["Rock", "Scissor"])
            or(play == "Spock" and yuumi_play in ["Paper", "Lizard"])
        ):
            print("You Lose!")
            choice = input("Yuumi: Nice! I beat you this time! Wanna go again?\n(Sure/Nah)\nYou: ")
        else:
            choice = input("Yuumi: Sorryy, but I couldn't understand you...\n" \
            "can you repeat that one more time?\n" \
            "(Sure/Nah)\n" \
            "You: ")