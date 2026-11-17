import random

questions_list = [
    {"What is 5 + 7?" : "12"},
    {"What is 6 * 3?" : "18"},
    {"What is the square root of 49?" : "7"},
    {"What is 15-4?" : "11"},
    {"What is the 25 / 5 ?" : "5"}
]


answer = questions_list[0]["What is 5 + 7?"], questions_list[1]["What is 6 * 3?"], questions_list[2]["What is the square root of 49?"], questions_list[3]["What is 15-4?"], questions_list[4]["What is the 25 / 5 ?"]

score = 0

print("Quizmaster: Welcome to the Quiz Game!")
yon = input("Quizmaster: Do you want to play?\n(yes/no)\nYou: ").lower()

while True:
    if yon == "yes":
        score = 0
        print("Quizmaster: Great! Let's start the game!")
        random.shuffle(questions_list)
        for question in questions_list:
            for q, answer in question.items():
                player = input(q + "\nYou: ")
                if player == answer:
                    print(f"Quizmaster: Correct! You earned 1 point. (Score: {score + 1})")
                    score += 1
                else:
                    print(f"Quizmaster: Incorrect! The correct answer is: {answer} (Score: {score})")
        print(f"Quizmaster: Your final score is: {score}")
        yon = input("Quizmaster: Do you want to play again?\n(yes/no)\nYou: ").lower()

    elif yon == "no":
        print("Quizmaster: Okay, maybe next time!")
        break 
    else:
        print("Quizmaster: Please enter 'yes' or 'no'.")
        yon = input("Quizmaster: Do you want to play?\n(yes/no)\nYou: ").lower()
        
