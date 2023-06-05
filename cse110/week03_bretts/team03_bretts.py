import math

print()
square_side = float(input('What is the length of a side of the square in centimeters? '))
square_area = square_side ** 2
square_area_sqmeters = square_area / 10000
print(f'The area of the square is: {square_area:.4f} cm\u00B2')
print(f'The area of the square in square meters is: {square_area_sqmeters:.4f} m\u00B2')

print()
rectangle_length = float(input('What is the length of rectangle in centimeters? '))
rectangle_width = float(input('What is the width of the rectangle in centimeters? '))
rectangle_area = rectangle_length * rectangle_width
rectangle_area_sqmeters = rectangle_area / 10000
print(f'The area of the rectangle is: {rectangle_area:.4f} cm\u00B2')
print(f'The area of the rectangle in square meters is: {rectangle_area_sqmeters:.4f} m\u00B2')

print()
circle_radius = float(input('What is the radius of the circle in centimeters? '))
circle_area = math.pi * (circle_radius ** 2)
circle_area_sqmeters = circle_area / 10000
print(f'The area of the circle is: {circle_area:.4f} cm\u00B2')
print(f'The area of the circle in square meters is: {circle_area_sqmeters:.4f} m\u00B2')

print()
fav_number = float(input('What is your favorite number? '))
fav_square_area = fav_number ** 2
fav_circle_area = math.pi * (fav_number ** 2)
fav_cube_volume = fav_number ** 3
fav_sphere_volume = (4/3) * math.pi * (fav_number ** 3)
print(f'The area of a square using your favorite number is: {fav_square_area:.4f}')
print(f'The area of a circle using your favorite number is: {fav_circle_area:.4f}')
print(f'The volume of a cube using your favorite number is: {fav_cube_volume:.4f}')
print(f'The volume of a sphere using your favorite number is: {fav_sphere_volume:.4f}')
print()
