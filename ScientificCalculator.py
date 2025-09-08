import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Scientific Calculator")
        self.root.config(bg="black")

        self.history_visible = False
        self.theme = "dark"

        self.entry = tk.Entry(
            root, font=("Arial", 18, "bold"),
            bg="black", fg="white", bd=8,
            width=22, justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=6, pady=10, padx=10)

        self.create_buttons()

        self.history_btn = tk.Button(
            root, text="History", width=10,
            bg="gray25", fg="white", activebackground="orange",
            font=("Arial", 12, "bold"),
            command=self.toggle_history
        )
        self.history_btn.grid(row=7, column=0, columnspan=3, pady=5)

        self.theme_btn = tk.Button(
            root, text="Light Mode", width=10,
            bg="gray25", fg="white", activebackground="orange",
            font=("Arial", 12, "bold"),
            command=self.toggle_theme
        )
        self.theme_btn.grid(row=7, column=3, columnspan=3, pady=5)

        self.history_list = []
        self.history_box = tk.Listbox(
            root, width=30, height=18,
            bg="black", fg="lightgreen",
            font=("Arial", 12), bd=5
        )
        self.scrollbar = tk.Scrollbar(root, command=self.history_box.yview)
        self.history_box.config(yscrollcommand=self.scrollbar.set)

        self.bind_keys()

        for i in range(1, 7):
            root.grid_rowconfigure(i, weight=1)
        for j in range(6):
            root.grid_columnconfigure(j, weight=1)

    def toggle_history(self):
        if self.history_visible:
            self.history_box.grid_forget()
            self.scrollbar.grid_forget()
            self.history_visible = False
            self.history_btn.config(text="History")
        else:
            self.history_box.grid(row=1, column=6, rowspan=6, padx=5, pady=5, sticky="ns")
            self.scrollbar.grid(row=1, column=7, rowspan=6, sticky="ns")
            self.history_visible = True
            self.history_btn.config(text="Hide History")

    def toggle_theme(self):
        if self.theme == "dark":
            self.theme = "light"
            bg, fg, entry_bg, entry_fg = "white", "black", "white", "black"
            btn_bg, btn_fg = "lightgray", "black"
            hist_bg, hist_fg = "white", "black"
            self.theme_btn.config(text="Dark Mode")
        else:
            self.theme = "dark"
            bg, fg, entry_bg, entry_fg = "black", "white", "black", "white"
            btn_bg, btn_fg = "gray20", "white"
            hist_bg, hist_fg = "black", "lightgreen"
            self.theme_btn.config(text="Light Mode")

        self.root.config(bg=bg)
        self.entry.config(bg=entry_bg, fg=entry_fg)

        for btn in self.root.grid_slaves():
            if isinstance(btn, tk.Button):
                if btn not in (self.history_btn, self.theme_btn):
                    btn.config(bg=btn_bg, fg=btn_fg)

        self.history_box.config(bg=hist_bg, fg=hist_fg)

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
                btn = tk.Button(
                    self.root, text=b, width=5, height=2,
                    bg="gray20", fg="white", activebackground="orange",
                    font=("Arial", 13, "bold"),
                    command=lambda val=b: self.click(val)
                )
                btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
                c += 1
            r += 1


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
