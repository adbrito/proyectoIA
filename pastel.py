# pylint: disable=missing-module-docstring
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("tweets_predict_all.csv", sep=",")

sentiments = {}

my_colors = ['lightblue','lightsteelblue','silver']

my_explode = (0, 0, 0.1)

labels = []
values = []

tweets = 0

for d in range(len(df)):
    tweets += 1
    label_predicted = df["label"][d]
    if label_predicted in sentiments:
        sentiments[label_predicted] += 1
    else:
        sentiments[label_predicted] = 1

for key in sentiments.keys():
    labels.append(key)
    values.append(sentiments[key])

plt.ion()
plt.pie(values,labels=labels,autopct='%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode)
plt.title('Proporción de los sentimientos encontrados en los tweets de los ecuatorianos')
plt.axis('equal')
plt.savefig('pastel.png')

print(labels)
print(values)
print(tweets)
