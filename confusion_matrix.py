import os
import csv
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score,recall_score
import matplotlib.pyplot as plt
import numpy as np
import random

encoding_files = "utf-8"


# open files
tweets_predict = open('tweets_predict_fix.csv', "r", encoding=encoding_files)
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

#print("Actual: ", y_actual)
#print("Predicted: ", y_predicted)

cm = confusion_matrix(y_actual, y_predicted, labels)

# Accuracy
accuracy=accuracy_score(y_actual, y_predicted)
print("Labels: ",labels)
print("Accuracy: ",accuracy)

# Precision
precision=precision_score(y_actual, y_predicted, average='micro',labels=labels)
print("GLobal Precision: ", precision)

precision_label=precision_score(y_actual, y_predicted, average=None,labels=labels)
print("Label Precision: ", precision_label)

# Recall: Sensibilidad
recall=recall_score(y_actual, y_predicted, average='micro',labels=labels)
print("Global Sensibilidad: ", recall)

recall_label=recall_score(y_actual, y_predicted, average=None,labels=labels)
print("Label Sensibilidad: ", recall_label)

# Plot
cmap=plt.cm.Blues

fig, ax = plt.subplots(figsize=(10, 5))
#map color cmap
cax = ax.matshow(cm,cmap=cmap)
plt.title('Confusion Matrix', fontsize=20)
plt.ylabel('Actual Label', fontsize=16)
plt.xlabel('Predicted Label', fontsize=16)

# color bar
plt.colorbar(cax)

ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)

thresh = cm.max() / 2.

for (i, j), z in np.ndenumerate(cm):
    ax.text(j, i, '{value:0.1f}'.format(value=z), ha='center', va='center',color="white" if cm[i, j] > thresh else "black")



plt.show()
# Closing file
tweets_predict.close()
