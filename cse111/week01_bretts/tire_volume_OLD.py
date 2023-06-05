# python tire_volume.py
# Enter the width of the tire in mm (ex 205): 185
# Enter the aspect ratio of the tire (ex 60): 50
# Enter the diameter of the wheel in inches (ex 15): 14

# The approximate volume is 24.09 liters


import math
pi = math.pi

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
