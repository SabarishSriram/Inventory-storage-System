import tkinter as tk
from tkinter import messagebox


class OnlineShoppingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Shopping Inventory System")
        self.root.geometry("425x1100")

        # Apply gradient background
        self.bg_color = "#f0f0f0"
        self.bg_color2 = "#e0e0e0"
        self.root.configure(bg=self.bg_color)

        self.food_items = {
            "Apple": 200,
            "Banana": 80,
            "Orange": 130,
            "Bread": 40,
            "Rice": 120,
            "Pasta": 60,
            "Milk": 30,
            "Cheese": 15,
            "Ice cream": 45,
            "Tomato": 30,
            "Potato": 20,
            "Bottled water": 10,
            "Coffee": 15,
            "Tea": 15,
        }
        self.cart = {}

        self.product_label = tk.Label(root, text="Food Items", font=("Arial", 14, "bold"), bg=self.bg_color)
        self.product_label.grid(row=0, column=0, columnspan=2, pady=10)

        row_index = 1
        col_index = 0
        for item, price in self.food_items.items():
            product_button = tk.Button(root, text=f"{item} - ${price:.2f}", 
                                       font=("Arial", 12, "bold"),
                                       bg="#7404c4", fg="white",
                                       command=lambda i=item, p=price: self.add_to_cart(i, p))
            product_button.grid(row=row_index, column=col_index, padx=10, pady=5, sticky="we")
            col_index += 1
            if col_index > 1:
                col_index = 0
                row_index += 1

            # Apply curved button style
            product_button.config(borderwidth=0, relief=tk.FLAT, bd=0, 
                                  highlightbackground=self.bg_color2, highlightcolor=self.bg_color2, 
                                  highlightthickness=2, pady=8, padx=15, 
                                  activebackground="#4202a8", activeforeground="white")
            
        self.cart_label = tk.Label(root, text="Cart", font=("Arial", 14, "bold"), bg=self.bg_color)
        self.cart_label.grid(row=row_index, column=0, columnspan=2, pady=10)

        row_index += 1
        self.cart_listbox = tk.Listbox(root, width=40, height=9, font=("Arial", 12))
        self.cart_listbox.grid(row=row_index, column=0, columnspan=2, pady=1)

        row_index += 1
        self.checkout_button = tk.Button(root, text="Checkout", 
                                         font=("Arial", 12, "bold"), bg="#00EBCB", fg="white",
                                         command=self.checkout)
        self.checkout_button.grid(row=row_index, column=0, columnspan=2, pady=10)

    def add_to_cart(self, item, price):
        if item in self.cart:
            self.cart[item] += price
        else:
            self.cart[item] = price
        self.update_cart_display()
        
    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        for item, price in self.cart.items():
            self.cart_listbox.insert(tk.END, f"{item} - ${price:.2f}")

    def checkout(self):
        total_price = sum(self.cart.values())
        messagebox.showinfo("Checkout", f"Total Price: ${total_price:.2f}")
        self.cart.clear()
        self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShoppingSystem(root)
    root.mainloop()
