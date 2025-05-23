import easygui as eg

# Shopping list stores item name and price
shopping_list = []

# Allowed clothing items
allowed_clothing_items = [
    "t-shirt", "jeans", "jacket", "sweater", "dress", "shoes", "hat", "scarf",
    "graphic shirt", "polo shirt", "suit", "baggy pants", "jorts", "shorts"
]

# Show the list with prices
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

# Add an item
def add_item():
    item = eg.enterbox("Enter clothing item to add:", title="Add Item")
    if item:
        item = item.strip().lower()
        if item in allowed_clothing_items:
            try:
                price = eg.enterbox(f"Enter the price of '{item}':", title="Item Price")
                if price:
                    price = float(price)
                    shopping_list.append({"item": item, "price": price})
                    eg.msgbox(f"'{item.title()}' for ${price:.2f} has been added.", title="Item Added")
            except ValueError:
                eg.msgbox("Invalid price entered.", title="Error")
        else:
            eg.msgbox(f"'{item}' is not a valid clothing item.", title="Invalid Item")

# Remove an item
def remove_item():
    if not shopping_list:
        eg.msgbox("Your shopping list is empty.", title="Remove Item")
        return
    choices = [f"{i + 1}. {item['item'].title()} - ${item['price']:.2f}" for i, item in enumerate(shopping_list)]
    choice = eg.choicebox("Select an item to remove:", choices=choices, title="Remove Item")
    if choice:
        index = choices.index(choice)
        removed = shopping_list.pop(index)
        eg.msgbox(f"Removed '{removed['item'].title()}' from the list.", title="Item Removed")

# Clear the list
def clear_list():
    if shopping_list:
        if eg.ynbox("Are you sure you want to clear the entire shopping list?", title="Clear List"):
            shopping_list.clear()
            eg.msgbox("Shopping list cleared.", title="Cleared")
    else:
        eg.msgbox("Your shopping list is already empty.", title="Clear List")

# Main menu loop
def main():
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
            eg.msgbox(
                "This program helps you keep track of clothing items you want to buy.\n\n"
                "- Add only clothing items from a preset list\n"
                "- View the current list with total cost\n"
                "- Remove items or clear the list\n"
                "- Prices must be numbers like 19.99",
                title="Help"
            )
        elif choice == "Quit":
            eg.msgbox("Goodbye! Thanks for using the shopping list.", title="Exit")
            break

main()
