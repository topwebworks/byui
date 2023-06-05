# What is the age of the first rider? 12
# What is the height of the first rider? 46
# Is there a second rider (yes/no)? no
# What is the age of the second rider? 14
# What is the height of the second rider? 35
# Sorry, you may not ride.
# Welcome to the ride. Please be safe and have fun!


can_ride = False

print()
age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))
sec_rider = input("Is there a second rider (yes/no)? ")

# If a second rider
if sec_rider.lower() == "yes":
    sec_age = int(input("What is the age of the second rider? "))
    sec_height = int(input("What is the height of the second rider? "))

    # Rule 1
    if (height < 36 or sec_height < 36):
        can_ride = False
    # Rule 3
    else:
        if age >= 18 or sec_age >= 18:
            can_ride = True
        else:
            can_ride = False
# Else a single rider
else:
    # Rule 2
    if age >= 18 and height >= 62:
        can_ride = True
    else:
        can_ride = False

print()
# Output
if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
