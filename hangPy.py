from random import choice

# hangPy.py is a Python implementation of the classic game Hangman.
# created by: Andrew Fong on 12/11/2023


def main():
    # Function to run the game
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
        display_game_state(
            secret_word, guessed_letters, attempts
        )  # Display the game state
        guess = get_player_guess()  # Get player's guess
        guessed_letters = update_guessed_letters(
            guessed_letters, guess
        )  # Update guessed letters


def update_guessed_letters(guessed_letters, guess):
    # Function to update the guessed letters
    # If letter already been guessed, print message and get another guess
    if guess not in guessed_letters:
        guessed_letters.add(guess)
    else:
        print("You already guessed that letter!")
        update_guessed_letters(guessed_letters, get_player_guess())
    return guessed_letters


def display_game_state(secret_word, guessed_letters, attempts):
    # Function to display the game state, only displays letters that have been guessed
    for i in secret_word:
        if i in guessed_letters:
            print(i, end=" ")
        else:
            print("_", end=" ")

    # Print the number of lives / attempts left
    print("\nAttempts left: " + str(6 - attempts))


def get_random_word(word_list):
    # Function to get a random word from the word list
    return choice(word_list)


def get_player_guess():
    # Function to get the player's guess
    return input("Guess a letter: ")


if __name__ == "__main__":
    main()
