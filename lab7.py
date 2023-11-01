#Написати програму, яка знаходить суму усіх елементів списку.
list = (1, 2, 3, 4, 5, 6, 7 , 8)
print(sum(list))

#Написати програму, яка рахує кількість елементів списку, які мають два та більше символів.
list1 = ["1", "kva", "jaba", "poshuk", "laba"]
rah = []

for item in list1:
    if len(item) >= 2:
        rah.append(1)
rah2 = sum(rah)
print("Кількість елементів в списку, які мають більше одного символа", rah2)

#Написати програму, яка прибирає дублікати значень зі списку. Очікуваний результат: Для a = [10,20,30,20,10,50,60,40,80,50,40] [10, 20, 30, 50, 60, 40, 80]

a = [10,20,30,20,10,50,60,40,80,50,40]

sortirovka = list(set(a))
sortirovka.sort()

print(sortirovka)

#Відкрийте файл romeo.txt і прочитайте його рядок за рядком. 
# Для кожного рядка розділити рядок на список слів методом split (). 
# Програма повинна скласти список слів. Для кожного слова в кожному рядку перевірте, чи слово вже є у списку, і якщо ні, його слід додати до списку. 
# Коли програма завершиться, список необхідно відсортувати та вивести на друк слова в алфавітному порядку. fname = input("Enter file name: ") fh = open(fname) lst = list()

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()

print(lst)

#Відкрийте файл mbox-short.txt і прочитайте його рядок за рядком. Коли ви знайдете рядок, який починається словом 'From', як наведено нижче :
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
#такий рядок необхідно розбити на слова за допомогою split () і роздрукувати друге слово в рядку (тобто всю адресу особи, яка відправила повідомлення). Вивести кількість таких поштових адрес.

#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
#fh = open(fname)
#print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = []

for line in fh:
    slova = line.split()
    if len(slova) < 2 or slova[0] != "From":
        continue
    print(slova[1])
    count.append(1)
count = sum(count)

print("There were", count, "lines in the file with From as the first word")