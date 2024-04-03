import pandas as pd
import numpy as np

df = pd.read_csv('Book.csv')

print(df.head(5))

to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 
           'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(columns=to_drop, inplace=True)

print(df.head(5))

print(df['Identifier'].is_unique)

df.set_index('Identifier', inplace=True)

print(df.loc[206])

print(df.dtypes)

print(df['Date of Publication'])

dates = df['Date of Publication']

dates = dates.str.replace(r'\[.*\]', '')

dates = dates.str.extract(r'^(\d{4})', expand=False)

dates = dates.replace('nan', np.nan)
dates = dates.replace('', np.nan)
dates = dates.replace('NaN', np.nan)

dates = dates.replace('nan', np.nan)

df['Date of Publication'] = pd.to_numeric(dates)

print(df['Date of Publication'])

extr = df['Date of Publication'].astype(str).str.extract(r'^(\d{4})', expand=False)

df['Date of Publication'] = pd.to_numeric(extr)

print(df['Date of Publication'].isnull().sum() / len(df))

condition_london = df['Place of Publication'].str.contains('London')

df['Place of Publication'] = np.where(condition_london, 'London', df['Place of Publication'])

condition_oxford = df['Place of Publication'].str.contains('Oxford')
df['Place of Publication'] = np.where(condition_oxford, 'Oxford', df['Place of Publication'])

print(df['Place of Publication'])

print(df.loc[[4157862, 4159587]])

london = df['Place of Publication'].str.contains('London')
oxford = df['Place of Publication'].str.contains('Oxford')
df['Place of Publication'] = np.where(london, 'London', 
                        np.where(oxford, 'Oxford',
                        df['Place of Publication'].str.replace('-', ' ')))

print(df[df['Place of Publication'] == 'London'].shape[0])

print(df[(df['Date of Publication'] >= 1860) & (df['Date of Publication'] <= 1870)])

print(df['Date of Publication'].max())

print(df['Date of Publication'].min())

import pandas as pd

data = pd.read_csv('loan.csv')
print(data.head())

print(data.shape)

print("\n", data.isnull().sum())

print("\n", data.columns[data.isna().sum() > 10])

print("\n", data[data.isnull().sum(axis=1) > 2])

print("", data[(data.Dependents.isna()) & (data.Married == "NO")])

data.Dependents[(data.Dependents.isna()) & (data.Married == 'No')] = "NA"

print("\n", data.Dependents.unique())

print("\n", data.Married.unique())

data.Married[(data.Married.isna()) & (data.Dependents != 0)] = 'No'

import pandas as pd

with open("town.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

states = []
cities = []

for line in data:
    line = line.strip()
    if line.endswith("[edit]"):
        state = line[:-6]
    else:
        city = line.split(" (")[0]
        cities.append(city)
        states.append(state)

df = pd.DataFrame({"State": states, "City": cities})

print(df)

import pandas as pd

df = pd.read_csv('olymp.csv', encoding='latin1', skiprows=1)

df.columns = ['Літні Олімпійські ігри', 'Зимова Олімпіада', 'Країна', 'золото', 'Срібло', 'Бронза', 'Всього', 
               'золото.1', 'Срібло.1', 'Бронза.1', 'Всього.1', '# Ігри', 'Золото.2', 'Срібло.2', 'Бронза.2', 'Зведений підсумок']

df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

print(df)

