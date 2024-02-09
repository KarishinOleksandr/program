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