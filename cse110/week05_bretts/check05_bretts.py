# What is the first number? 4
# What is the second number? 3

# The first number is greater
# The numbers are not equal
# The second number is not greater

# What is your favorite animal? sdfdsf
# That one is not my favorite.

# Compare Numbers
print()
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')

if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')

# Compare Strings
print()
fav_animal = input('What is your favorite animal? ')

if fav_animal.lower() == 'bear':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')