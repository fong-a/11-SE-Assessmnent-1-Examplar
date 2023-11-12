from random import choice

# hangPy.py is a Python implementation of the classic game Hangman.
# created by: Andrew Fong on 12/11/2023


# Function to run the game
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
    attempts = 0  # Number of attempts
    game_won = False  # Boolean to check if game is won

    # Game loop
    while attempts < 6 and not game_won:
        pass


# Function to get a random word from the word list
def get_random_word(word_list):
    return choice(word_list)


# Function to get the player's guess
def get_player_guess():
    pass  # Placeholder for player's guess input function


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
