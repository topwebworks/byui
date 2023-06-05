import random


word_list = ["long", "longer", "longest"]


print("Welcome to the word guessing game!")
print()


restart = "yes"

while restart == "yes":

    guess_count = 0
    word_guess = ""

    secret_word = random.choice(word_list).lower()
    # secret_length = len(secret_word)

    while word_guess != secret_word:
        # print(f"Your hint is: {word_hint}")
        word_guess = input("What is your guess? ").lower()
        guess_count = guess_count + 1
        if word_guess != secret_word:
            print("Your guess was not correct.")
        else:
            print("Congratulations! You guessed it!")

    print(f"You guessed {guess_count} times.")
    print()
    restart = input("Want to play again (yes/no)? ").lower()

print()
print("Thanks for playing! Goodbye.")
