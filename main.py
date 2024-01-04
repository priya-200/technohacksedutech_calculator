import re
from tkinter import *


def calculate(eq):
    try:
        result = eval(eq)
        equation.delete(0, END)
        equation.insert(0, str(result))
    except Exception as e:
        equation.delete(0, END)
        equation.insert(0, str(e))


# Your button_click function could look like this:

def button_click(value):
    current_text = equation.get()
    if value == '=':
        calculate(current_text)
    else:
        equation.delete(0, END)
        equation.insert(0, current_text + str(value))


window = Tk()
window.title("Calculator")
window.config(padx=10, pady=10, bg="black")

equation = Entry(width=40, font=('Helvetica', 16), borderwidth=2, relief="solid", justify="right")
equation.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_value in buttons:
    btn = Button(text=button_value, bg="#D3D3D3", fg="black", font=('Helvetica', 12, 'bold'), width=5, height=2,
                 relief=FLAT,
                 command=lambda value=button_value: button_click(value))
    btn.grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
