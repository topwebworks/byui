import os

cart_items = []
item_prices = []
error_msg = ["Oops! Missing positive number. Try again.",
             "Please input a number.", "Your cart is empty. Add items first.", "Item number not found."]

# Functions


def show_instructions():
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart (Redundant)")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print()


def reset_main():
    os.system("cls")
    main()


def num_error():
    if len(cart_items) > 1:
        os.system("cls")
        list_cart()
        print()
        print(f"Please input a number from 1-{len(cart_items)}.")
    else:
        os.system("cls")
        list_cart()
        print()
        print(f"Please input the number 1.")


def add_item():
    item = ""
    while item != "done":
        price = 0
        print()
        item = input("Add item? or [done]? ").lower()
        if item != "" and item != "done":
            try:
                price = float(input("Item Price? "))
                if price >= 0:
                    cart_items.append(item)
                    item_prices.append(price)
                    os.system("cls")
                    list_cart()
                    print(
                        f"'{item.title()} @ ${price:.2f}' was added to your cart.")
                else:
                    print(error_msg[0])
            except ValueError:
                print(error_msg[0])

    view_cart()
    return cart_items


def remove_item():
    item_delete = ""
    item = ""
    price = 0
    os.system("cls")
    list_cart()
    while item_delete != "done" and cart_items != []:
        print()
        item_delete = input(
            f"{len(cart_items)} items. Choose item number to REMOVE or [done]: ").lower()
        if item_delete != "done":
            try:
                if int(item_delete) <= int(len(cart_items)) and int(item_delete) > -1:
                    for i in range(len(cart_items)):
                        item = cart_items[i]
                        price = item_prices[i]
                        i += 1
                        if i == int(item_delete):
                            cart_items.remove(item)
                            item_prices.remove(price)
                            os.system("cls")
                            list_cart()
                            print(
                                f"'{item.title()} @ ${float(price):.2f}' was REMOVED from your cart.")
                            break
                else:
                    num_error()
            except ValueError:
                num_error()

    view_cart()
    return cart_items


def list_cart():
    if cart_items != []:
        print("Your shopping cart contents:")
        for i in range(len(cart_items)):
            print(
                f"{i + 1}. {cart_items[i].title():17} - ${item_prices[i]:.2f}")
        # for item in cart_items:
        #     print(item.title())
    else:
        print(error_msg[2])


def get_action_number():
    action_num = -1
    while action_num < 1 or action_num > 5:
        try:
            action_num = int(
                input("Please enter an action number (1-5): "))
        except ValueError:
            print()
            print(error_msg[1])
            print()
    return action_num


def view_cart():
    os.system("cls")
    list_cart()
    print()
    main()


def cart_total():
    total = sum(item_prices)
    os.system("cls")
    if cart_items == []:
        view_cart()
    else:
        list_cart()
        print(f"{'CART TOTAL:':20} - ${float(total):.2f}")
        print()
        main()


def quit():
    print()
    print("Thank you. Goodbye.")
    print()


def main():
    show_instructions()
    action = get_action_number()
    if action == 1:
        add_item()
    elif action == 2:
        view_cart()
    elif action == 3:
        remove_item()
    elif action == 4:
        cart_total()
    elif action == 5:
        quit()
    else:
        print()
        print(f"Error on action {action}!")
        quit()


# Call Menu App

os.system("cls")
print("Welcome to the Shopping Cart Program!")
main()
