"""

Workflow of project:

1- Input from user(Rock, Paper, scissor)
2- Computer choice(Computer will choose randomly not conditionally)
3- Result print


Cases:

A- Rock
Rock - Rock = tie 
Rock - Paper = Paper Win 
Rock - Scissor = Rock Win 

B - Paper
Paper - Paper = tie 
Paper - Rock = Paper Win 
Paper - Scissor = Scissor win 

C - Scissor
Scissor - Scissor = Tie 
Scissor - Rock = Rock Win 
Scissor - Paper = Scissor Win 
"""

import random
item_list = ["Rock" ,  "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses Same : = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = Computer win")


    else:
        print("Rock will break Scissor = You Win")


elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = Computer Win")

    else:
        print("Paper overs rock = You Win")


elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor will cut paper = You win")


    else:
        print("Rock will break scissor = Computer wins")


"""

