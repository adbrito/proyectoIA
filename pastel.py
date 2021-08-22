# pylint: disable=missing-module-docstring
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("tweets_predict.csv", sep=",")

sentiments = {}

labels = []
values = []

for d in range(len(df)):
    label_predicted = df["label_predicted"][d]
    if label_predicted in sentiments:
        sentiments[label_predicted] += 1
    else:
        sentiments[label_predicted] = 1

for key in sentiments.keys():
    labels.append(key)
    values.append(sentiments[key])

plt.ion()
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title('My Title')
plt.axis('equal')
plt.savefig('pastel.png')

print(labels)
print(values)
