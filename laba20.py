import re
def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(specific_char("ABCDEFabcdef123450")) 
print(specific_char("*&%@fgfhdfghkhglj#!}{"))

import re

pattern = r'a{1}b{2,}'

text1 = "ab"
text2 = "aabbbbbc"

result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)

print(result1)
print(result2)

import re

def check(text):
    pattern = r'^[a-z_]+$'
    result = re.search(pattern, text)
    
    print(result)

text1 = 'aab_cbbbc'
text2 = 'aab_Abbbc'
text3 = 'Aaab_abbbc'

check(text1)
check(text2)
check(text3)

import re

def find_all_emails(text):
    pattern = r'\b[A-Za-z]\w*@[A-Za-z]+\.[A-Za-z]{2,}\b'
    matches = re.findall(pattern, text)
    return matches

text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
result = find_all_emails(text)
print(result)

import re

def remove_zero(ip):
    pattern = r'\b0+(\d+)\b'

    def replace_zeros(match):
        return str(int(match.group(1)))

    result = re.sub(pattern, replace_zeros, ip)

    return result

ip = "216.08.094.196"
result = remove_zero(ip)
print(result)

import re

def check(text):
    pattern = re.compile(r'\d$')
    match = pattern.search(text)
    return bool(match)

text1 = 'abcdef'
text2 = 'abcdef6'

result1 = check(text1)
result2 = check(text2)

print(result1)
print(result2)

import re 

def changed(data):
    pattern = re.match(r'(\d{4})-(\d{2})-(\d{2})', data)
    changed_data = f"{pattern.group(3)} - {pattern.group(2)} - {pattern.group(1)}"
    
    return changed_data

data = "2026-01-02"

result = changed(data)
print(result)

import re

def find_all_phones(text):
    pattern = re.compile(r'\+380\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}')
    return pattern.findall(text)

text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
phones = find_all_phones(text)
print(phones)

import re

def find_all_words(word, text):
    pattern = re.compile(fr'\b{re.escape(word)}\b', re.IGNORECASE)
    return pattern.findall(text)

text = "Python is a modern programming language. PyThOn is easy. I love pYtHoN"
word = "python"
matches = find_all_words(word, text)
print(matches)

import re

def sanitize_phone_number(phone_number):
    digits_only = re.sub(r'\D', '', phone_number)
    if len(digits_only) == 12 and digits_only.startswith('380'):
        return digits_only
    elif len(digits_only) == 10:
        return digits_only
    else:
        return None

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for number in phone_numbers:
    print(sanitize_phone_number(number))
