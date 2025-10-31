import random

def get_random_word():
    """Returns a random word from a predefined list."""
    words = ["python", "programming", "hangman", "developer", "computer", "keyboard", "algorithm", "variable", "function"]
    return random.choice(words).upper()

def display_hangman(incorrect_guesses):
    """Prints the ASCII art for the hangman based on incorrect guesses."""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    print(stages[incorrect_guesses])

def play_hangman():
    """Main function to play the Hangman game."""
    word_to_guess = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)

        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()