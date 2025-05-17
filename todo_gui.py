import tkinter as tk
from tkinter import messagebox

FILENAME = "gui_todo.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(listbox.get(0, tk.END))
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks(listbox.get(0, tk.END))
    else:
        messagebox.showinfo("No Selection", "Please select a task to delete.")

# --- GUI Setup ---
root = tk.Tk()
root.title("📝 To-Do List (GUI Version)")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", width=15, command=add_task)
btn_add.pack(pady=2)

btn_delete = tk.Button(root, text="Delete Task", width=15, command=delete_task)
btn_delete.pack(pady=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Load tasks on startup
for task in load_tasks():
    listbox.insert(tk.END, task)

root.mainloop()
