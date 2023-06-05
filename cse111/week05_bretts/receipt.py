
import csv
from datetime import datetime

# Expected Output

# Inkom Emporium

# wheat bread: 2 @ 2.55
# 1 cup yogurt: 4 @ 0.75
# 32 oz granola: 1 @ 3.21
# twix candy bar: 2 @ 0.85
# 1 cup yogurt: 3 @ 0.75

# Number of Items: 12
# Subtotal: 15.26
# Sales Tax: 0.92
# Total: 16.18

# Thank you for shopping at the Inkom Emporium.
# Wed Nov 4 05:10:30 2020


def main():
    try:
        PRODUCT_INDEX = 0

        # Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
        products_dict = read_dict("products.csv", PRODUCT_INDEX)

        # Prints the products_dict.
        # print(products_dict)

        # Opens the request.csv file for reading.
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)

            # Skips the first line of the request.csv file
            next(reader)

            # 1. Print the store name at the top of the receipt.
            print()
            print("Inkom Emporium")
            print()

            # Uses a loop that reads and processes each row from the request.csv file
            total_quantity = 0
            subtotal = 0
            tax_rate = .06
            for row_list in reader:

                # Use the requested product number to find the corresponding item in the products_dict.
                requested_product_number = row_list[0]
                request_quantity = row_list[1]
                requested_list = products_dict[requested_product_number]

                total_quantity += int(request_quantity)

                request_price = float(
                    requested_list[2]) * float(request_quantity)
                subtotal += float(request_price)

                tax_rate = .06
                sales_tax = subtotal * tax_rate

                total_due = subtotal + sales_tax

                # 2. Print the list of ordered items. Print the product name, requested quantity, and product price.
                print(
                    f"{requested_list[1]}: {request_quantity} @ {requested_list[2]}")

        # 3. Sum and print the number of ordered items.
        print()
        print(f"Number of items: {total_quantity}")

        # 4. Sum and print the subtotal due.
        print(f"Subtotal: {round(subtotal, 2)}")

        # 5. Compute and print the sales tax amount. Use 6% as the sales tax rate.
        print(f"Sales Tax: {round(sales_tax, 2)}")

        # 6. Compute and print the total amount due.
        print(f"Total: {round(total_due, 2)}")

        # 7. Print a thank you message.
        print()
        print("Thank you for shopping at the Inkom Emporium.")

        # 8. Get the current date and time from your computer’s operating system and print the current date and time.
        # Wed Nov 4 05:10:30 2020 - I changed syntax to be more readable - Fri Jan 13 2023  11:07:51 AM
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %Y  %I:%M:%S %p}")
        print()

        # STRETCH: Write code to print a coupon at the bottom of the receipt.
        # Write the code so that it will always print a coupon for one of the products ordered by the customer.
        print(
            f"*** LOYALTY COUPON for {requested_list[1]}: Use code INK{requested_product_number} ***")
        print()

    # 9. Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    # Expected Output
    # Error: unknown product ID in the request.csv file
    # 'R002'
    # -----------
    # Error: missing file
    # [Errno 2] No such file or directory: 'products.csv'
    except (FileNotFoundError, PermissionError) as error:
        print()
        print("Error: missing file")
        print(error)
        print()

    except (csv.Error, KeyError) as error:
        print()
        print(
            f"Error: unknown product ID in the {csv_file.name} file")
        print(error)
        print()


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()
