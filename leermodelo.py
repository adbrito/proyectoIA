import os
import csv
import fasttext

encoding_files = "utf-8" 

os.system('python filter_tweets.py')

# Load Moldel
model = fasttext.load_model("model-es.ftz")

# open files
tweets = open('tweets.csv', "r", encoding=encoding_files)
csv_reader = csv.reader(tweets, delimiter=',')


# output files
file_output = open('tweets_predict_all.csv', "w", encoding=encoding_files, newline='')

header = ['date', 'label','value', 'content']
# write the header
csv_writer = csv.writer(file_output)
csv_writer.writerow(header)

current_line = 1

def get_label(s):
    return s.replace("__label__","")


for row in csv_reader:
    if(current_line == 1):
        current_line += 1
        continue
    
    tweet=row[1]

    #print('***************************************************')
    # print('Frase: ',tweet)
    try:
        l=model.predict(tweet, k=1)
        # print(l[0])
        label=get_label(l[0][0])
        value = l[1][0]
        line=[row[0],label,value,tweet]
        csv_writer.writerow(line)
    except:
        print("Line: ",current_line," ",tweet)

    #l=model.predict(tweet, k=3)
    #print(l)
    current_line += 1

# Closing file
tweets.close()
file_output.close()
