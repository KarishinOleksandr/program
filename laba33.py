import pandas as pd
import numpy as np
import seaborn as sns

titanic = pd.read_csv('titanic_data.csv')
print(titanic.head(10))

print(titanic.columns)

print(titanic.shape)

survived_class = titanic.groupby(['Pclass'])['Survived'].sum().reset_index()
print('\n', survived_class)

titanic["embark_town"] = titanic.Embarked.map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
print(titanic.head(10))

avg_fare_town = titanic.groupby(['embark_town'])['Fare'].mean().reset_index()
print('\n',avg_fare_town)

avg_fare_town_sex = titanic.groupby(['embark_town', 'Sex'])['Fare'].mean().reset_index()
print(avg_fare_town_sex)

avg_fare_age_town_sex = titanic.groupby(['embark_town', 'Sex']).agg({'Fare': 'mean', 'Age': 'mean'}).reset_index()
print('\n',avg_fare_age_town_sex)

avg_age_sex_town = titanic.groupby(['embark_town', 'Sex'])['Age'].mean().reset_index()
print(avg_age_sex_town)

age_range_by_town_sex = titanic.groupby(['embark_town', 'Sex'])['Age'].apply(lambda x: x.max() - x.min()).reset_index()
print('\n',age_range_by_town_sex)

fare_age_ratio = titanic.groupby(['embark_town', 'Sex']).apply(lambda x: (x['Fare']/x['Age']).mean()).reset_index(name='fare_age_ratio')
print(fare_age_ratio)

unique_ages_by_town_sex = titanic.groupby(['embark_town', 'Sex'])['Age'].apply(set).reset_index()
print(unique_ages_by_town_sex)

agg_stats = titanic.groupby(['embark_town', 'Sex']).agg({'Fare': 'mean', 'Age': 'median'}).reset_index()
print('\n',agg_stats)

full_agg_stats = titanic.groupby(['embark_town', 'Sex']).agg({'Fare': ['sum', 'mean'], 'Age': ['median', 'min', 'max']}).reset_index()
print(full_agg_stats)

avg_fare_by_age_group = titanic.groupby('Sex')['Fare'].transform('mean')
titanic['avg_fare_by_age_group'] = avg_fare_by_age_group
print(titanic[['Sex', 'avg_fare_by_age_group']].drop_duplicates())