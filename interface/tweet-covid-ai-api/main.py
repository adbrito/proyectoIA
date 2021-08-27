from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import fasttext
import emoji

# uvicorn main:app --reload
# git push heroku master

# Load Moldel
model = fasttext.load_model("model-es.ftz")

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_label(s):
    return s.replace("__label__", "")

def clean_tweet(content):
    content_list = content.split(" ")
    line_filter = []
    for s in content_list:
        # remove hastags, mentions and links
        if(s.count("#") > 0 or s.count("@") > 0 or s.count("https:") > 0 or s.count("http:") > 0):
            continue
        line_filter.append(s)

    line_filter_s = " ".join(line_filter)
    line_filter_s =" ".join(line_filter_s.split("\n"))
    line_filter_s =" ".join(line_filter_s.split("\t"))
    return line_filter_s



class Tweet(BaseModel):
    content: str



@app.post("/")
def post_predict(tweet: Tweet):
    tweet_content = clean_tweet(tweet.content)

    tweet_content=emoji.demojize(tweet_content,language='es')
    tweet_content = tweet_content.replace(":"," ")

    print("To Predict Tweet: ",tweet_content)
    l = model.predict(tweet_content, k=1)
    label = get_label(l[0][0])
    value = l[1][0]

    return {"label": label, "value": value}
