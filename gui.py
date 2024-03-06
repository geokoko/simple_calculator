import tkinter as tk
from tkinter import ttk
from math_expr import calc

def on_button_click(char):
    if char == '=':
        try:
            result = calc(entry.get())
            entry.set(int(result) if result.is_integer() else round(result, 9))
        except:
            entry.set('Error')
    elif char == 'C':
        entry.set('')
    elif char == 'Del':
        entry.set(entry.get()[:-1])
    else:
        current_text = entry.get()
        entry.set(current_text + char)


root = tk.Tk()
root.title('Calculator')

entry = tk.StringVar() # variable to keep track of the entry field

display = ttk.Entry(root, textvariable=entry, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew')

buttons = [
    'Del', '(', ')', 'mod', '^',
    '7', '8', '9', '+', '√',
    '4', '5', '6', '-', 'x²',
    '1', '2', '3', '*', '=',
    '0', '.', '%', '/', 'C'
]

for button in buttons:
    if button == 'Del':
        btn = tk.Button(root, text=button, fg="white", bg="red", activeforeground="red", activebackground="white", command=lambda char=button: on_button_click(char))
    elif button == 'C':
        btn = tk.Button(root, text=button, fg="white", bg="red", activeforeground="red", activebackground="white", command=lambda char=button: on_button_click(char))
    elif button == '=':
        btn = tk.Button(root, text=button, fg="white", bg="green", activeforeground="green", activebackground="white", command=lambda char=button: on_button_click(char))
    else:
        btn = tk.Button(root, text=button, fg="white", bg="grey", activeforeground="grey", activebackground="white", command=lambda char=button: on_button_click(char))
    btn.grid(row=buttons.index(button) // 5 + 1, column=buttons.index(button) % 5, sticky='nsew', ipadx=10, ipady=10)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()