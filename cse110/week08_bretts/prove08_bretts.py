import random
import os

word_list = ["beauty", "degree", "noise", "easy", "model", "cattle",
             "specific", "sale", "wooden", "both", "orange", "can",
             "horn", "drop", "come", "village", "star", "purpose",
             "third", "dear", "curious", "cost", "glass", "hundred",
             "guard", "individual", "skin", "hello", "main", "east",
             "strength", "prepare", "seldom", "fast", "flat", "worry",
             "warm", "principal", "dry", "nervous", "former", "nuts"]

restart = "yes"

while restart == "yes":
    os.system("cls")
    print("Welcome to the word guessing game! Lower letter means word contains it. CAPS means correct!")
    print()

    secret_word = random.choice(word_list).lower()
    guess_count = 0
    word_guess = ""
    i = 0

    print("Your hint is: ", end="")
    for i in range(i, len(secret_word)):
        print("_ ", end="")
    print()

    while word_guess != secret_word:
        word_guess = input("What is your guess? ").lower()
        guess_count = guess_count + 1
        if len(word_guess) == len(secret_word) and word_guess != secret_word:
            print("Your hint is: ", end="")
            i = 0
            for i in range(i, len(word_guess)):
                if word_guess[i] == secret_word[i]:
                    print(f"{word_guess[i].upper()} ", end="")
                elif word_guess[i] != secret_word[i] and word_guess[i] in secret_word:
                    print(f"{word_guess[i].lower()} ", end="")
                else:
                    print("_ ", end="")
            print()
        elif len(word_guess) > len(secret_word):
            print("*guess too long*")
        elif len(word_guess) < len(secret_word):
            print("*guess too short*")
        else:
            print()
            print(f"Congratulations! You guessed {secret_word.upper()}!")
            print(f"It took you {guess_count} guesses.")

    print()
    restart = input("Want to play again (yes/no)? ").lower()

print()
print("Thanks for playing! Goodbye.")
print()
