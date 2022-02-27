import random


print(f"Hello there!\nToday you have signed up to play Rock-paper-scissors!")
print()
while True:
    try:
        diff = int(input(f"Would you like\nEasy(1) \nNormal(2) \nHard(3)\n"))
    except ValueError:
        print("Thats not an answer")

    # easy diff
    if diff == 1:
        choice = int(
            input(f"Would you like\nRock(1) \nPaper(2)\nor \nScissors(3)\n"))
        RPS_choices = ["Rock", "Paper", "Scissors"]
        RPS = random.choice(RPS_choices)
        if choice == 1:
            easy = ["Scissors", "Scissors", "Rock",
                    "Paper", "Rock", "Scissors", "Scissors"]
            easy_choice = random.choice(easy)
            if easy_choice == "Paper":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Paper")
                print("You Lost!!!")

            if easy_choice == "Rock":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Rock")
                print("You Tied!!!")

            if easy_choice == "Scissors":
                print()
                print("You chose: Rock")
                print("The computer chose: Scissors")
                print("You WON!!!")

        if choice == 2:
            easy = ["Scissors", "Rock", "Paper",
                    "Paper", "Rock", "Rock", "Rock"]
            easy_choice = random.choice(easy)
            if easy_choice == "Paper":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Paper")
                print("You Tied!!!")

            if easy_choice == "Rock":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Rock")
                print("You Won!!!")

            if easy_choice == "Scissors":
                print()
                print("You chose: Paper")
                print("The computer chose: Scissors")
                print("You Lost!!!")

        if choice == 3:
            easy = ["Scissors", "Scissors", "Paper",
                    "Paper", "Paper", "Paper", "Rock"]
            easy_choice = random.choice(easy)
            if easy_choice == "Paper":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Paper")
                print("You Won!!!")

            if easy_choice == "Rock":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Rock")
                print("You Lost!!!")

            if easy_choice == "Scissors":
                print()
                print("You chose: Scissors")
                print("The computer chose: Scissors")
                print("You Tied!!!")

    # Medium diff
    elif diff == 2:
        choice = int(
            input(f"Would you like\nRock(1) \nPaper(2)\nor \nScissors(3)\n"))
        RPS_choices = ["Rock", "Paper", "Scissors"]
        RPS = random.choice(RPS_choices)
        if choice == 1:
            medium = ["Paper", "Rock", "Scissors", "Scissors"]
            medium_choice = random.choice(medium)
            if medium_choice == "Paper":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Paper")
                print("You Lost!!!")

            if medium_choice == "Rock":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Rock")
                print("You Tied!!!")

            if medium_choice == "Scissors":
                print()
                print("You chose: Rock")
                print("The computer chose: Scissors")
                print("You WON!!!")

        if choice == 2:
            medium = ["Paper", "Rock", "Scissors", "Scissors"]
            medium_choice = random.choice(medium)
            if medium_choice == "Paper":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Paper")
                print("You Tied!!!")

            if medium_choice == "Rock":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Rock")
                print("You Won!!!")

            if medium_choice == "Scissors":
                print()
                print("You chose: Paper")
                print("The computer chose: Scissors")
                print("You Lost!!!")

        if choice == 3:
            medium = ["Paper", "Rock", "Scissors", "Scissors"]
            medium_choice = random.choice(medium)
            if medium_choice == "Paper":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Paper")
                print("You Won!!!")

            if medium_choice == "Rock":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Rock")
                print("You Lost!!!")

            if medium_choice == "Scissors":
                print()
                print("You chose: Scissors")
                print("The computer chose: Scissors")
                print("You Tied!!!")

    elif diff == 3:
        choice = int(
            input(f"Would you like\nRock(1) \nPaper(2)\nor \nScissors(3)\n"))
        RPS_choices = ["Rock", "Paper", "Scissors"]
        RPS = random.choice(RPS_choices)
        if choice == 1:
            hard = ["Paper", "Rock", "Scissors"]
            hard_choice = random.choice(hard)
            if hard_choice == "Paper":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Paper")
                print("You Lost!!!")

            if hard_choice == "Rock":
                print()
                print("You chose: Rock")
                print(f"The computer chose: Rock")
                print("You Tied!!!")

            if hard_choice == "Scissors":
                print()
                print("You chose: Rock")
                print("The computer chose: Scissors")
                print("You WON!!!")

        if choice == 2:
            hard = ["Paper", "Rock", "Scissors"]
            hard_choice = random.choice(hard)
            if hard_choice == "Paper":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Paper")
                print("You Tied!!!")

            if hard_choice == "Rock":
                print()
                print("You chose: Paper")
                print(f"The computer chose: Rock")
                print("You Won!!!")

            if hard_choice == "Scissors":
                print()
                print("You chose: Paper")
                print("The computer chose: Scissors")
                print("You Lost!!!")

        if choice == 3:
            hard = ["Paper", "Rock", "Scissors"]
            hard_choice = random.choice(hard)
            if hard_choice == "Paper":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Paper")
                print("You Won!!!")

            if hard_choice == "Rock":
                print()
                print("You chose: Scissors")
                print(f"The computer chose: Rock")
                print("You Lost!!!")

            if hard_choice == "Scissors":
                print()
                print("You chose: Scissors")
                print("The computer chose: Scissors")
                print("You Tied!!!")

    again = input(f"Press Enter to play again!\n")
    if again == "":
        pass
