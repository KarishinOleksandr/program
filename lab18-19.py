from tkinter import *

def f():
    label_data["text"] = "Вас звуть - %s" % entry_name.get()

root = Tk()

name = Label(root, text= "Введіть ваше ім'я: ")
name.pack()

entry_name = Entry(root)
entry_name.pack(pady = 10)

button_get = Button(root, text = "Згенерувати", command=f)
button_get.pack()

label_data = Label(root, text = "Вас звуть - ___" , fg = "green")
label_data.pack(side=LEFT, pady=10)

root.title("My app")
root.mainloop()

from tkinter import *

def calc():
    try:
        n = int(entry.get())
        sum_formula = " + ".join(str(i) for i in range(1, n + 1))
        result = sum(range(1, n + 1))
        result_label_var.set(f"Sum({n}) = {sum_formula} = {result}")
    except ValueError:
        result_label_var.set("Please enter a valid integer.")

root = Tk()
root.title("My app")

label = Label(root, text="Enter an integer N:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = Button(root, text="Calculate Sum", command=calc)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label_var = StringVar()
result_label = Label(root, textvariable=result_label_var)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

from tkinter import *

def privedstvie():
    label_data["text"] = "Welcome %s !" % entry_n.get()

root = Tk()
root.title("My app")

left_label = Label(root, text = "Enter your name: ")
left_label.grid(row=0, column=0, pady=10, padx=10)

entry_n = Entry(root)
entry_n.grid(row=0, column=1, pady=10, padx=10)

button1 = Button(root, text="Validate", command=privedstvie)
button1.grid(row=1, column=1,  pady=10, padx=10)

label_data = Label(root)
label_data.grid(row=2, column=1,  pady=10, padx=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def new():
    messagebox.showinfo("New")

def open():
    messagebox.showinfo("Open")

def exit():
    root.destroy()

def cut():
    messagebox.showinfo("Cut")

def copy():
    messagebox.showinfo("Copy")

def paste():
    messagebox.showinfo("Paste")

def about():
    messagebox.showinfo("About")

root = tk.Tk()
root.title("My app")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Python", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()

import tkinter as tk
from tkinter import *

root = Tk()
root.title("my app")

n = tk.StringVar()
n.set("1")

def right():
    now =   int(n.get())
    n.set( now + 1)

def left():
    now =   int(n.get())
    n.set( now  - 1)


root.rowconfigure(0, minsize=50, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)

left_button = Button(root, text="-", command=left)
left_button.grid(row=0, column=0)

mid_label = Label(root, textvariable = n)
mid_label.grid(row=0, column=1)

right_button = Button(root, text="+", command=right)
right_button.grid(row=0, column=2)

root.mainloop()