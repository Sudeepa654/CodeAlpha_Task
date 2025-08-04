import random

def display_welcome():
    """Displays the welcome message and instructions."""
    print("=====================================")
    print("        WELCOME TO HANGMAN GAME      ")
    print("=====================================")
    print("Guess the word one letter at a time.")
    print("You have 6 chances to guess wrong.")
    print("Let's start!\n")

def get_random_word():
    """Selects a random word from a predefined list."""
    word_list = ['apple', 'banana', 'grape', 'mango', 'peach']
    return random.choice(word_list)

def display_word_progress(secret_word, guessed_letters):
    """Returns the word with unguessed letters replaced by underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def get_valid_guess(guessed_letters):
    """Prompts the user to enter a valid guess (a single alphabet character)."""
    while True:
        guess = input("Enter your guess (a-z): ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess

def play_hangman():
    display_welcome()

    secret_word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Word to guess:", display_word_progress(secret_word, guessed_letters))
    print()

    while incorrect_guesses < max_attempts and set(secret_word) != set(guessed_letters):
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Oops! '{guess}' is not in the word.")
        
        print(f"\nCurrent word: {display_word_progress(secret_word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    # End of game
    if set(secret_word) <= set(guessed_letters):
        print("🎉 Congratulations! You guessed the word correctly:", secret_word)
    else:
        print("💀 You've run out of guesses. The word was:", secret_word)

    print("\nThanks for playing Hangman!")

# Entry point
if __name__ == "__main__":
    play_hangman()