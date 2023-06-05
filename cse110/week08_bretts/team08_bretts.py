
word = "Commitment"

fav_letter = input("What is you favorite letter? ").lower()

for letter in word:
    if letter.lower() == fav_letter.lower():
        # print(letter.upper(), end="")
        print("_", end="")
    else:
        print(letter.lower(), end="")

print()

# restart = "yes"
# while restart == "yes":

#     quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

#     n = int(input("Please enter a number: "))

#     for i, letter in enumerate(quote):
#         if i % n == 0:
#             print(letter.upper(), end="")
#         else:
#             print(letter.lower(), end="")

#     print()
#     restart = input("Want to play again? (yes/no) ").lower()

# print()
# print("Thanks for playing! Goodbye.")
