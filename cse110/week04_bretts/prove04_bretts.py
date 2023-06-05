
# Data Inputs
print()
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input('How many children are there? '))
num_adults = int(input('How many adults are there? '))
sales_tax_rate = float(input('What is the sales tax rate? '))

# Calculate Subtotal
subtotal_child = child_meal_price * num_children
subtotal_adult = adult_meal_price * num_adults
subtotal_price_list = [subtotal_child, subtotal_adult]
subtotal = sum(subtotal_price_list)

# Calculate Sales Tax
sales_tax_rate = sales_tax_rate / 100
sales_tax = subtotal * sales_tax_rate

# Calculate Total
total = subtotal + sales_tax

# Print Price Summary
print()
# print(f'subtotal_child: ${subtotal_child:.2f}')
# print(f'subtotal_adult: ${subtotal_adult:.2f}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

# Print Tip Options
print()
tip_rates = [.18, .20, .22]
for rate in tip_rates:
  # print(type(rate))
  # print(rate)
  # print(total)
  tip_amount = (rate * total)
  tip_percent = (rate * 100)
  print(f'{int(tip_percent)}% Tip: ${tip_amount:.2f}')
  
print()
customer_tip = float(input("Tip amount? $"))

# Print Grand Total with Tip
print()
grand_total = total + customer_tip
print(f'Your new total with tip: ${grand_total:.2f}')

# Payment
print()
customer_payment_amount = float(input("What is your payment amount? $"))

# Any Change owed?
print()
change = customer_payment_amount - grand_total

if change < 0:
    change = grand_total - customer_payment_amount
    print(f'Sorry, you still owe: ${change:.2f}')
elif grand_total == total:
    print(f'Change: ${change:.2f}. Really, no tip?')
elif change == 0 and customer_tip <= 0:
    print('No change. Also, no tip!')
elif change == 0 and customer_tip > 0:
    print('No change. Thank you!')
else:
    print(f'Change: ${change:.2f}. Thank you!')

print()
