

# Inputs
temp_input = float(input("What is the temperature? "))
fc = input("Fahrenheit or Celsius (F/C)? ").lower()


# Convert to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahren = ((9/5) * celsius) + 32
    return fahren


# Calculate the Windchill
def windchill(temp, wind):
    return 35.74 + (.6215 * temp) - (35.75 * wind ** .16) + (0.4275 * temp * wind ** .16)


# If celsius input, call convert function
if fc == "c":
    temp = convert_to_fahrenheit(temp_input)
else:
    temp = temp_input


# Loop windchill funtion
for wind in range(5, 61, 5):
    chill = float(windchill(temp, wind))
    print(
        f"At temperature {temp}F, and wind speed {wind} mph, the windchill is: {chill:.2f}F")
