from datetime import datetime

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10 % from the subtotal. Your program must then compute the total amount due by adding sales tax of 6 % to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = float(input("Please enter the subtotal: "))

current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:.2f}")
