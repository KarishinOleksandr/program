from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = "https://www.holidify.com/explore/"
r = requests.get(url)

if r.status_code == 200:
    print("Успіх")
else:
    print("ПОмилка:", r.status_code)

p_soup = BeautifulSoup(r.text, "html.parser")

contain = p_soup.find_all("div", class_="col-12 col-md-6 pr-md-3")
print("Кількість країн для аналізу \n", len(contain))

country = []
p_name = p_soup.find_all("h3", class_="card-heading")
for name in p_name:
    p_namee = name.text[4:].strip().split("-")
    namee = p_namee[0].strip().split(",")
    country.append(namee[0])
print("Назв країн: \n", country)

ratings = []
p_ratings = p_soup.find_all("span", class_="rating-badge")
for rating in p_ratings:
    cleaned_rating = rating.text.strip().replace("\n", "").replace("/5", "").strip()
    ratings.append(cleaned_rating)
print("Рейтинг турів: \n", ratings) 

about = []
p_about = p_soup.find_all("p", class_="card-text")
for abouts in p_about:
    about.append(abouts.text.strip())
numbered_about = [f"{i+1}. {desc}" for i, desc in enumerate(about[:5])]
print("Опис турів \n"+"\n".join(numbered_about))

attraction = []
p_attraction = p_soup.find_all("p", class_="collection-cta")
for attractions in p_attraction:
    match = re.search(r"\d", attractions.text)
    if match:
        attraction.append(int(match.group()))
    else:
        attraction.append(0)
print("Кількість місць: \n", attraction)

column = ['Place', 'Ratings','About','Attraction']
Data = pd.DataFrame(list(zip(country, ratings, about, attraction)), columns = column)


Data.to_csv("Places.csv", index = None)

Data["Ratings"] = Data['Ratings'].astype(float)
top_rated = Data.nlargest(10, 'Ratings')
print("10 країн з найвищим рейтингом \n", top_rated)

Data['Attraction'] = Data["Attraction"].astype(int)
top_attraction = Data.nlargest(10, 'Attraction')
print("10 Краън з більшістю місць \n", top_attraction)