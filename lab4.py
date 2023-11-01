# Вивести на екран послідовність чисел 1 2 4 8 16 32 64 128 256 512.
n = 1
while n <= 512:
    print(n)
    n = n * 2

# Для введеного чотирьохзначного числа знайти суму усіх його цифр.
nn =  int(input("Введіть чотирьохзначне число: "))
tuch = nn // 1000
sotni = (nn // 100) % 10
des = (nn // 10) % 10
od = nn % 10
s = tuch + sotni + des + od
print("Сума всіх цифр:", s)

# Написати програму, яка зчитує числа, що вводить користувач до тих пір, поки не зустріне від’ємне число. 
# При появі від’ємного числа програма завершується і виводить суму від додатніх чисел, введених користувачем.
mm = 0
while True:
    try:
        number = int(input("Введіть число, якщо хочете завершити - введіть від`ємне: "))
    except ValueError:
        print("Будь ласка введіть одне ціле число, або від'ємне для завершення: ")
        continue
    if number < 0:
        break  
    else:
        mm += number 

print("Сума всіх числел: ", mm)

# Написати програму, яка зчитує числа, що вводить користувач до тих пір, поки не зустріне нуль. 
# При появі нуля програма завершується і виводить середнє значення від усіх чисел, введених користувачем.
ff = 0
uu = 0

while True:
    try:
        rr = float(input("Введіть число або 0 для виходу: "))
    except ValueError:
        print("Будь ласка, ввкедіть числа")
        continue

    if number == 0:
        break 
    else:
        ff += rr
        uu += 1

if uu == 0:
    print("Ви не ввели жодного числа")
else:
    average = ff / uu
    print("Середнє значення введених чисел: ", )

# У введеному користувачем тексті, збереженому у змінній word вивести всі символи крім голосних літер.
word = input("Введіть будь яке речення українською: ")
i = 0
golos = "АЕЄІЇЙОУЮЯаеєіїйоуюя"
itog =""

while i < len(word):
    bb = word[i]
    if bb not in golos:
        itog += bb
    i += 1

print("Ваше речення без голосних:", itog)

# Є різні цінові категорії квитків у кінотеатр – залежно від покупця. Якщо клієнту менше ніж 3 роки – квиток безкоштовний, від 3-12 років – коштує 50 грн, вартість дорослого квитка – 80 грн. 
# Напишіть цикл в якому ви питатимете користувача про його вік, а тоді підказуватимете вартість квитка. Для вирішення задачі використайте умовну перевірку в операторі while для виходу з циклу. 
# Використайте змінну number -для підрахунку кількості ітерацій в циклі. Використайте оператор break для виходу з циклу, коли користувач натисне значення ‘exit’.
nnumber = 1

while True:
    age = input("Введіть ваш вік або 'exit' для виходу: ")

    if age == "exit":
        print("До побачення. Гарного дня")
        break
    try:
        age = int(age)
    except ValueError:
        print("Некоректний ввід. Повторіть")
        continue
    if age < 3:
        print("Квиток безкоштовний")
    elif 3 <= age <= 12:
        print("Квиток коштує - 50 грн")
    else:
        print("Квиток коштує - 80 грн")

    nnumber += 1

import random

ss = random.randint(1, 10)

while True:
    guess = input("Вгадайте число від 1 до 10 або введіть 99 для виходу: ")

    if guess.lower() == '99':
        print("До зустрічі!")
        break

    if not guess.isdigit():
        print("Введіть будь ласка ціле число")
        continue 

    guess = int(guess)

    if guess < 1 or guess > 10:
        print("Введіть число від 1 до 10")
    elif guess < ss:
        print("Загадане число більше.")
    elif guess > ss:
        print("Загадане число менше.")
    else:
        print("Вітаю, ви перемогли!")
        break