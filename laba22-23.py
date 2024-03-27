import pandas as pd

train = pd.read_csv('train.csv')
df = train.copy()

print(df)

print(df.head(5))
print(df.tail(5))

print("\n", df.shape)

print("\n", df.columns)

print("\n", df.index)

print("\n", df.dtypes)

print("\n", df.isna().sum())

print("\n", df["Pclass"].unique())

print("\n", df["Pclass"].value_counts())

print("\n", df.describe())

print("\n", df['Age'].mean())

print("\n", df['Age'].max())

print("\n", df['Age'].min())

print("\n", df['Fare'].sum())

print("\n", df.isnull().sum().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\n", df['Age'].isnull().sum())

print("\n", df['Sex'].nunique())

df['Sex'] = df['Sex'].map({"male": '0', "female": "1"})

print("\n",df['Name'])

df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
df['First Name'] = df['Name'].apply(lambda x: ' '.join(x.split(',')[1:]))

df.drop(['PassengerId'], axis=1, inplace=True)

df.rename(columns={'Sex': 'Gender', 'Name': 'Full Name', 'Surname': 'Last Name', 'First Name': 'First Name'}, inplace=True)

print("\nAll passengers in third class:")
print(df[df['Pclass'] == 3].reset_index(drop=True))

df_aged_women = df[(df['Age'] > 60) & (df['Gender'] == '1')]
print("\nWomen aged over 60:")
print(df_aged_women)
if df_aged_women['Survived'].all() == 1:
    print("\nAll of these women survived.")
else:
    print("\nSome of these women did not survive.")

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df_num = df.select_dtypes(include=numerics)
print("\nNumeric columns:")
print(df_num)

df_cat = df.select_dtypes(include=['object'])
print("\nText columns:")
print(df_cat)

print("\nUnique values in 'Embarked' column:")
print(df['Embarked'].unique())

young_survived = df[df['Age'] < 30]['Survived']
old_survived = df[df['Age'] > 60]['Survived']
print("\nSurvival rate: \n\t among young people {}%, \n\t among old people {}%.".format(round(100 * young_survived.mean(), 1), round(100 * old_survived.mean(), 1)))

male_survived = df[df['Gender'] == '0']['Survived']
female_survived = df[df['Gender'] == '1']['Survived']
print("\nSurvival rate: \n\t among women {}%, \n\t among men {}%.".format(round(100 * female_survived.mean(), 1), round(100 * male_survived.mean(), 1)))

print("\nMost common names among Titanic passengers:")
print(df['First Name'].value_counts().head())

import pandas as pd

data = pd.read_excel('WHO POP TB all.xls')

total_deaths = data['TB deaths'].sum()
total_deaths = int(total_deaths)
max_deaths = data['TB deaths'].max()
max_deaths = int(max_deaths)
min_deaths = data['TB deaths'].min()
min_deaths = int(min_deaths)
mean_deaths = data['TB deaths'].mean()
mean_deaths = int(mean_deaths)

max_deaths_countries = data[data['TB deaths'] == max_deaths]['Country']
min_deaths_countries = data[data['TB deaths'] == min_deaths]['Country']

data['TB deaths (per 100,000)'] = data['TB deaths'] * 100 / data['Population (1000s)']

max_mortality_countries = data[data['TB deaths (per 100,000)'] == data['TB deaths (per 100,000)'].max()]['Country']
min_mortality_countries = data[data['TB deaths (per 100,000)'] == data['TB deaths (per 100,000)'].min()]['Country']

print(f"У всіх країнах світу було загинуто близько {total_deaths} чоловік від туберкульозу у 2013 році.")
print(f"Медіана показує, що половина цих країн мала менше {data['TB deaths'].median()} смертей.")
print(f"Середня кількість смертей склала {mean_deaths}.")
print(f"Найменш постраждалими {min_deaths_countries.values[0]} та {max_deaths_countries.values[0]} з відповідно {min_deaths} і {max_deaths} померлими відповідно.")
print(f"Найбільше постраждали {min_mortality_countries.values[0]} та {max_mortality_countries.values[0]} з понад {data['TB deaths (per 100,000)'].min()} і {data['TB deaths (per 100,000)'].max()} смертельними випадками на 100 000 жителів.")


import pandas as pd
from datetime import datetime

# 1. Зчитуємо дані з файлу, прибираємо зайві пробіли перед заголовками
london = pd.read_csv('London_2014.csv', skipinitialspace=True)

# 2. Виводимо дані для стовпчика 'WindDirDegrees<br />'
print(london['WindDirDegrees<br />'])

# 3. Перейменовуємо стовпчик 'WindDirDegrees<br />' на 'WindDirDegrees'
london = london.rename(columns={'WindDirDegrees<br />' : 'WindDirDegrees'})

# 4. Прибираємо зайві символи в значеннях стовпчика 'WindDirDegrees'
london['WindDirDegrees'] = london['WindDirDegrees'].str.rstrip('<br />')

# 5. Виводимо інформацію щодо пропущених значень в таблиці
print(london.info())

# 6. Виводимо дані стовпчика 'Events'
print(london['Events'])

# 7. Перевіряємо дані стовпчика на наявність нульових значень
print(london['Events'].isnull())

# 8. Підраховуємо кількість нульових значень по стовпчику 'Events'
print(london['Events'].isnull().sum())

# 9. Прибираємо рядки з пустими даними
london = london.dropna()

# 10. Виводимо інформацію про тип даних в стовпчиках
print(london.dtypes)

# 11. Змінюємо тип даних в стовпчику 'WindDirDegrees' з строкового на числовий
london['WindDirDegrees'] = london['WindDirDegrees'].astype('int64')

# 12. Змінюємо тип даних в стовпчику 'GMT' на тип дата
london['GMT'] = pd.to_datetime(london['GMT'])

# 13. Перевіряємо тип даних у таблиці
print(london.dtypes)

# 14. Виводимо дані на 4 червня 2014 р.
print(london[london['GMT'] == datetime(2014, 6, 4)])

# 15. Виводимо діапазон даних з 8 грудня по 12 грудня
start = datetime(2014, 12, 8)
end = datetime(2014, 12, 12)
print(london[(london['GMT'] >= start) & (london['GMT'] <= end)])

# 16. Вибираємо всі дні з північним вітром
north_wind_days = london[(london['WindDirDegrees'] >= 350) | (london['WindDirDegrees'] <= 10)]
print(north_wind_days)

# 17. Виводимо всі дані між 1 та 14 квітня
start_date = datetime(2014, 4, 1)
end_date = datetime(2014, 4, 14)
print(london[(london['GMT'] >= start_date) & (london['GMT'] <= end_date)])
