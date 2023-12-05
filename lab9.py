#Заданий файл dict.txt, що містить словник в форматі:
# cat - кішка
# dog - собака
# house - дім
# В словнику англійські та українські слова розділені двома табуляціями та девісом: '\t-\t'.
# У файлі translate.txt міститься текст для перекладу.
# Необхідно зробити порядковий переклад та за допомогою словника вивести результат у файл output.txt. Незнайомі слова необхідно залишити у незмінному вигляді. 

with open('dict.txt', 'r', encoding='utf-8') as dict_file:
    translation_dict = {}
    for line in dict_file:
        parts = line.strip().split('\t-\t')
        if len(parts) == 2:
            eng_word, ukr_word = parts
            translation_dict[eng_word] = ukr_word

with open('translate.txt', 'r', encoding='utf-8') as translate_file:
    trans_text = translate_file.read()

lines = trans_text.splitlines()

with open('output.txt', 'w', encoding='utf-8') as output_file:
    translated_lines = []

    for line in lines:
        words = line.split()
        translated_words = []

        for word in words:
            word = word.strip('.,!?()[]{}"\'')
            if word in translation_dict:
                translated_words.append(translation_dict[word])
            else:
                translated_words.append(word)

        translated_line = ' '.join(translated_words)
        translated_lines.append(translated_line)

    output_file.write('\n'.join(translated_lines))

# У файлі input_countries.txt заданий перелік країн та мов, на яких розмовляють в цих країнах у форматі: <Назва країни> : <мова 1> <мова 2> <мова 3>
# Для введеної користувачем мови необхідно вивести перелік країн, в яких розмовляють даною мовою.

zapros = input("Введіть обрану мову: ")

found_countries = []

with open('input_countries.txt', 'r', encoding='utf-8') as dict_file:
    for line in dict_file:
        parts = line.strip().split(':')
        if len(parts) == 2:
            cont, lang = parts
            cont = cont.strip()
            lang = lang.split()
            if zapros in lang:
                found_countries.append(cont)

if found_countries:
    print("Країни, де розмовляють мовою:")
    for country in found_countries:
        print(country)
else:
    print("Цієї мови немає в словнику для жодної країни.")

# У вагоні-купе є кілька купе, у кожному з яких по 4 місця. Розробник зберігає інформацію про зайнятість одного купе у вигляді словника:
# {1: 'м', 2: None, 3: None, 4: 'ж'}
# де:

# ключ визначає номер місця (непарні номери – нижні місця, парні – верхні);
# значення може бути одне з трьох: None, "м" та "ж", якщо місце не зайняте, зайняте чоловіком або жінкою відповідно.
# Інформація про зайнятість всього вагона зберігається як перелік зазначених словників.

# Визначте:
# •        список повністю вільних купе;
# •        список вільних місць у вагоні;
# •        список вільних нижніх чи верхніх місць;
# •        список вільних місць у поєднанні з виключно чоловічою компанією;
# •        список вільних місць у поєднанні з виключно жіночою компанією.


wagon = {
    1: 'м',
    2: None,
    3: None,
    4: 'ж'
}

free_cabins = [cab for cab in range(1, len(wagon) + 1) if all(seat is None for seat in wagon[cab].values())]

free_seats = [cab * 10 + seat for cab in wagon for seat, occupant in wagon[cab].items() if occupant is None]

free_nuzh_seats = [cab * 10 + seat for cab in wagon for seat, occupant in wagon[cab].items() if seat % 2 == 1 and occupant is None]

free_m_sears = [cab * 10 + seat for cab in wagon for seat, occupant in wagon[cab].items() if occupant is None and all(val == 'м' for val in wagon[cab].values())]

free_w_seats = [cab * 10 + seat for cab in wagon for seat, occupant in wagon[cab].items() if occupant is None and all(val == 'ж' for val in wagon[cab].values())]

print("Список повністю вільних купе:", free_cabins)
print("Список вільних місць у вагоні:", free_seats)
print("Список вільних нижніх місць:", free_nuzh_seats)
print("Список вільних місць у поєднанні з виключно чоловічою компанією:", free_m_sears)
print("Список вільних місць у поєднанні з виключно жіночою компанією:", free_w_seats)