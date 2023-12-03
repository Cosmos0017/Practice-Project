import random

def play():
    """
    This function takes input from user, randomizes computer input and
    """
    user = input("Enter 'r' for rock, 's' for scissor, 'p' for paper: \n")
    computer = random.choice(['r', 's', 'p'])

    print("You: ", user)
    print("Computer: ", computer)
    if user == computer:
        return("")
    
    if is_win(user, computer):
        return("User wins")

    return("Computer wins")


def is_win(p1, p2):
    """
    This function decides who won wrt to given inputs.
    param p1: player 1 input
    param p2: player 2 input
    win rules: r>s, s>p, p>r
    """
    if (p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r"):
        return True

print(play())