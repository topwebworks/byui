# Please type a positive number: -3
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -8
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -1
# Sorry, that is a negative number. Please try again.
# Please type a positive number: 12
# The number is: 12

# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? yes
# Thank you.


print()
num = int(input("Please type a positive number: "))
print()
while num < 0:
    print("Sorry, that is a negative number. Please try again.")
    num = int(input("Please type a positive number: "))

print(f"The number is: {num}")
print()

print()
candy = ""

while candy != "yes":
    candy = input("May I have a piece of candy? ").lower()

print("Thank you.")
print()
