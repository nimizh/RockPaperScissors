import random


def play():
    print("WELCOME TO THE ROCK PAPER AND SCISSORS GAME")
    print("Rules are  1.Rock> Scissors  2.Scissors> Paper  3.Paper>Rock")

    user = input(
        "What is your choice?? R for Rock, S for Scissors P for paper".lower())

    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'It is A Tie'

    if is_win(user, computer):
        return 'YOU WON !! :)'

    else:
        return 'You Lost :('


def is_win(player, opponent):

    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
