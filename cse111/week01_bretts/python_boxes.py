# python boxes.py
# Enter the number of items: 8
# Enter the number of items per box: 5
# For 8 items, packing 5 items in each box, you will need 2 boxes.

import math

# inputs
num_items = int(input(f"Enter the number of items: "))
num_items_box = int(input(f"Enter the number of items per box: "))

# Calculate number of boxes
# print(num_items / num_items_box)
num_boxes = math.ceil(num_items / num_items_box)

# Output
print()
print(f"For {num_items} items, packing {num_items_box} items in each box, you will need {num_boxes} boxes.")
print()
