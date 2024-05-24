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

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

tweets = pd.read_csv('tweets.csv')
print(tweets.head())

print("Shape of the dataframe:", tweets.shape)

print("Number of tweets in each language:")
print(tweets['lang'].value_counts())

def language(df):
    if df["lang"] == "en":
        return "English"
    elif df["lang"] == "es":
        return "Spanish"
    else:
        return "Other"

tweets["lang"] = tweets.apply(language, axis=1)
print("Number of tweets in each language after transformation:")
print(tweets['lang'].value_counts())

print("Data in the 'time' column:")
print(tweets['time'].head())

date_format = "%Y-%m-%dT%H:%M:%S" 
tweets["time"] = pd.to_datetime(tweets["time"], format=date_format)

data = pd.concat([tweets['handle'], tweets['text']], axis=1)

data.dropna(axis=0, inplace=True)

print("Number of posts for each candidate:")
print(data['handle'].value_counts())

sns.countplot(x='handle', data=tweets)
plt.savefig("tweet.png")

# 11. Analyze the proportion of retweets for each candidate
plt.style.use('ggplot')

plt.figure(figsize=(13, 6))
plt.subplot(121)
tweets[tweets["handle"] == "realDonaldTrump"]["is_retweet"].value_counts().plot.pie(autopct="%1.0f%%", wedgeprops={"linewidth": 1, "edgecolor": "k"}, shadow=True, fontsize=13, explode=[.1, 0.09], startangle=20, colors=["#ff0026", "#fbff00"])
plt.ylabel("")
plt.title("Percentage of Trump retweets")

plt.subplot(122)
tweets[tweets["handle"] == "HillaryClinton"]["is_retweet"].value_counts().plot.pie(autopct="%1.0f%%", wedgeprops={"linewidth": 1, "edgecolor": "k"}, shadow=True, fontsize=13, explode=[.09, 0], startangle=60, colors=["#0095ff", "#fbff00"])
plt.ylabel("")
plt.title("Percentage of Hillary retweets")
plt.savefig("pieplot.png")

# 12. Information about the TextBlob library
# TextBlob is a Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

# 13. Classify tweets into positive, neutral, and negative sentiments using TextBlob
bloblist_desc = list()
df_tweet_descr_str = tweets['text'].astype(str)

for row in df_tweet_descr_str:
    blob = TextBlob(row)
    bloblist_desc.append((row, blob.sentiment.polarity, blob.sentiment.subjectivity))

df_tweet_polarity_desc = pd.DataFrame(bloblist_desc, columns=['sentence', 'sentiment', 'polarity'])

def f(df_tweet_polarity_desc):
    if df_tweet_polarity_desc['sentiment'] > 0:
        val = "Positive"
    elif df_tweet_polarity_desc['sentiment'] == 0:
        val = "Neutral"
    else:
        val = "Negative"
    return val

df_tweet_polarity_desc['Sentiment_Type'] = df_tweet_polarity_desc.apply(f, axis=1)

plt.figure(figsize=(10, 10))
sns.set_style("whitegrid")
ax = sns.countplot(x="Sentiment_Type", data=df_tweet_polarity_desc)
plt.savefig("text.png")

import pandas as pd
from collections import Counter
import re

# Assuming 'data' DataFrame contains the text of the tweets
# 14. Remove all unnecessary characters from the text of the posts in the DataFrame data
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove mentions
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove non-alphanumeric characters and symbols
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    return text

data['clean_text'] = data['text'].apply(clean_text)

# 15. Determine the most common word in the tweets
all_words = ' '.join(data['clean_text'])
words_list = all_words.split()
word_counts = Counter(words_list)
most_common_word = word_counts.most_common(1)[0][0]
print("The most common word in the tweets is:", most_common_word)
