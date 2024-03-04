import tkinter as tk
from tkinter import ttk
from math_expr import calc

def on_button_click(char):
    if char == '=':
        try:
            result = calc(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.set('Error')
    elif char == 'C':
        entry.delete(0, tk.END)
    else:
        current_text = entry.get()
        entry.set(current_text + char)


root = tk.Tk()
root.title('Calculator')

entry = tk.StringVar() # variable to keep track of the entry field

display = ttk.Entry(root, textvariable=entry, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='ew')

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for button in buttons:
    ans = ttk.Button(root, text=button, command=lambda button=button: on_button_click(button))
    ans.grid(row=buttons.index(button) // 4 + 1, column=buttons.index(button) % 4, sticky='nsew')

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()