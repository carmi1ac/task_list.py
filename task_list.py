import tkinter as tk
from tkinter import messagebox
import pickle

#create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x520")

#create a listbox to display tasks
task_listbox = tk.Listbox(root, width=70, height=20)
task_listbox.pack(pady=20)

#Define functions to Add, Remove, and Save tasks
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

#Remove selected task function
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "No Task selected!")

#Save tasks to file function
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    messagebox.showinfo("Info", "Tasks saved successfully")

# Load Tasks from File (when app starts)
def load_tasks():
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass # If no file exists yet, just skip loading

# Create entry box and buttons for user interaction
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

# Load tasks when app starts
load_tasks()
root.mainloop()
