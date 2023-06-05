# Data Input
print()
grade_percentage = float(input('What is your grade percentage? '))
grade_percentage = round(grade_percentage)
# print(grade_percentage)
print()

# Find Grade Letter
letter = 'ABCDF'

if grade_percentage >= 90:
    grade = letter[0]
elif grade_percentage >= 80:
    grade = letter[1]
elif grade_percentage >= 70:
    grade = letter[2]
elif grade_percentage >= 60:
    grade = letter[3]
else:
    grade = letter[4]

# Add Plus or Minus Grade Symbol    
if int(str(grade_percentage)[1]) >= 7:
    symbol = '+'
elif int(str(grade_percentage)[1]) <= 3:
    symbol = '-'
else:
    symbol = ''

# No Grade Symbol above 93 or below 60
if grade_percentage < 60 or grade_percentage > 93:
    symbol = ''

# Output Grade
print(f'Your grade is {grade}{symbol}')

# Print Passed or Not 
if grade_percentage >= 70:
  print('You have passed this course!')
else:
  print('You did not pass this course. Keep studying.')
print()
    