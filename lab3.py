password = input("Введите пароль: ")
if password == "sshh":
    print("Вітаємо!")
else:
    print("Доступ заборонено")

text_pass = "hhh" "lll" "qqq" "ddd" "sss"
proverk = input("Введите пароль: ")
if proverk == "hhh":
    print("вітаю")
elif proverk == "lll":
    print("вітаю")
elif proverk == "qqq":
    print("вітаю")
elif proverk == "ddd":
    print("вітаю")
elif proverk == "sss":
    print("вітаю")
else:
    print("Відхилено")

score = int(input("Введите вашу оцінку: "))
if score >= 90:
	print("Ваша оцінка А")
elif score >= 82:
	print("Ваша оцінка B")
elif score >=74:
     print("Ваша оцінка C")
elif score >=64:
     print("Ваша оцінка D")
elif score >=60:
     print("Ваша оцінка E")
elif score >=35:
     print("Ваша оцінка FX")
elif score >=0:
     print("Ваша оцінка F")
else:
     print("Введіть цифру")

a,b = input("Ведіть два числа через пробіл:").split()
if a>b:
    print("b менше")
elif b>a:
    print("a менше")
elif a==b:
    print("a = b")

aa,bb,cc = input("Ведіть три числа через пробіл:").split()
if aa >= bb and aa>= cc:
    print("a найбільше")
elif bb >= aa and bb >= cc:
    print("b найбільше")
elif cc >= aa and cc >= bb:
    print("c найбільше")

x = input("Введіть будь яке число: ")
m = int(x)
if m > 0:
    print("X більше 0")
elif m < 0:
    print("X менше 0")
elif m == 0:
    print("X = 0")

xx = int(input("Введіть число: "))
if xx % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

den = int(input("Введіть будь яку цифру від 1 до 7: "))
if den == 1:
    print("Перший день тиждня - Понеділок")
elif den == 2:
    print("Другий день тиждня - Вітвторок")
elif den == 3:
    print("Третій день тиждня - Середа")
elif den == 4:
    print("Четвертий день тиждня - Четвер")
elif den == 5:
    print("П'ятий день тиждня - П'ятниця")
elif den == 6:
    print("Шостий день тиждня - Субота")
elif den == 7:
    print("Неділя день тиждня - Неділя")
else:
    print("Від 1 до 7")


usd = 28
euro = 32
print("Доброго дня.","Курс валют на данний момент:", "Доллар - 28","Євро - 32", sep="\n" )
try:
    money = int(input("Введіть суму, яку ви бажаєте обміняти: "))
except ValueError:
    print("Невірно введена сума. Будь ласка, введіть число.")
    exit()

try:
    currency = int(input("Вкажіть код валюти: (долар - 400, євро - 401): "))
except ValueError:
    print("Вкажіть коректний код валюти (долар - 400, євро - 401)")
    exit()
if currency == 400:
        xxx = money/usd
        print(xxx)
elif currency == 401:
        yyy = money/euro
        print(yyy) 
else:
    print("Вкажіть коректний код валюти (долар - 400, євро - 401)")