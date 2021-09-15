import time
import random

words_bank = [
    "january",
    "border",
    "image",
    "film",
    "promise",
    "kids",
    "lungs",
    "doll",
    "rhyme",
    "damage",
    "plants",
]


def start_game():
    word = random.choice(words_bank)


def init_game():
    time.sleep(1)
    print("Let's play Hangman!")
    time.sleep(1)
    print("You will have 5 guesses before you are hanged. Let's try your best!")
    time.sleep(1)
    confirm_game_start = input("Are you ready: ")

    while confirm_game_start not in ['Y', 'N', 'y', 'n']:
        confirm_game_start = input("Come on! Are you ready: ")
    if confirm_game_start in ['Y', 'y']:
        start_game()
    elif confirm_game_start in ['N', 'n']:
        print("Maybe later (◞‸◟；)")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    init_game()
