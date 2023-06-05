# What is the temperature in Fahrenheit? 81
# The temperature in Celsius is 27.2 degrees.

# Data Input - Fahrenheit
print()
temperature_f = float(input("What is the temperature in Fahrenheit? "))

# Calculate Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * (5 / 9)

# Output
print(f'The temperature in Celsius is {temperature_c:.1f} degrees.')
print()