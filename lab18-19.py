##Написати програму, яка запитує у користувача ім’я і виводить його після натиснення кнопки у відповідній текстовій мітці. 

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

##Написати програму, яка використовуючи бібліотеку Tkinter, просить користувача увести ціле число  N та у мітці виводить значення суми послідовності "1 + 2 + ... + N" в наступному форматі

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

##Створіть програму на Python за допомогою бібліотеки Tkinter, яка відображає діалогове вікно, у якому користувача просять ввести своє ім’я, і виводять вітальне повідомлення у наступному форматі

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

##Напишіть програму на Python, яка створює базову панель меню з пунктами меню за допомогою Tkinter. Меню пункту File – New, Open, Exit. Для візуального відділення пункту Exit використовуйте команду 

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

##Створити програму за зразком, яка залежно від натискання кнопки збільшує або зменшує з кроком 1 значення в мітці. Початкове значення мітки  1. 

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

##Створити додаток, у якому можна перевести долари чи євро у гривні.

import tkinter as tk

def update_currence():
    selected_currency = currence.get()

    if selected_currency == "USD":
        thirthd_label.config(text="38")
    elif selected_currency == "Euro":
        thirthd_label.config(text="40")

def converd():
    selected_currency = currence.get()
    amount = int(first_enter.get())

    if selected_currency == "USD":
        result = amount * 38
    elif selected_currency == "Euro":
        result = amount * 40

    last_label.config(text = result)    


root = tk.Tk()
root.title("My app")

currence = tk.StringVar()

first_label = tk.Label(root, text = "Виберіть валюту")
first_label.grid(row = 0, column = 0)

radio_usd = tk.Radiobutton(root, text="Долар США", variable=currence, value="USD", command=update_currence)
radio_usd.grid(row= 0, column= 1)

radio_euro = tk.Radiobutton(root, text = "Євро",variable=currence , value= "Euro", command=update_currence)
radio_euro.grid(row= 1, column= 1)

second_label = tk.Label(root, text = "Курс")
second_label.grid(row = 2, column = 0)

thirthd_label = tk.Label(root, text = "" )
thirthd_label.grid(row=2, column=1)

fourth_label = tk.Label(root, text="Введіть суму у валюті: ")
fourth_label.grid(row = 3, column=0)

first_enter = tk.Entry(root)
first_enter.grid(row = 3, column = 1)

one_button = tk.Button(root, text = "Конвертувати", command=converd)
one_button.grid(row = 4, column = 0)

last_label = tk.Label(root, text="", fg="red")
last_label.grid(row = 4, column = 1)

root.mainloop()

##Створити програму-гру: комп'ютер загадує число від 1 до 100, гравець намагається відгадати його та записує у текстове поле відповідь; програма повинна рахувати кількість спроб та робити підказку користувачеві, виводячи повідомлення "число менше", чи "число більше"; коли число відгадане, вказати кількість спроб, за яку це вдалося зробити гравцю.

import random 
import tkinter as tk
from tkinter import *

min = 1
max =100

def guess():
    try:    
        global math, count
        number = int(first_enter.get())
        
        if math == number:
            count += 1
            third_label["text"] = f"УРААА ПЕРЕМОГА БУДЕ!!! Кількість спроб: {count}"
        elif math > number:
            count += 1
            third_label["text"] = "Гаряче, число більше"
        else:
            count += 1
            third_label["text"] = "Холодно, число менше"
    except ValueError:
        third_label["text"] = "Введіть число"        

def generate_number():
    global math, count
    math = random.randint(min, max)
    count = 0
    third_label["text"] = "Нове число згенеровано"

root = tk.Tk()
root.title("my app")

first_label = tk.Label(root, text = "Вгадайте число від 1 до 100")
first_label.grid(row = 0, column = 0, columnspan=2)

second_label = tk.Label(root, text = "Ваш варіант")
second_label.grid(row=1, column=0)

first_enter = tk.Entry(root)
first_enter.grid(row =1, column=1)
math = random.randint(min, max)

third_label = tk.Label(root, text="")
third_label.grid(row= 2, column=0, columnspan=2)

first_button = tk.Button(root, text="Згенерувати", command=generate_number)
first_button.grid(row=3, column=0, columnspan=2)

second_button = tk.Button(root, text="Відгадати", command=guess)
second_button.grid(row=4, column=0, columnspan=2)

root.mainloop()

##Створити програму-калькулятор.

import tkinter as tk
from tkinter import *

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda btn=button: button_click(btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="(", width=5, height=2, command=lambda: button_click("(")).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text=")", width=5, height=2, command=lambda: button_click(")")).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=row_val, column=col_val)

root.mainloop()
