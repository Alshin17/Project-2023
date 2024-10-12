import tkinter as tk
from tkinter import messagebox, StringVar

# Grocery items data
grocery_items = {
    "Rice": {"price": 40, "quantity": 100},
    "Wheat": {"price": 35, "quantity": 100},
    "Sugar": {"price": 50, "quantity": 100},
    "Salt": {"price": 20, "quantity": 100},
    "Milk": {"price": 60, "quantity": 50},
    "Eggs": {"price": 5, "quantity": 200},
    "Tea": {"price": 300, "quantity": 50},
    "Coffee": {"price": 400, "quantity": 50},
    "Oil": {"price": 150, "quantity": 40},
    "Pulses": {"price": 90, "quantity": 80},
    "Butter": {"price": 250, "quantity": 30},
    "Cheese": {"price": 300, "quantity": 30}
}

cart = {}
user_name = ""
user_phone = ""

def update_inventory_display():
    """Refreshes the inventory display."""
    inventory_text.delete(1.0, tk.END)
    for item, details in grocery_items.items():
        inventory_text.insert(tk.END, f"{item}: Rs {details['price']} per kg (Available: {details['quantity']} kg)\n")

def add_to_cart(item):
    """Adds the selected item and its quantity to the cart."""
    try:
        quantity = int(quantity_entry.get())
        if item in grocery_items and quantity <= grocery_items[item]["quantity"]:
            cart[item] = cart.get(item, {"price": grocery_items[item]["price"], "quantity": 0})
            cart[item]["quantity"] += quantity
            grocery_items[item]["quantity"] -= quantity
            messagebox.showinfo("Success", f"{quantity} kg of {item} added to cart!")
            update_inventory_display()
        else:
            messagebox.showerror("Error", "Not enough stock or invalid quantity!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")

def view_cart():
    """Displays the current items in the cart and total bill."""
    if not cart:
        messagebox.showinfo("Cart", "Your cart is empty.")
        return

    cart_window = tk.Toplevel(window)
    cart_window.title("Your Cart")
    cart_window.configure(bg="#F1F8E9")

    tk.Label(cart_window, text="Your Cart", font=("Arial", 14, "bold"), bg="#F1F8E9").pack(pady=10)

    total_cost = sum(details["price"] * details["quantity"] for details in cart.values())
    for item, details in cart.items():
        item_cost = details["price"] * details["quantity"]
        tk.Label(cart_window, text=f"{item}: {details['quantity']} kg @ Rs {details['price']} per kg = Rs {item_cost}",
                 font=("Arial", 12), bg="#F1F8E9").pack()

    tk.Label(cart_window, text=f"Total Bill: Rs {total_cost}", font=("Arial", 14, "bold"), bg="#F1F8E9").pack(pady=10)

def submit_details():
    """Collects user details and initializes the main interface."""
    global user_name, user_phone
    user_name = user_name_entry.get()
    user_phone = user_phone_entry.get()
    
    if user_name and user_phone:
        user_details_frame.pack_forget()  # Hide user details frame
        main_frame.pack(pady=10)          # Show main frame
        messagebox.showinfo("Welcome", f"Welcome, {user_name}!")
        update_inventory_display()
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

# Main window setup
window = tk.Tk()
window.title("Grocery Management System")
window.geometry("500x600")
window.configure(bg="#FFF3E0")

# User details frame
user_details_frame = tk.Frame(window, bg="#E0F7FA")
user_details_frame.pack(pady=20)

tk.Label(user_details_frame, text="Enter your details", font=("Arial", 16, "bold"), bg="#E0F7FA").pack(pady=20)
tk.Label(user_details_frame, text="Name:", font=("Arial", 12), bg="#E0F7FA").pack()
user_name_entry = tk.Entry(user_details_frame)
user_name_entry.pack(pady=5)

tk.Label(user_details_frame, text="Phone Number:", font=("Arial", 12), bg="#E0F7FA").pack()
user_phone_entry = tk.Entry(user_details_frame)
user_phone_entry.pack(pady=5)

tk.Button(user_details_frame, text="Submit", command=submit_details, bg="#0288D1", fg="white").pack(pady=20)

# Main frame
main_frame = tk.Frame(window, bg="#FFF3E0")

# Inventory display
inventory_text = tk.Text(main_frame, height=15, width=60, bg="#FFF3E0", font=("Arial", 10))
inventory_text.pack(pady=10)

# Quantity entry
tk.Label(main_frame, text="Select item and quantity to add to cart", font=("Arial", 12, "bold"), bg="#FFF3E0").pack(pady=10)

item_choice = StringVar(main_frame)
item_choice.set("Select an item")
item_dropdown = tk.OptionMenu(main_frame, item_choice, *grocery_items.keys())
item_dropdown.pack()

tk.Label(main_frame, text="Quantity (in kg):", font=("Arial", 12), bg="#FFF3E0").pack()
quantity_entry = tk.Entry(main_frame)
quantity_entry.pack(pady=5)

add_button = tk.Button(main_frame, text="Add to Cart", command=lambda: add_to_cart(item_choice.get()), bg="#42A5F5", fg="white")
add_button.pack(pady=10)

view_cart_button = tk.Button(main_frame, text="View Cart and Bill", command=view_cart, bg="#8BC34A", fg="white")
view_cart_button.pack(pady=10)

exit_button = tk.Button(main_frame, text="Exit", command=window.quit, bg="#BDBDBD", fg="white")
exit_button.pack(pady=20)

window.mainloop()

