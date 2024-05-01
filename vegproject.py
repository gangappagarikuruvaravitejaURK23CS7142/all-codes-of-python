import tkinter as tk
from tkinter import ttk

class VegetableShop:
    def _init_(self, master):
        self.master = master
        self.master.title("Vegetable Shop")
        
        # List of vegetables and their prices
        self.vegetables = {
            'Carrot': 2,
            'Tomato': 3,
            'Cucumber': 1.5,
            'Spinach': 2.5,
            'Bell Pepper': 4,
            'Brinjal':3,
            'onion':2,
            'Beetroot':4
            
        }
        
        # Variables to store selected vegetable and quantity
        self.selected_vegetable = tk.StringVar()
        self.quantity = tk.IntVar()
        
        # Creating UI elements
        tk.Label(master, text="Select Vegetable:").grid(row=0, column=0, padx=5, pady=5)
        self.vegetable_combo = ttk.Combobox(master, textvariable=self.selected_vegetable, state='readonly')
        self.vegetable_combo['values'] = list(self.vegetables.keys())
        self.vegetable_combo.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(master, text="Select Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_spinbox = tk.Spinbox(master, from_=1, to=10, textvariable=self.quantity)
        self.quantity_spinbox.grid(row=1, column=1, padx=5, pady=5)
        
        self.add_button = tk.Button(master, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.cart_label = tk.Label(master, text="Your Cart:")
        self.cart_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.cart_listbox = tk.Listbox(master)
        self.cart_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def add_to_cart(self):
        vegetable = self.selected_vegetable.get()
        quantity = self.quantity.get()
        price = self.vegetables.get(vegetable, 0)
        total_price = price * quantity
        
        self.cart_listbox.insert(tk.END, f"{quantity} {vegetable}(s) - ${total_price:.2f}")

# Create Tkinter root window
root = tk.Tk()
# Create an instance of the VegetableShop class
app = VegetableShop(root)
# Run the Tkinter event loop
root.mainloop()