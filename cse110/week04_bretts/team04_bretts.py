import math

# Data Input - Fahrenheit
print()
print('Welcome to the velocity calculator. Please enter the following:')
print()
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder):"))

# Calculate c = 1/2 p A C
c = (1 / 2) * p * A * C

# Calculate v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Output
print()
print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after 10.0 seconds is:  {v:.3f} m/s')
print()