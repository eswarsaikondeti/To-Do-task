import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected_task = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected_task)
            listbox.insert(selected_task, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task, width=10, bg="lightgreen")
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(frame, text="Update Task", command=update_task, width=10, bg="lightblue")
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", command=delete_task, width=10, bg="tomato")
delete_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Run the app
root.mainloop()
