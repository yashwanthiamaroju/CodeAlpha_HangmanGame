import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "intern"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is guessed
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    # Take input from user
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# If user loses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)