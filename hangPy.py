from random import choice

# hangPy.py is a Python implementation of the classic game Hangman.
# created by: Andrew Fong on 12/11/2023


def main():
    # Function to run the game
    word_list = {
        1: ["cat", "dog", "rat"],
        2: ["elephant", "giraffe", "dolphin"],
        3: ["hippopotamus", "chrysanthemum", "pterodactyl"],
    }

    difficulty = int(input("Select a difficulty level (1, 2, or 3): "))
    while difficulty not in [1, 2, 3]:
        print("Invalid input. Please enter 1, 2, or 3.")
        difficulty = int(input("Select a difficulty level (1, 2, or 3): "))

    secret_word = choice(word_list[difficulty])
    guessed_letters = set()  # Set to store guessed letters
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
        if guess not in secret_word:
            attempts += 1  # Increment attempts if guess is wrong
        game_won = check_game_won(secret_word, guessed_letters)  # Check if game is won
    show_win_loss_screen(game_won, secret_word)  # Show win/loss screen


def update_guessed_letters(guessed_letters, guess):
    # Function to update the guessed letters
    # If letter already been guessed, print message and get another guess
    if guess not in guessed_letters:
        guessed_letters.add(guess)
    else:
        print("You already guessed that letter!")
        update_guessed_letters(guessed_letters, get_player_guess())
    return guessed_letters


def show_ascii_hangman(attempts):
    # Function to show the ascii hangman
    if attempts == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif attempts == 6:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("|             ")


def display_game_state(secret_word, guessed_letters, attempts):
    # Function to display the game state, only displays letters that have been guessed
    show_ascii_hangman(attempts)
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
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter, not a number or symbol.")
        else:
            return guess  # Exit the loop if the input is valid


def check_game_won(secret_word, guessed_letters):
    # Function to check if the game is won
    for i in secret_word:
        if i not in guessed_letters:
            return False
    return True


def show_win_loss_screen(game_won, secret_word):
    # Function to show the win screen
    if game_won:
        print(f"You won! The word was {secret_word}")
    else:
        print("You lost!")


if __name__ == "__main__":
    play_game = True
    while play_game:
        main()
        play_again = input("Play again? (y/n): ")
        if play_again == "n":
            play_game = False
