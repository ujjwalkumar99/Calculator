import tkinter as tk

def on_button_click(event):
    # Handle button click event
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        if entry_var.get() == "0":
            entry_var.set(button_text)
        else:
            entry_var.set(entry_var.get() + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.configure(bg="#1f1f1f")  # Set dark background color

# Entry widget to display and input calculations
entry_var = tk.StringVar()
entry_var.set("0")  # Set initial placeholder text
entry = tk.Entry(root, textvar=entry_var, font="Helvetica 24 bold", bd=10, insertwidth=4, width=15, justify="right", bg="#2c2c2c", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Create buttons
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("(", ")", "^", "=")
]

# Add buttons to the calculator
for i in range(5):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font="Helvetica 20 bold", padx=20, pady=20, bd=0, bg="#000000", fg="#ffffff")
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", on_button_click)

# Configure column and row weights to expand the buttons
for i in range(5):
    root.grid_rowconfigure(i+1, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main loop
root.mainloop()
