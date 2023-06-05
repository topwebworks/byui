import os

cart_items = []


# Functions

def show_instructions():
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total (Prices not added yet)")
    print("5. Quit")
    print()


def reset_main():
    os.system("cls")
    main()


def add_item():
    item = ""
    while item != "done":
        print()
        item = input("Add item? or [done]? ").lower()
        if item != "" and item != "done":
            cart_items.append(item)
            print(f"'{item}' has been added to your cart -> {cart_items}")
    reset_main()
    return cart_items


def remove_item():
    item = ""
    while item != "done":
        print()
        item = input("Remove item? or [done]? ").lower()
        if item != "" and item != "done":
            try:
                cart_items.remove(item)
                print(f"'{item}' has been removed from your cart -> {cart_items}")
            except ValueError:
                print('Item is not in the list.')
    reset_main()
    return cart_items


def get_action_number():
    action_num = -1
    while action_num < 1 or action_num > 5:
        try:
            action_num = int(
                input("Please enter an action number (1-5): "))
        except ValueError:
            print("Please input a number.")
            print()
    return action_num


def view_cart():
    os.system("cls")
    if cart_items != []:
        print("Your shopping cart contents:")
        for item in cart_items:
            print(item.capitalize())
    else:
        print("Your cart is empty.")
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
    elif action == 5:
        quit()
    else:
        print()
        print(f"Error on action {action}!")
        quit()


# Call Menu App

os.system("cls")
print()
print("Welcome to the Shopping Cart Program!")
main()
