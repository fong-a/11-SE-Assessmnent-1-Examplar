from random import choice

# hangPy.py is a Python implementation of the classic game Hangman.
# created by: Andrew Fong on 12/11/2023


def main():
    word_list = [
        "apple",
        "banana",
        "cherry",
        "orange",
        "grape",
        "kiwi",
        "lemon",
        "melon",
        "peach",
        "pear",
    ]  # List to store the words
    guessed_letters = set()  # Set to store guessed letters
    secret_word = get_random_word(word_list)


def get_random_word(word_list):
    return choice(word_list)


def get_player_guess():
    pass  # Placeholder for player's guess input function


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
