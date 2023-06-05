import datetime

# Get current month for start month. Not as flexible as input, but a fun excercize.
currentDate = datetime.date.today()
currentMonthName = currentDate.strftime("%B").capitalize()

print('\nEnter your information below:\n')

# ID Badge Data
first_name = input('First name: ').capitalize()
last_name = input('Last name: ').upper()
email = input('Email address: ').lower()
phone = input('Phone number: ')
title = input('Job title: ').title()
id_number = input('ID number: ')

divider = '--------------------------------------------'
intro = 'The ID Card is:'

# Stretch Data
eye_color = input('Eye color: ').title()
hair_color = input('Hair color: ').title()
training = input('Training? (Yes/No): ').title()

# ID Badge Formating
id = f'ID: {id_number}'
name = f'{last_name}, {first_name}'

# Stretch Formatting
stretch1 = f'Hair: {hair_color:17} Eyes: {eye_color}'
stretch2 = f'Started: {currentMonthName:14} Training: {training}'

# Build ID Badge
id_badge = f'\n{intro}\n{divider}\n{name}\n{title}\n{id}\n\n{email}\n{phone}\n\n{stretch1}\n{stretch2}\n{divider}\n'

# ID Badge Output
print(id_badge)
