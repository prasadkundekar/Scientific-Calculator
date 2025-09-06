import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Scientific Calculator")
        self.root.geometry("720x500+100+100")
        self.root.config(bg="black")

        self.entry = tk.Entry(root, font=("Arial", 20, "bold"), bg="black", fg="white", bd=10, width=32, justify="right")
        self.entry.grid(row=0, column=0, columnspan=8, pady=10)

        self.create_buttons()

    def click(self, val):
        expression = self.entry.get()
        try:
            if val == "C":  # Clear last character
                self.entry.delete(len(expression) - 1, tk.END)

            elif val == "CE":  # Clear all
                self.entry.delete(0, tk.END)

            elif val == "=":  # Evaluate
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)

            elif val == "√":
                self.show_result(math.sqrt(eval(expression)))

            elif val == "x²":
                self.show_result(eval(expression) ** 2)

            elif val == "x³":
                self.show_result(eval(expression) ** 3)

            elif val == "xʸ":
                self.entry.insert(tk.END, "**")

            elif val == "π":
                self.show_result(math.pi)

            elif val == "e":
                self.show_result(math.e)

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

    def create_buttons(self):
        buttons = [
            ["C", "CE", "(", ")", "√", "x²", "x³", "xʸ"],
            ["7", "8", "9", "/", "sin", "cos", "tan", "π"],
            ["4", "5", "6", "*", "sinh", "cosh", "tanh", "e"],
            ["1", "2", "3", "-", "log", "ln", "x!", "%"],
            ["0", ".", "=", "+", "deg", "rad"]
        ]

        r = 1
        for row in buttons:
            c = 0
            for b in row:
                btn = tk.Button(
                    self.root, text=b, width=6, height=2,
                    bg="black", fg="white", font=("Arial", 16, "bold"),
                    command=lambda val=b: self.click(val)
                )
                btn.grid(row=r, column=c, padx=2, pady=2)
                c += 1
            r += 1


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
