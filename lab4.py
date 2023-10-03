n = 1
while n <= 512:
    print(n)
    n = n * 2

nn =  int(input("Введіть чотирьохзначне число: "))
tuch = nn // 1000
sotni = (nn // 100) % 10
des = (nn // 10) % 10
od = nn % 10
s = tuch + sotni + des + od
print("Сума всіх цифр:", s)

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