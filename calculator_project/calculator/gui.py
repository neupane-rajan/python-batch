import tkinter as tk
from calculator.logic import CalculatorLogic
from calculator.buttons import buttons
from calculator.styles import *


class CalculatorGUI:

    def __init__(self):
        self.logic = CalculatorLogic()
        self.root = tk.Tk()
        self.root.title("calculator")
        self.root.geometry("350x500")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)
        self.input_text = tk.StringVar()
        self.create_display()
        self.create_buttons()

    def create_display(self):
        entry = tk.Entry(
            self.root,
            textvariable=self.input_text,
            font=("Arial", 26),
            bd=0,
            bg="#252525",
            fg="#ffffff",
            justify="right",
        )
        entry.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=15)

    def button_click(self, value):
        if value == "=":
            result = self.logic.calculate()
            self.input_text.set(result)

        elif value == "C":
            self.input_text.set(self.logic.clear())

        elif value == "<x]":
            self.input_text.set(self.logic.backspace())

        else:
            self.input_text.set(self.logic.add_to_expression(value))

    def create_buttons(self):
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(expand=True, fill="both")
        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=button,
                    font=FONT,
                    bg=BTN_COLOR,
                    fg=TEXT_COLOR,
                    bd=0,
                    activebackground="#555555",
                    command=lambda value=button: self.button_click(value),
                )
                btn.grid(
                    row=row_index,
                    column=col_index,
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )
            for i in range(5):
                frame.grid_rowconfigure(i, weight=1)

            for i in range(4):
                frame.grid_columnconfigure(i, weight=1)

    def run(self):
        self.root.mainloop()
