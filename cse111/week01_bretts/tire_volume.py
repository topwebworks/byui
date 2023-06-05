

import math
from datetime import date

pi = math.pi
today = date.today()

# Get inputs
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate approximate volume
v = (pi * (w**2)*a*(w*a+2540*d))/10**10

# Output
print()
print(f"The approximate volume is {v:.2f} liters")
print()

# Writes to file core values
with open("volumes.txt", "a") as file:
    file.write(f"{today}, ")  # current date
    file.write(f"{w}, ")  # width of the tire
    file.write(f"{a}, ")  # aspect ratio of the tire
    file.write(f"{d}, ")  # diameter of the wheel

# Writes to file with /n - either just volume or volume & phone
buy_tires = input(
    "Buy tires with the entered dimensions? (yes/no) ").lower()

if buy_tires != "no":
    cust_phone = input("Please enter your phone number: ")
    with open("volumes.txt", "a") as file:
        file.write(f"{v:.2f}, ")  # volume of the tire
        file.write(f"{cust_phone}\n")  # customer phone
else:
    with open("volumes.txt", "a") as file:
        file.write(f"{v:.2f}\n")  # volume of the tire
