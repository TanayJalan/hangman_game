from random import random

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
        """
            +--------+
            |
            |
            |
            |
            |
        ===========
        """
    ]
    if 0 <= hangman < len(graphic):
        print(graphic[hangman])
    else:
        print("Invalid hangman stage.")
