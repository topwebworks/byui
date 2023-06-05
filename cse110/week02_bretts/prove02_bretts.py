import textwrap

print('\nPlease enter the following:\n')

# Story Data
adjective_1 = input('adjective: ').lower()
animal_1 = input('animal: ').lower()
verb_1 = input('verb: ').lower()
exclamation_1 = input('exclamation: ').upper()
verb_2 = input('verb: ').lower()
verb_3 = input('verb: ').lower()

print()

# Extra Story Elements
intro = f'Based on actual {adjective_1} {animal_1} events...'

# Check if use a or an before adjective_1
vowels = 'aeiou'

if adjective_1[0] in vowels:
  a_an = 'an'
else:
  a_an = 'a'

# Build Madlib
madlib = f'{intro}the other day, I was really in trouble. It all started when I saw {a_an} {adjective_1} {animal_1} {verb_1} down the hallway. "{exclamation_1}!" I yelled. But all I could think to do was to {verb_2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_3} right in front of my family.'

# Wrap text
wrapper = textwrap.TextWrapper(width=70)
word_list = wrapper.wrap(text=madlib)

# Madlib Output - Print each line
for element in word_list:
  print(element)

print()