import easygui as eg  # This lets us use easy pop-up windows

#A list to store all shopping items
shopping_list = []

#Only these items are allowed to be added
allowed_clothes = [
    "t-shirt", "jeans", "jacket", "sweater", "dress", "shoes", "hat", "scarf"
]

# Show all items in the list with total price
def show_items():
    if not shopping_list:  # If list is empty
        eg.msgbox("Your shopping list is empty.", title="Shopping List")
        return

    message = ""
    total = 0
    for i, item in enumerate(shopping_list, start=1):
        message += f"{i}. {item['name'].title()} - ${item['price']:.2f}\n"
        total += item['price']

    message += f"\nTotal: ${total:.2f}"
    eg.msgbox(message, title="Your Shopping List")

# Add a new clothing item
def add_new_item():
    item_name = eg.enterbox("Enter a clothing item to add:", title="Add Item")
    if item_name:
        item_name = item_name.strip().lower()
        if item_name in allowed_clothes:
            price_input = eg.enterbox(f"Enter the price for '{item_name}':", title="Enter Price")
            if price_input:
                try:
                    item_price = float(price_input)
                    shopping_list.append({"name": item_name, "price": item_price})
                    eg.msgbox(f"{item_name.title()} added for ${item_price:.2f}", title="Item Added")
                except ValueError:
                    eg.msgbox("Please enter a valid number for the price.", title="Invalid Input")
        else:
            eg.msgbox("That is not a valid clothing item.", title="Not Allowed")

# Remove an item from the list
def remove_item():
    if not shopping_list:
        eg.msgbox("Your shopping list is empty.", title="Remove Item")
        return

    item_choices = [f"{i + 1}. {item['name'].title()} - ${item['price']:.2f}" for i, item in enumerate(shopping_list)]
    selected = eg.choicebox("Pick an item to remove:", choices=item_choices, title="Remove Item")

    if selected:
        index = item_choices.index(selected)
        removed_item = shopping_list.pop(index)
        eg.msgbox(f"Removed {removed_item['name'].title()} from the list.", title="Item Removed")

#Clear all items
def clear_list():
    if not shopping_list:
        eg.msgbox("Your shopping list is already empty.", title="Nothing to Clear")
    else:
        confirm = eg.ynbox("Are you sure you want to clear the entire list?", title="Confirm Clear")
        if confirm:
            shopping_list.clear()
            eg.msgbox("The shopping list has been cleared.", title="List Cleared")

#This runs the main menu loop
def run_shopping_program():
    while True:
        user_choice = eg.buttonbox(
            "What would you like to do?",
            choices=["Add Item", "Show List", "Remove Item", "Clear List", "Help", "Quit"],
            title="Clothing Shopping List"
        )

        if user_choice == "Add Item":
            add_new_item()
        elif user_choice == "Show List":
            show_items()
        elif user_choice == "Remove Item":
            remove_item()
        elif user_choice == "Clear List":
            clear_list()
        elif user_choice == "Help":
            eg.msgbox(
                "This is a simple clothing shopping list.\n\n"
                "- You can only add clothes from a set list.\n"
                "- Enter a price for each item.\n"
                "- You can see your total and remove items.\n"
                "- All input is done with buttons and boxes!",
                title="Help"
            )
        elif user_choice == "Quit":
            eg.msgbox("Thanks for using the shopping list!", title="Goodbye")
            break

# Start the program
run_shopping_program()
