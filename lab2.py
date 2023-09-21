letters = "abcdefghijklmnopqrstuvwxyz"
print(letters)
a = letters[19:]
print(a)
b = letters[11:13]
print(b)
c = letters[21:]
print(c)
d = letters[17:23]
print(d)
f = letters[20:24]
print(f)
g = letters[7:26:7]
print(g)
h = letters[3:19:3]
print(h)
j = letters[18:26:4]
print(j)
k = letters[0:20:5]
print(k)
q = letters[::-1]
print(q)
print(len(letters))

str = 'http://dl.dropbox.com/u/7334460/Magick_py/py_magick.pdf'
str.rfind('/')
file_name = str[42:]

text = "Думи мої, думи мої, Лихо мені з вами! Нащо стали на папері Сумними рядами?..Чом вас вітер не розвіяв В степу, як пилину? Чом вас лихо не приспало, Як свою дитину?... "
aa = text.count(' ')
print(aa)
print(len(text))
text = text.strip()
text1 = text[38:]
splited_text = text1.split("?")
bb = text.replace("степу", "полі")
print(bb)
cc = text.find("вітер")
print(cc)
text.upper()
text.lower()

phone = "+38(099)-123-12-13" 
aaa = phone.replace("-", " ")
bbb = aaa.replace("(", " ")
ccc = bbb.replace("+", " ")
fff = ccc.replace(")", " ")
print(fff)