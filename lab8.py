#Написати програму, яка виводить відсортовані елементи словника.
d = dict({"A": 34, "B": 45})
print(d)

#Знайти три ключі з найбільшими значеннями в словнику: 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted1 = sorted(my_dict.items(), key = lambda x: x[-1])

top3 = sorted1[:3]

for key, value in top3:
    print(key)

#Написати програму, яка перевіряє, чи існує такий ключ у словнику. Розробити словник, що містить три великі річки  та країни, якими вони протікають у форматі ключ-значення: river:country. Вивести за допомого циклу на екран по одному реченню про кожну річку: Річка «river» протікає через «country».

slov = dict({"Дніпро": "Україна", "Ніл": "Єгипет", "Амазонка": "Бразилія"})
zapros = input("Введіть назву річки: ")
if zapros in slov:
    country = slov[zapros]
    print(f"Річка '{zapros}' протікає '{country}'." )
else:
    print("Ціє річки немає в базі данних")

#Написати програму, яка створює словник, що в якості ключа містить числа (від 1 до n), а у якості значень квадрат цього числа.
n = int(input("Введіть значення n: "))
zapros = {}

for i in range(1, n + 1):
    zapros[i] = i ** 2

print(zapros)

# Відкрийте файл mbox-short.txt і прочитайте його рядок за рядком. Коли знайдете рядок, який починається словом 'From', як наведено нижче :
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
# такий рядок необхідно розбити на слова за допомогою split () і записати друге слово в рядку в словник (тобто всю адресу особи, яка відправила повідомлення).\
# Програма створює словник Python, який відображає поштову адресу відправника з урахуванням кількості випадків їх появи у файлі. 
# Після створення словника програма читає словник, використовуючи максимальний цикл, щоб знайти адресата, який відправив найбільшу кількість листів.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

zapros = {}

for line in handle:
    if line.startswith('From '):
        words = line.split()
        zapros1 = words[1]
        zapros[zapros1] = zapros.get(zapros1, 0) + 1

maxzapros = None
rah = None

for zapros1, count in zapros.items():
    if maxzapros is None or count > rah:
        maxzapros = zapros1
        rah = count

print(maxzapros, rah)

# Ви створюєте гру, структура даних для інвентаря гравця – словник. В якому ключі – рядкові величини, що описують інвентар, а значення – кількість одиниць даного інвентаря. 
# Наприклад: 
 
# Напишіть програму, яка приймає за аргумент опис інвентаря і відображає його в наступному вигляді:


def inventar(inventory):
    print("Inventory: ")
    total_items = 0
    for item, quantity in inventory.items():
        print(quantity, item)
        total_items = total_items + quantity
    print("Total number of items: ", total_items)

player_inv = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

inventar(player_inv)