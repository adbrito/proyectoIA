import fasttext


def get_label(s):
    return s.replace("__label__", "")

# Load Moldel
model = fasttext.load_model("model-es.ftz")

tweet = "Por qué no traen a Ecuador está vacuna? Motivos políticos, económicos o de salud?"

l = model.predict(tweet, k=3)

print(l)
label = get_label(l[0][0])
value = l[1][0]

print("Tweet: ",tweet)
print("Label: ",label)
print("Value: ", value)
