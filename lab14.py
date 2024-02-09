import pandas as pd

population_dict = {"Kyiv": 2967360, "Kharkiv": 1443207, "Odesa": 1017699, "Dnipro": 990724, "Doneck": 908456, "Zaporizcha": 731922, "Lviv": 717273, "Kryvyi Rih": 619278, "Mykolaiv": 480080, "Sevastopol": 449138} 
population = pd.Series(population_dict)
a= pd.DataFrame(list(population_dict.items()), columns = ["City", "Population"])
minn = a[a["Population"]== a["Population"].min()]
maxx  = a[a["Population"]== a["Population"].max()]
average = a["Population"].mean()
fisrt5 = a.head(5)["Population"]
print(population)
print("Найменше значення",minn)
print("Найбільше значення",maxx)
print("Середня к-сть населення",average)
print("Населення Києва: ",population["Kyiv"])
print(fisrt5)
new_city = {"Poltava": 286649}
population_dict.update(new_city)
population = pd.Series(population_dict)
a= pd.DataFrame(list(population_dict.items()), columns = ["City", "Population"])
print(population) 
above1M = a[a["Population"] > 1000000]
print(above1M)
cities = a["City"].tolist()
print(cities)


a = pd.DataFrame({ 
    "town": ['Shanhai', "Beijing", "Tianjin", "Stambul", "Lagos", "Guangzhou", "Mumnbai", "Barad-dûr", "Dakka", "Cairo"],
    "population": [24150000, 21516000, 14722100, 14377019, 13400000, 12700800, 12655220, 12197596, 12043977, 11922949],
    "squares": [6340.5, 16410.54, 4037, 5461, 999.58, 3843.43, 603.4, 2510.12, 1463.6, 3085.1],
    "country": ["CPR", "CPR", "CPR", "Turkey", "Nigeria", "CPR", "India", "Mordor", "Bangladesh", "Egypt"]
})
a["destiny"] = a["population"]/a["squares"]
print(a)
aa = a[['town', "country"]]
print("Виведення міст та країн")
print(aa)
f5 = a.head(5)
print("Перші 5 міст")
print(f5)
a.index.name = "Town's name"
print(a)
aaa = a.iloc[0]
print(aaa)
above12M = a[a["population"] > 12000000]
print("Населення більше 12000000")
print(above12M)
square5km = a[a["squares"] > 5000]
print("Міста з площею більше 5к км^2 ")
print(square5km)
CNR = a[a["country"] == "CPR"]
print(CNR)