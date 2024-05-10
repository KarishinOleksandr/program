import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FootballData = pd.read_csv('top250.csv')

print(FootballData.head())

print(FootballData.shape)

print(FootballData.describe())

print(FootballData.isnull().sum())

FootballData.dropna(inplace=True)

plt.style.use('ggplot')
FootballData[['Age', 'Market_value', 'Transfer_fee']].hist()
plt.tight_layout()
plt.savefig('Distribution.png')

sns.countplot(x='Position', data=FootballData)
plt.xticks(rotation=90)

sns.pointplot(x='Season', y='Season', data=FootballData['Season'].value_counts().reset_index().sort_values('Season'))
plt.xticks(rotation=90)
plt.xlabel('Season')
plt.ylabel('Number of Trades')

FootballData = FootballData.head(20)

FootballData.Transfer_fee = [float(i)/sum(FootballData.Transfer_fee) for i in FootballData.Transfer_fee]
FootballData.Age = [float(i)/sum(FootballData.Age) for i in FootballData.Age]

plt.figure(figsize=(16, 8))
sns.pointplot(x='Name', y='Age', data=FootballData, color='black')
sns.pointplot(x='Name', y='Transfer_fee', data=FootballData, color='red')
plt.xlabel("Football Player Names")
plt.ylabel("Transfer Fee vs. Age")
plt.savefig('graph.png')

sns.countplot(x='Team_from', data=FootballData)
plt.xticks(rotation=90)
plt.xlabel("Team From")
plt.ylabel("Count")
plt.savefig('graph1.png')

plt.figure(figsize=(7, 7))
labels = FootballData['League_to'].value_counts().index[:15]
sizes = FootballData['League_to'].value_counts().values[:15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Transfers Leagues to')
plt.savefig('graph2.png')

plt.figure(figsize=(10, 6))
sns.swarmplot(x="Position", y="Transfer_fee", hue="League_from", data=FootballData)
plt.xticks(rotation=15)
plt.title("Swarm Plot for Transfer Fee and Position")
plt.xlabel("Position")
plt.ylabel("Transfer Fee")
plt.savefig('graph3.png')
