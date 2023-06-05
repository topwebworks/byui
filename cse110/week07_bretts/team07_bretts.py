
import random

restart = "yes"

while restart == "yes":

    guess_count = 0
    guess = -1

    # magic_num = int(input("What is the magic number? "))
    magic_num = random.randint(1, 100)
    result = ["Higher", "Lower", "You guessed it!"]

    print()
    # print(f"This is the mag_num: {magic_num}")

    while magic_num != guess:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1
        if magic_num > guess:
            print(result[0])
        elif magic_num < guess:
            print(result[1])
        else:
            print(result[2])

    print(f"You guessed {guess_count} times.")
    print()
    restart = input("Want to play again? (yes/no) ").lower()

print()
print("Thanks for playing! Goodbye.")
