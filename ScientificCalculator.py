import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Scientific Calculator")
        self.root.geometry("720x500+100+100")
        self.root.config(bg="black")

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 20, "bold"), bg="black", fg="white", bd=10, width=32, justify="right")
        self.entry.grid(row=0, column=0, columnspan=8, pady=10)

        # Buttons layout
        self.create_buttons()

