#Rock, Paper, Scissors

from random import randint

t = ["R", "P", "S"]
# assign a random number to computer

computer = t[randint(0, 2)]
player = False
while player is False:

    player = input("R " "P " "S ? ")
    if computer == player:
        print("That's a Tie")
    elif player == "R":
        if computer == "P":
            print("CPU: Paper, Player: Rock ")
            print("You lose! Computer covers you up.")
        else:
            print("CPU: Scissors Player: Rock")
            print("You win! Your rock smashes computer's scissors")
    elif player == "S":
        if computer == "R":
            print("CPU: Rock Player: Scissors")
            print("You lose! Computer's rock smashes your Scissors.")
        else:
            print("CPU: Paper Player: Scissors")
            print("You win! Your scissors cuts through computer's paper.")
    elif player == "P":
        if computer == "S":
            print("CPU: Scissors Player: Paper")
            print("You lose! Computer's Scissors cuts through your paper.")
        else:
            print("CPU: Rock Player: Paper")
            print("You win! Your paper covers computer's rock.")
    else:
        print("That's not a valid play. Please check your spellings.")

