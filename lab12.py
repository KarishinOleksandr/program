def bank(x, years):
    years_procent = 0.10 
    total_amount = x 

    for _ in range(years):
        total_amount += total_amount * years_procent
        total_amount = int(total_amount)
    return print("Загальна сума: ", total_amount)

bank(14000, 20)

def recommend_sneakers():
    print("It is sunny day, good to wear Sneakers.")

def recommend_rainboots():
    print("Oops! It is raining, Gumboot would be better to wear.")

def recommend_regularboots():
    print("Wow! It is snowing, better to wear boots.")

def main():
    weather = input("What is the weather today? (sunny, rainy, snowy): ").lower()

    if weather == "sunny":
        recommend_sneakers()
    elif weather == "rainy":
        recommend_rainboots()
    elif weather == "snowy":
        recommend_regularboots()
    else:
        print("Invalid option")

main()

def combine(list1, list2):
    result = []
    minn = min(len(list1), len(list2))

    for i in range(minn):
        result.append(list1[i])
        result.append(list2[i])

    if len(list1) > len(list2):
        result.extend(list1[minn:])
    elif len(list2) > len(list1):
        result.extend(list2[minn:])

    return print(result)

list1 = [1, 2, 3]
list2 = [11, 22, 33]

combine(list1, list2)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_previous_date(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    if day > 1:
        return day - 1, month, year
    elif month > 1:
        return days_in_month[month - 1], month - 1, year
    else:
        return 31, 12, year - 1

def get_next_date(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    if day < days_in_month[month]:
        return day + 1, month, year
    elif month < 12:
        return 1, month + 1, year
    else:
        return 1, 1, year + 1


current_day = 30
current_month = 11
current_year = 2023

previous_date = get_previous_date(current_day, current_month, current_year)
next_date = get_next_date(current_day, current_month, current_year)

print("Вчора:", previous_date)
print("Завтра:", next_date)

def draw_frame(text, char):
    length = len(text) + 4

    print(char * length)

    print(char, text, char)

    print(char * length)

input_text = "Текст в рамці"
frame_char = "*"
draw_frame(input_text, frame_char)

def getInput():
    return input("Введіть значення: ")

def testInput(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def strToInt(value):
    return int(value)

def printInt(value):
    print("Отримане значення:", value)

input_value = getInput()

if testInput(input_value):
    int_value = strToInt(input_value)
    printInt(int_value)
else:
    print("Введене значення не є цілим числом.")

def sort(input_s):
    words = input_s.split('-')
    sorted_words = sorted(words)
    result = '-'.join(sorted_words)
    print(result)

input_se = input("Введіть послідовність слів, розділених дефісами: ")

sort(input_se)

import re

def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,254}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    return bool(pattern.match(email))

email_address = input("Введіть адресу електронної пошти: ")

if is_valid_email(email_address):
    print("Це дійсна адреса електронної пошти.")
else:
    print("Це не дійсна адреса електронної пошти.")
