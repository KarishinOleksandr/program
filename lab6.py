#Створити файл. Записати у файл своє ім’я та прізвище.
my_file = open("1.txt", "w")
my_file.write("Oleksandr Karishin")
my_file.close

#Створити текстовий файл, записати в нього дані, які вводить користувач. 
# Закінченням введення служить порожній рядок. Порахувати та вивести на друк кількість ліній та кількість символів.
my_file2 = "2.txt"
with open(my_file2, "w") as file:
    linii = 0
    lenn = 0

    while True:
        vvid = input("Введіть будь який текст, або порожній для завершення: ")
        if vvid == "":
            break

        file.write(vvid + "\n")
        linii = linii + 1
        lenn = lenn + len(vvid)

print("Кількість ліній: ", linii)
print("Кількість символів: ", lenn)

#Написати програму яка рахує кількість рядків, які НЕ починаються з літери "T" та кількість рядків, які закінчуються на “d” у файлі poetry.txt. 
# Вивести на друк кількість слів, що починаються з великої літери.
my_file3 = "poetry.txt"

ryad_T = 0
ryad_D = 0
V_liter = 0
with open(my_file3, "r") as file:
    for line in file:
        line = line.strip("")
        if not line.startswith("T"):
            ryad_T = ryad_T + 1
        elif line.endswith("d"):
            ryad_D = ryad_D + 1

        slova = line.split()
    for slovo in slova:
        if slovo and slovo[0].isupper():
            V_liter = V_liter + 1

print("Кількість рядків які не починаються на Т: ", ryad_T)
print("Кількість рядків які закінчується на d: ", ryad_D)
print("Кількість слів надруковані з великої літери: ", V_liter)

#У файлі mbox-short.txt порахувати кількість символів в кожному рядку файлу та знайти найдовше слово.
my_file4 = "mbox-short.txt"

dlunne = ""

with open("mbox-short.txt", "r") as file:
    for line in file:
        line = line.strip()
        dlina_linii = len(line)

        slova2 = line.split()
        for slovo in slova2:
            if len(slovo) > len(dlunne):
                dlunne = slovo
        
        print("Кількість символів в рядку: ", dlina_linii)

print("Найдовше слово: ", dlunne)

my_file4 = "mbox-short.txt"

with open(my_file4, "r") as file:
    for linein in file:
        print(line.upper(), end='')
    

#Напишіть програму яка зчитує файл mbox-short.txt та друкує його вміст (рядок за рядком) у верхньому регістрі. Виконання програми буде виглядати наступним чином: 
my_file4 = "mbox-short.txt"

cilk = list()
with open(my_file4, "r") as file:
    for line in file:
        if "@" in line:
            print(line, end="")
            cilk.append(1)
    aa = sum(cilk)
print("Кількість рядків з @: ", aa)