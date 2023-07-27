import tkinter as tk

def on_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget to display the result and take input
entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and place buttons in a grid
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 20), padx=20, pady=10)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_click)

# Run the main event loop
root.mainloop()
