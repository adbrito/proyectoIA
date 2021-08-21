import os
import csv
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import random

encoding_files = "utf-8"


# open files
tweets_predict = open('tweets_predict.csv', "r", encoding=encoding_files)
csv_reader = csv.reader(tweets_predict, delimiter=',')

y_actual = []
y_predicted = []


labels = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']

for row in csv_reader:
    y_predicted.append(row[2])

    if(row[1] in labels):
        y_actual.append(row[1])
    else:
        y_actual.append(random.choice(labels))

cm = confusion_matrix(y_actual, y_predicted, labels)

fig, ax = plt.subplots(figsize=(10, 5))
ax.matshow(cm)
plt.title('Matriz de Confusión', fontsize=20)
plt.ylabel('Etiqueta Actual', fontsize=20)


for (i, j), z in np.ndenumerate(cm):
    ax.text(j, i, '{value:0.1f}'.format(value=z), ha='center', va='center')

plt.show()
# Closing file
tweets_predict.close()
