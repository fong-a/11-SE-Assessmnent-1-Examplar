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
        display_game_state(secret_word, guessed_letters, attempts)


def display_game_state(secret_word, guessed_letters, attempts):
    # Function to display the game state, only displays letters that have been guessed
    for i in secret_word:
        if i in guessed_letters:
            print(i, end=" ")
        else:
            print("_", end=" ")

    # Print the number of lives / attempts left
    print("\nAttempts left: " + str(6 - attempts))


# Function to get a random word from the word list
def get_random_word(word_list):
    return choice(word_list)


# Function to get the player's guess
def get_player_guess():
    return input("Guess a letter: ")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
