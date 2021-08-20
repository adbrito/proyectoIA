import os
import csv
import random

encoding_files = "utf-8"

os.system('python leermodelo.py')


# open files
tweets_predict = open('tweets_predict_all.csv', "r", encoding=encoding_files)
csv_reader = csv.reader(tweets_predict, delimiter=',')


# output files
file_output = open('tweets_predict.csv', "w", encoding=encoding_files, newline='')

header = ['date', 'label', 'value']
# write the header
csv_writer = csv.writer(file_output)
csv_writer.writerow(header)


# Select random items
#################################
num_to_select = 100 # set the number to select here.
#################################

list_of_random_items = random.sample(list(csv_reader)[1:], num_to_select)

for i in list_of_random_items:
    csv_writer.writerow(i)

# Closing file
tweets_predict.close()
file_output.close()


