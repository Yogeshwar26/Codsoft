import tkinter as tk

# Constants
BACKGROUND_COLOR = "#2980b9"
BUTTON_COLOR = "#7DF9FF"
FONT_NAME = "Courier"
BUTTON_FONT_SIZE = 18
ENTRY_FONT_SIZE = 24

# Function to handle button press for expression values
def press(x):
    input_entry.insert(tk.END, str(x))

def clear():
    input_entry.delete(0, tk.END)

def evaluate():
    try:
        input_expression = input_entry.get()
        output = eval(input_expression)
        input_entry.delete(0, tk.END)
        input_entry.insert(0, f"{output:.2f}")
    except (SyntaxError, ZeroDivisionError):
        input_entry.delete(0, tk.END)
        input_entry.insert(0, "BAD EXPRESSION")

# Function to handle "Enter" key press event
def evaluate_on_enter(event):
    evaluate()

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry field for input
input_entry = tk.Entry(window, font=(FONT_NAME, ENTRY_FONT_SIZE))
input_entry.focus_set()
input_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=10, ipady=10, sticky="nsew")

# Define a custom style for buttons
button_style = {"font": (FONT_NAME, BUTTON_FONT_SIZE), "width": 4, "height": 2}

# Create a grid of buttons
button_grid = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("00", 4, 1), (".", 4, 2), ("+", 4, 3),
]

for text, row, col in button_grid:
    button = tk.Button(window, text=text, **button_style, command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
clear_button = tk.Button(window, text="CLEAR", font=(FONT_NAME, BUTTON_FONT_SIZE), width=10, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Evaluate button
equal_button = tk.Button(window, text="=", font=(FONT_NAME, BUTTON_FONT_SIZE), width=4, height=2, command=evaluate)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Event listener for "Enter" key to evaluate expression in input field
window.bind("<Return>", evaluate_on_enter)

# Configure the grid layout to be responsive
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


# Window configuration
window.config(bg=BACKGROUND_COLOR)
window.geometry("+575+125")
window.minsize(width=325, height=500)
window.resizable(False, False)

for widget in window.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(bg=BUTTON_COLOR, activebackground="#89CFF0")  # Change activebackground for hover effect

# Start the application
window.mainloop()
