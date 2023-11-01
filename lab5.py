# Вивести на екран послідовність чисел від 1 до 20.
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    print(number)

# Дано два цілих числа A і В. Вивести всі числа від A до B включно, в порядку зростання, якщо A <B, або в порядку спадання, якщо A>B.
A = int(input("Введіть число А: "))
B = int(input("Введіть чилсо В: "))

if A > B:
    for cc in range(A, B -1, -1):
        print(cc)

elif A <= B:
    for cc in range(A, B +1):
        print(cc)

dod = 1

# Написати програму, яка зчитує 10 чисел, що вводить користувач та виводить добуток цих чисел.
for f in range(10):
    try:
        mm = int(input("Введіть число: "))
        dod = dod * mm
    except ValueError:
        print("Введіть ЧИСЛО")

print("Добуток: ", dod)

# Написати програму, яка зчитує 10 чисел, що вводить користувач  та виводить парні числа.
yy = []

for f in range(10):
    try:
        mmm = int(input("Введіть число: "))
        if mmm % 2 == 0:
            yy.append(mmm)
    except ValueError:
        print("Введіть ЧИСЛО")

if yy:
    print("Парені числа які ви ввели: ")
    for mmm in yy:
        print(mmm, end=" ")
else:
    print("Ви не ввели парні числа")

# Написати програму, яка зчитує 10 чисел, що вводить користувач  та виводить найбільше з цих чисел.
yyy = None

for ff in range(10) :
    try:
        yxz = int(input("Введіть число: "))
        if yyy is None or yxz > yyy:
            yyy = yxz
    except ValueError:
        print("Введіть число")

print("Найбільше введене число: ", yyy)

# Написати програму, щоб зчитувала рядок від користувача та відображувала лише ті символи, індекси яких мають парні номери/
# Наприклад, str = "pynative", слід відобразити "p", "n", "t", "v".

vhid = input("Введіть якесь речення. ")

vuhid = ""
for zz in range(len(vhid)):
    if zz % 2 == 0:
        vuhid = vuhid + vhid[zz]

print("Парні індеси: ", vuhid)

# Напишіть програму Python для побудови наступного шаблону, використовуючи вкладений цикл for.

kk = 5

for u in range(1, kk + 1):
    for j in range(1, u + 1):
        print("*", end="")
    print()

for u in range(kk - 1, 0, -1):
    for j in range(1, u + 1):
        print("*", end="")
    print()

def calculate_profit(amount, percent, period):
    if amount == 0 or percent == 0 or period == 0:
        return 0

    for _ in range(period):
        amount += amount * (percent / 100)

    profit = amount - amount / (1 + percent / 100)
    return round(profit, 2)

amount = float(input("Введіть початкову суму: "))
percent = float(input("Введіть річну відсоткову ставку: "))
period = int(input("Введіть кількість років: "))


profit = calculate_profit(amount, percent, period)
print("Чистий прибуток", profit)

result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            user_input = input("Введіть число або = для обчислення: ")
            if user_input == "=":
                break
            operand = float(user_input)
            wait_for_number = False
        else:
            user_input = input("Введіть оператор (+, -, *, /): ")
            if user_input not in ('+', '-', '*', '/'):
                print("Ви ввели неправильний оператор")
                continue
            operator = user_input
            wait_for_number = True

            if result is None:
                result = operand
            else:
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    if operand == 0:
                        print("Ділення на нуль неможливе. Спробуйте ще раз.")
                        continue
                    result /= operand

    except ValueError:
        print("Введіть число")

if result is not None:
    print("Результат: ", result)