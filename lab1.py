print("Hello, enter your name:")
name = input()
print("Hello, "+ name +"!")

print("Hi, answer for next questions:","What is your name?", sep="\n")
names = input()
print("How old are you?")
age = input()
print("Where do you live?")
place = input()
print("This is " + names + "","it is " + age + "", "(S) He lives in " + place + "", sep="\n")

print("Напишіть ваше ім'я та прізвище")
a,b = input().split()
print("Ім'я: " + a + "")
print("Прізвище: " + b + "")

print("Напишіть 4 різних цифри через ';' ")
c,d,e,f = input().split(';')
print("Перша цифра: " + c + "")
print("Друга цифра: " + d + "")
print("Третя цифра: " + e + "")
print("Четверта цифра: " + f + "")

print("Введіть поточний рік:")
n = input()
q = int(n)
m = q + 50
print("Поточний рік + 50 років = ", m )

dd,mm,yyyy = input("Введіть вашу дату народження у цифровому форматі (Наприклад: 13.10.2004) ").split('.')
print("Ви народились: " + dd + " числа " + mm + " місяця " + yyyy + " року!")

aa,bb = input("Введіть два різних числа: ").split()
x = int(aa)
z = int(bb)
print("Множення: ", x * z)
print("Ділення: ", x / z)
print("Додавання: ", x + z)
print("Віднімання: ", x - z)

qq,mm,ss,ff = input("Введіть 4 різних числа: ").split()
o = float(qq + mm)
g = float(ss + ff)
v= round(o/g, 2)
print("МАГІЯ: ", v)

xx = int(input("Введіть перше натуральне число: "))
bb = int(input("Введіть друге натуральне число: "))
az = xx//bb
vz = xx % bb
print(f"{xx}/{bb} = {az} та {vz} в залишку")

n = int(input("Введіть двозначне число: "))
d = n // 10
oo = n % 10
s = d + oo
print(f"Сума цифр числа {n} = {s}")

nn = int(input("Введіть натуральне число: "))
ooo = nn % 10
print(f"Останнє число: {nn} = {ooo}")