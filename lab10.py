# Написати програму, яка перевіряє скільки разів елемент повторюється в кортежі.
t = tuple("a, b, v, a, a, a")
v = t.count("a")
print(v)

# Написати програму, яка для заданого кортежу на запит користувача виводить індекс елементу в кортежі.
t = tuple("a, b, v, a, a, j")
v = t.index("v")
print(v)

# Написати програму, яка для заданого кортежу виводить новий кортеж, що містить перший і останній елемент попередньо.
t = ("a, b, v, c, d, j")
v = (t[0], t[-1])
print(v)

# Написати програму, яка перевіряє чи всі елементи кортежу однакові та повідомляє про це користувачу.
def perevirka(kortej):
    if all(elem == kortej[0] for elem in kortej):
        print("Всі елементи кортежу однакові.")
    else:
        print("Елементи кортежу неоднакові.")

t = (6,6,6,6,6)
perevirka(t)

# Написати програму, яка знаходить суму всіх числових елементів змішаного кортежу, якщо текстовий елемент кортежу можна перевести в число, програма здійснює це перетворення і додає елемент до загальної суми числових значень кортежу.
# Приклад:
# sum_numeric(10, 20, 'a', '30', 'bcd')
# Результат: Сума елементів дорівнює 60

def summ(*args):
    total_sum = 0

    for element in args:
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str) and element.isdigit():
            total_sum += int(element)

    return total_sum

tt = ("a", 3, 56, 1, 8, "10")
result = summ(*tt)
print("Сума елементів =", result)


# Написати програму, яка змінює останню цифру на цифру введену користувачем в усіх вкладених кортежах заданого списку.
# Приклад:
# number=100
# list1= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Результат: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

def change(number, tuple_list):
    new_list = []

    for tpl in tuple_list:
        lst = list(tpl)

        lst[-1] = number

        new_list.append(tuple(lst))

    return new_list

number_to_insert = int(input("Введіть число для заміни останнього числа в кожному кортежі: "))
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result_list = change(number_to_insert, list1)
print("Результат:", result_list)


# Відкрийте файл mbox-short.txt і прочитайте його рядок за рядком. Коли ви знайдете рядок, який починається словом 'From', як наведено нижче :
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
# такий рядок необхідно розбити на слова за допомогою split () і знайти час, який також слід розбити, використовуючи роздільник двокрапку. 
# За результатом роботи програми слід порахувати скільки разів кожен час зустрічається у файлі та вивести результат в порядку зростання.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = {}

for line in handle:
    if line.startswith('From '):
        words = line.split()
        times = words[5].split(':')[0]
        time[times] = time.get(times, 0) + 1

for times, count in sorted(time.items()):
    print(times, ":", count)

# Є чотирикутна схема польотів дронів з координатами (0, 1, 2, 3). У нас є словник points, ключі якого — кортежі, точки польоту між координатами чотирикутника, вигляду (1, 2). 
# Значення словника — це відстані між вказаними точками.

# Приклад:
# points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

# Напишіть програму, яка використовуючи список координат чотирикутника зі словника виду [0, 1, 3, 2, 0]. 
# Програма повинна підрахувати, використовуючи вказаний словник, яку загальну відстань пролетить дрон, рухаючись між точками польоту.

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
    }

def calculate(coord_list, distances):
    total_distance = 0

    for i in range(len(coord_list) - 1):
        point_pair = tuple(sorted([coord_list[i], coord_list[i + 1]]))
        total_distance = total_distance + distances.get(point_pair, 0)

    return total_distance

drone_path = [0, 1, 3, 2, 0]
total_distance = calculate(drone_path, points)

print("Загальна відстань, яку пролетів дрон: ", total_distance)