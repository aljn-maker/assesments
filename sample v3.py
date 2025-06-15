import easygui as eg

# --------- User Data ---------
valid_users = {
    "alice": "pass123",
    "bob": "secure456"
}

def sign_up():
    while True:
        new_info = eg.multpasswordbox("Create a new account:", title="Sign Up", fields=["New Username", "New Password"])
        if new_info is None:
            return False  # User cancelled

        username, password = new_info
        username = username.strip().lower()

        if not username or not password:
            eg.msgbox("Username and password cannot be empty.", title="Sign Up Error")
        elif username in valid_users:
            eg.msgbox("That username is already taken. Please choose another.", title="Sign Up Error")
        else:
            valid_users[username] = password
            eg.msgbox(f"Account for '{username}' created successfully! You can now sign in.", title="Sign Up Success")
            return True

def login():
    attempts = 0
    while attempts < 3:
        login_info = eg.multpasswordbox("Please sign in to continue:", title="User Login",
                                        fields=["Username", "Password"])
        if login_info is None:
            return False  # User cancelled

        username, password = login_info
        username = username.strip().lower()

        if username in valid_users and valid_users[username] == password:
            eg.msgbox(f"Welcome, {username.title()}!", title="Login Successful")
            return True
        else:
            attempts += 1
            eg.msgbox("Incorrect username or password. Try again.", title="Login Failed")

    eg.msgbox("Too many failed attempts. Exiting...", title="Access Denied")
    return False

# --------- Shopping List Features ---------
shopping_list = []

allowed_clothing_items = [
    "t-shirt", "jeans", "jacket", "sweater", "dress", "shoes", "hat", "scarf",
    "graphic shirt", "polo shirt", "suit", "baggy pants", "jorts", "shorts"
]

def show_list():
    if not shopping_list:
        eg.msgbox("Your shopping list is empty.", title="Shopping List")
        return

    message = ""
    total = 0
    for i, item in enumerate(shopping_list, start=1):
        message += f"{i}. {item['item'].title()} - ${item['price']:.2f}\n"
        total += item['price']
    message += f"\nTotal: ${total:.2f}"
    eg.msgbox(message, title="Your Shopping List")

def add_item():
    item = eg.enterbox("Enter a clothing item to add:", title="Add Item")
    if not item:
        return

    item = item.strip().lower()
    if item not in allowed_clothing_items:
        eg.msgbox(f"'{item}' is not a valid clothing item.\n\n"
                  f"Allowed items: {', '.join(allowed_clothing_items)}", title="Invalid Item")
        return

    while True:
        price_input = eg.enterbox(f"Enter the price of '{item.title()}':", title="Item Price")
        if price_input is None:
            return

        try:
            price = float(price_input)
            if price < 0:
                eg.msgbox("Price cannot be negative.", title="Invalid Price")
            else:
                break
        except ValueError:
            eg.msgbox("Please enter a valid number for the price.", title="Invalid Input")

    shopping_list.append({"item": item, "price": price})
    eg.msgbox(f"'{item.title()}' for ${price:.2f} has been added to your shopping list.", title="Item Added")

def remove_item():
    if not shopping_list:
        eg.msgbox("Your shopping list is empty.", title="Remove Item")
        return

    choices = [f"{i + 1}. {item['item'].title()} - ${item['price']:.2f}" for i, item in enumerate(shopping_list)]
    choice = eg.choicebox("Select an item to remove:", choices=choices, title="Remove Item")
    if choice:
        index = choices.index(choice)
        removed = shopping_list.pop(index)
        eg.msgbox(f"Removed '{removed['item'].title()}' from your shopping list.", title="Item Removed")

def clear_list():
    if not shopping_list:
        eg.msgbox("Your shopping list is already empty.", title="Clear List")
        return

    if eg.ynbox("Are you sure you want to clear the entire shopping list?", title="Confirm Clear"):
        shopping_list.clear()
        eg.msgbox("Your shopping list has been cleared.", title="List Cleared")

def show_help():
    help_text = (
        "*How to use this Clothing Shopping List app:*\n\n"
        "• Add only clothing items from a predefined list\n"
        "• Each item must have a price (e.g. 19.99)\n"
        "• View your current list with total cost\n"
        "• You can remove items or clear the whole list\n\n"
        " Allowed items:\n"
        + ", ".join(allowed_clothing_items)
    )
    eg.msgbox(help_text, title="Help")

def shopping_menu():
    while True:
        choice = eg.buttonbox(
            "Welcome to your Clothing Shopping List!",
            choices=["Add Item", "Show List", "Remove Item", "Clear List", "Help", "Quit"],
            title="Shopping Menu"
        )

        if choice == "Add Item":
            add_item()
        elif choice == "Show List":
            show_list()
        elif choice == "Remove Item":
            remove_item()
        elif choice == "Clear List":
            clear_list()
        elif choice == "Help":
            show_help()
        elif choice == "Quit":
            eg.msgbox("Goodbye! Thanks for using the shopping list.", title="Exit")
            break

def main():
    while True:
        start_choice = eg.buttonbox(
            "🛒 Welcome! Please choose an option:",
            choices=["Sign In", "Sign Up", "Quit"],
            title="Start Menu"
        )

        if start_choice == "Sign In":
            if login():
                shopping_menu()
                break
        elif start_choice == "Sign Up":
            sign_up()
        elif start_choice == "Quit":
            eg.msgbox("Goodbye thankyou for using my program!!!", title="Exit")
            break

main()
