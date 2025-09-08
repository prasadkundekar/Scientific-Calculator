import tkinter as tk
from tkinter import ttk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Scientific Calculator")
        self.root.geometry("650x520+200+100")
        self.theme = "dark"
        self.history_visible = False

        # Custom style
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Rounded.TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            borderwidth=0,
            relief="flat",
            foreground="white",
            background="#2d2d2d"
        )
        style.map(
            "Rounded.TButton",
            background=[("active", "#ff9500")],
            foreground=[("active", "black")]
        )

        # Entry field
        self.entry = tk.Entry(
            root, font=("Arial", 20, "bold"),
            bg="black", fg="white", bd=6,
            width=25, justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=6, pady=10, padx=10)

        # Buttons layout
        self.create_buttons()

        # History button
        self.history_btn = ttk.Button(
            root, text="📜 History", style="Rounded.TButton",
            command=self.toggle_history
        )
        self.history_btn.grid(row=7, column=0, columnspan=3, pady=8, sticky="nsew")

        # Theme toggle button
        self.theme_btn = ttk.Button(
            root, text="🌙 Light Mode", style="Rounded.TButton",
            command=self.toggle_theme
        )
        self.theme_btn.grid(row=7, column=3, columnspan=3, pady=8, sticky="nsew")

        # History panel
        self.history_list = []
        self.history_box = tk.Listbox(
            root, width=28, height=18,
            bg="black", fg="lightgreen",
            font=("Arial", 12), bd=5
        )
        self.scrollbar = tk.Scrollbar(root, command=self.history_box.yview)
        self.history_box.config(yscrollcommand=self.scrollbar.set)

        # Keyboard bindings
        self.bind_keys()

        # Expand grid cells equally
        for i in range(1, 8):
            root.grid_rowconfigure(i, weight=1)
        for j in range(6):
            root.grid_columnconfigure(j, weight=1)

    def toggle_history(self):
        if self.history_visible:
            self.history_box.grid_forget()
            self.scrollbar.grid_forget()
            self.history_visible = False
            self.history_btn.config(text="📜 History")
        else:
            self.history_box.grid(row=1, column=6, rowspan=6, padx=5, pady=5, sticky="ns")
            self.scrollbar.grid(row=1, column=7, rowspan=6, sticky="ns")
            self.history_visible = True
            self.history_btn.config(text="❌ Hide History")

    def toggle_theme(self):
        if self.theme == "dark":
            self.theme = "light"
            self.root.config(bg="white")
            self.entry.config(bg="white", fg="black")
            self.history_box.config(bg="white", fg="black")
            self.theme_btn.config(text="🌑 Dark Mode")
        else:
            self.theme = "dark"
            self.root.config(bg="black")
            self.entry.config(bg="black", fg="white")
            self.history_box.config(bg="black", fg="lightgreen")
            self.theme_btn.config(text="🌙 Light Mode")

    def click(self, val):
        expression = self.entry.get()
        try:
            if val == "C":
                self.entry.delete(len(expression) - 1, tk.END)
            elif val == "CE":
                self.entry.delete(0, tk.END)
            elif val == "=":
                result = eval(expression)
                self.show_result(result)
                self.add_to_history(expression, result)
            elif val == "√":
                self.show_result(math.sqrt(eval(expression)))
            elif val == "x²":
                self.show_result(eval(expression) ** 2)
            elif val == "x³":
                self.show_result(eval(expression) ** 3)
            elif val == "xʸ":
                self.entry.insert(tk.END, "**")
            elif val == "π":
                self.entry.insert(tk.END, str(math.pi))
            elif val == "e":
                self.entry.insert(tk.END, str(math.e))
            elif val == "sin":
                self.show_result(math.sin(math.radians(eval(expression))))
            elif val == "cos":
                self.show_result(math.cos(math.radians(eval(expression))))
            elif val == "tan":
                self.show_result(math.tan(math.radians(eval(expression))))
            elif val == "sinh":
                self.show_result(math.sinh(eval(expression)))
            elif val == "cosh":
                self.show_result(math.cosh(eval(expression)))
            elif val == "tanh":
                self.show_result(math.tanh(eval(expression)))
            elif val == "log":
                self.show_result(math.log10(eval(expression)))
            elif val == "ln":
                self.show_result(math.log(eval(expression)))
            elif val == "x!":
                self.show_result(math.factorial(eval(expression)))
            elif val == "deg":
                self.show_result(math.degrees(eval(expression)))
            elif val == "rad":
                self.show_result(math.radians(eval(expression)))
            else:
                self.entry.insert(tk.END, val)
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def show_result(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)

    def add_to_history(self, expression, result):
        calc = f"{expression} = {result}"
        self.history_list.append(calc)
        if len(self.history_list) > 20:
            self.history_list.pop(0)
        self.update_history_box()

    def update_history_box(self):
        self.history_box.delete(0, tk.END)
        for item in self.history_list:
            self.history_box.insert(tk.END, item)

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.click("="))
        self.root.bind("<BackSpace>", lambda event: self.click("C"))
        self.root.bind("<Escape>", lambda event: self.click("CE"))
        for key in "0123456789+-*/().%":
            self.root.bind(key, lambda event, val=key: self.click(val))

    def create_buttons(self):
        buttons = [
            ["C", "CE", "(", ")", "√", "x²"],
            ["7", "8", "9", "/", "sin", "cos"],
            ["4", "5", "6", "*", "tan", "log"],
            ["1", "2", "3", "-", "ln", "x!"],
            ["0", ".", "=", "+", "π", "e"],
            ["x³", "xʸ", "deg", "rad", "sinh", "cosh"]
        ]

        r = 1
        for row in buttons:
            c = 0
            for b in row:
                btn = ttk.Button(
                    self.root, text=b,
                    style="Rounded.TButton",
                    command=lambda val=b: self.click(val)
                )
                btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")
                c += 1
            r += 1


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
