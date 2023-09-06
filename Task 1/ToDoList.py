import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_task():
    task = entry.get()
    time = time_entry.get()
    if task:
        if time:
            task += f" (at {time})"
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        time = time_entry.get()
        if updated_task:
            if time:
                updated_task += f" (at {time})"
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

def mark_as_done():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        updated_task = task + " (Done)"
        listbox.delete(index)
        listbox.insert(index, updated_task)
        listbox.itemconfig(index, {'fg': 'black'})
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

window = tk.Tk()
window.title("To-Do List")

primary_color = "#1976D2"
secondary_color = "#BBDEFB"

window.configure(bg=secondary_color)

listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)

scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, font=("Arial", 12), highlightbackground=secondary_color)
entry.pack(pady=10)

time_label = tk.Label(window, text="Time (optional):", font=("Arial", 12), bg=secondary_color)
time_label.pack()
time_entry = tk.Entry(window, font=("Arial", 12), highlightbackground=secondary_color)
time_entry.pack()

style = ttk.Style()
style.configure("TButton", padding=5, background=primary_color, foreground="white")



style.configure("MarkDone.TButton", padding=5, background=primary_color, foreground="black")


add_button = ttk.Button(window, text="Add Task", command=add_task, style="MarkDone.TButton")
add_button.pack(pady=10)

delete_button = ttk.Button(window, text="Delete Task", command=delete_task, style="MarkDone.TButton")
delete_button.pack(pady=10)

update_button = ttk.Button(window, text="Update Task", command=update_task, style="MarkDone.TButton")
update_button.pack(pady=10)

mark_done_button = ttk.Button(window, text="Mark as Done", command=mark_as_done, style="MarkDone.TButton")
mark_done_button.pack(pady=10)

window.mainloop()
