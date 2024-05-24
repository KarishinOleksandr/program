from bs4 import BeautifulSoup
import requests

URL_TEMPLATE = "https://jobs.ua/city/poltava_jobs"
r = requests.get(URL_TEMPLATE)

if r.status_code == 200:
    print("Успіх")
else:
    print("ПОмилка:", r.status_code)


print("Текст сторінки: \n")
print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
print("Текст з використанням методу pretiffy(): \n")
print(soup.prettify())

print("Інформація про вакансії: \n")
vacans = soup.find_all("h3", class_="")
for name in vacans:
    vacans_title = name.a.text.strip()
    vacans_url = "https://jobs.ua/city/poltava_jobs" + name.a["href"]
    print(f"<h2 class=''\n\t<a href='{vacans_url}' title='{vacans_title}'>{vacans_title}</a>\n</h2>")

print("Перелік вакансій: \n")
for name in vacans:
    print(name.a["title"])

print("Текст вакансій: \n")
for name in vacans:
    print(name.a['title'].split(', вакансія')[0])    

print("Сайт вакансій: \n")
for name in vacans:
    vacans_title = name.a["title"].split(",")[0]
    vacans_url = "https://jobs.ua/city/poltava_jobs" + name.a["href"]
    print(f"{vacans_title}: {vacans_url}")

print("Вивід текстової інформації про вакансію: \n")
vacans_info = soup.find_all("span", class_="link__hidden")
for info in vacans_info:
    print(info.text.strip())

print("Інформація по зп: \n")
salars = soup.find_all("span", class_="b-vacancy__top__pay")
for salar in salars:
    print(salar.text.strip())

