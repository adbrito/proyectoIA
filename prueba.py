import fasttext
import sys
import os
import nltk
nltk.download('punkt')
import csv
import datetime
from bs4 import BeautifulSoup
import re
import itertools
import emoji


#####################################################################################
#
# DATA CLEANING
#
#####################################################################################

# emoticons
def load_dict_smileys():
    
    return {
        ":‑)":"sonriente",
        ":-]":"sonriente",
        ":-3":"sonriente",
        ":->":"sonriente",
        "8-)":"sonriente",
        ":-}":"sonriente",
        ":)":"sonriente",
        ":]":"sonriente",
        ":3":"sonriente",
        ":>":"sonriente",
        "8)":"sonriente",
        ":}":"sonriente",
        ":o)":"sonriente",
        ":c)":"sonriente",
        ":^)":"sonriente",
        "=]":"sonriente",
        "=)":"sonriente",
        ":-))":"sonriente",
        ":‑D":"sonriente",
        "8‑D":"sonriente",
        "x‑D":"sonriente",
        "X‑D":"sonriente",
        ":D":"sonriente",
        "8D":"sonriente",
        "xD":"sonriente",
        "XD":"sonriente",
        "Xd":"sonriente",
        ":‑(":"triste",
        ":‑c":"triste",
        ":‑<":"triste",
        ":‑[":"triste",
        ":(":"triste",
        ":c":"triste",
        ":<":"triste",
        ":[":"triste",
        ":-||":"triste",
        ">:[":"triste",
        ":{":"triste",
        ":@":"triste",
        ">:(":"triste",
        ":'‑(":"triste",
        ":'(":"triste",
        ":‑P":"jugueton",
        "X‑P":"jugueton",
        "x‑p":"jugueton",
        ":‑p":"jugueton",
        ":‑Þ":"jugueton",
        ":‑þ":"jugueton",
        ":‑b":"jugueton",
        ":P":"jugueton",
        "XP":"jugueton",
        "xp":"jugueton",
        ":p":"jugueton",
        ":Þ":"jugueton",
        ":þ":"jugueton",
        ":b":"jugueton",
        "<3":"amor",
        ":*":"amoroso"
        }

# self defined contractions
def load_dict_contractions():
    
    return {
        "pq":"porque",
        "xq":"porque",
        "tb":"tambien",
        "fyi":"para tu atencion",
        "k":"que",
        "bro":"hermano",
        "bb": "bebe"
        }


def tweet_cleaning_for_sentiment_analysis(tweet):    
    
    #Escaping HTML characters
    tweet = BeautifulSoup(tweet).get_text()
   
    #Special case not handled previously.
    tweet = tweet.replace('\x92',"'")
    
    #Removal of hastags/account
    tweet = ' '.join(re.sub("(@[\s?_?\wA-Za-z0-9]+)|(#[\s?_?\w]+)", "", tweet).split())
    
    #Removal of address
    tweet = ' '.join(re.sub("(\w+:\/\/\w+\.?\S+)", "", tweet).split())
    
    #Removal of Punctuation
    tweet = ' '.join(re.sub("[\.\,\!\?\¿\:\;\-\=\&\´\``\|\[\]\*\)\(\%\>\<\#\/]", "", tweet).split())
    
    #Lower case
    tweet = tweet.lower()
    
    #CONTRACTIONS source: https://en.wikipedia.org/wiki/Contraction_%28grammar%29
    CONTRACTIONS = load_dict_contractions()
    # tweet = tweet.replace("’","'")
    words = tweet.split()
    reformed = [CONTRACTIONS[word] if word in CONTRACTIONS else word for word in words]
    tweet = " ".join(reformed)
    
    # Standardizing words
    tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))
    
    #Deal with emoticons source: https://en.wikipedia.org/wiki/List_of_emoticons
    SMILEY = load_dict_smileys()  
    words = tweet.split()
    reformed = [SMILEY[word] if word in SMILEY else word for word in words]
    tweet = " ".join(reformed)
    
    #Deal with emojis
    tweet = emoji.demojize(tweet)

    tweet = tweet.replace(":"," ")
    tweet = ' '.join(tweet.split())

    return tweet



#####################################################################################
#
# DATA PROCESSING
#
#####################################################################################

def transform_instance(row):
    cur_row = []
    #Prefix the index-ed label with __label__
    label = "__label__" + row[4]  
    cur_row.append(label)
    cur_row.extend(nltk.word_tokenize(tweet_cleaning_for_sentiment_analysis(row[2].lower())))
    return cur_row


def preprocess(input_file, output_file, keep=1):
    i=0
    with open(output_file, 'w') as csvoutfile:
        csv_writer = csv.writer(csvoutfile, delimiter=' ', lineterminator='\n')
        with open(input_file, 'r', newline='',encoding='latin1') as csvinfile: #,encoding='latin1'
            csv_reader = csv.reader(csvinfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                if row[4]!="MIXED" and row[4].upper() in ['POSITIVE','NEGATIVE','NEUTRAL'] and row[2]!='':
                    row_output = transform_instance(row)
                    csv_writer.writerow(row_output)
                    # print(row_output)
                i=i+1
                if i%10000 ==0:
                    print(i)
            
# Preparing the training dataset        
preprocess('data.csv', 'tweets.train')

# Preparing the validation dataset        
# preprocess('data.csv', 'tweets.validation')
preprocess('tester.csv', 'tweets.validation')



#####################################################################################
#
# UPSAMPLING
#
#####################################################################################

def upsampling(input_file, output_file, ratio_upsampling=1):
    # Create a file with equal number of tweets for each label
    #    input_file: path to file
    #    output_file: path to the output file
    #    ratio_upsampling: ratio of each minority classes vs majority one. 1 mean there will be as much of each class than there is for the majority class 
    
    i=0
    counts = {}
    dict_data_by_label = {}

    # GET LABEL LIST AND GET DATA PER LABEL
    with open(input_file, 'r', newline='',encoding="utf-8") as csvinfile:
        csv_reader = csv.reader(csvinfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            counts[row[0].split()[0]] = counts.get(row[0].split()[0], 0) + 1
            if not row[0].split()[0] in dict_data_by_label:
                dict_data_by_label[row[0].split()[0]]=[row[0]]
            else:
                dict_data_by_label[row[0].split()[0]].append(row[0])
            i=i+1
            if i%10000 ==0:
                print("read" + str(i))

    # FIND MAJORITY CLASS
    majority_class=""
    count_majority_class=0
    for item in dict_data_by_label:
        if len(dict_data_by_label[item])>count_majority_class:
            majority_class= item
            count_majority_class=len(dict_data_by_label[item])  
    
    # UPSAMPLE MINORITY CLASS
    data_upsampled=[]
    for item in dict_data_by_label:
        data_upsampled.extend(dict_data_by_label[item])
        if item != majority_class:
            items_added=0
            items_to_add = count_majority_class - len(dict_data_by_label[item])
            while items_added<items_to_add:
                data_upsampled.extend(dict_data_by_label[item][:max(0,min(items_to_add-items_added,len(dict_data_by_label[item])))])
                items_added = items_added + max(0,min(items_to_add-items_added,len(dict_data_by_label[item])))

    # WRITE ALL
    i=0

    with open(output_file, 'w') as txtoutfile:
        for row in data_upsampled:
            txtoutfile.write(row+ '\n' )
            i=i+1
            if i%10000 ==0:
                print("writer" + str(i))


upsampling( 'tweets.train','uptweets.train')
# No need to upsample for the validation set. As it does not matter what validation set contains.


#####################################################################################
#
# TRAINING
#
#####################################################################################

# Full path to training data.
training_data_path ='uptweets.train' 
validation_data_path ='tweets.validation'
model_path =''
model_name="model-es"

def train():
    print('Training start')
    try:
        hyper_params = {"lr": 0.01,
                        "epoch": 20,
                        "wordNgrams": 2,
                        "dim": 20}     
                               
        print(str(datetime.datetime.now()) + ' START=>' + str(hyper_params) )

        # Train the model.
        model = fasttext.train_supervised(input=training_data_path, **hyper_params)
        print("Model trained with the hyperparameter \n {}".format(hyper_params))

        # CHECK PERFORMANCE
        print(str(datetime.datetime.now()) + 'Training complete.' + str(hyper_params) )
        
        model_acc_training_set = model.test(training_data_path)
        model_acc_validation_set = model.test(validation_data_path)
        
        # DISPLAY ACCURACY OF TRAINED MODEL
        text_line = str(hyper_params) + ",accuracy:" + str(model_acc_training_set[1])  + ", validation:" + str(model_acc_validation_set[1]) + '\n' 
        print(text_line)
        
        #quantize a model to reduce the memory usage
        model.quantize(input=training_data_path, qnorm=True, retrain=True, cutoff=100000)
        
        print("Model is quantized!!")
        model.save_model(os.path.join(model_path,model_name + ".ftz"))                
    
        ##########################################################################
        #
        #  TESTING PART
        #
        ##########################################################################            
        model.predict(['why not'],k=3)
        model.predict(['this player is so bad'],k=1)
        
    except Exception as e:
        print('Exception during training: ' + str(e) )


# Train your model.
train()