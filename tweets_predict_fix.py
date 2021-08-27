import os
import csv
import fasttext
import emoji

encoding_files = "utf-8" 


# Load Moldel
model = fasttext.load_model("model-es.ftz")

# open files
tweets = open('tweets_predict.csv', "r", encoding=encoding_files)
csv_reader = csv.reader(tweets, delimiter=',')


# output files
file_output = open('tweets_predict_fix.csv', "w", encoding=encoding_files, newline='')

header = ['date','label_actual','label_predicted', 'value', 'content']
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
    
    tweet=row[4]

    #print('***************************************************')
    # print('Frase: ',tweet)
    try:
        tweet=emoji.demojize(tweet,language='es')
        tweet = tweet.replace(":"," ")
        l=model.predict(tweet, k=1)
        # print(l[0])
        label=get_label(l[0][0])
        value = l[1][0]
        line=[row[0],row[1],label,value,tweet]
        csv_writer.writerow(line)
    except:
        print("Line: ",current_line," ",tweet)

    #l=model.predict(tweet, k=3)
    #print(l)
    current_line += 1

# Closing file
tweets.close()
file_output.close()
