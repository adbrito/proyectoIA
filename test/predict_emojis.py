import fasttext


def get_label(s):
    return s.replace("__label__", "")


# Load Moldel
model = fasttext.load_model("model-es.ftz")

emojis = [["🤔 🤔","Think"],["😂 😂","Laughter"],["😠 😠","Angry"],["😘 😊","Kiss:Smiling"],["😊 😘","Smiling:Kiss"]]

for i in emojis:
    emoji=i[0]
    description =i[1]

    l = model.predict(emoji, k=1)
    label = get_label(l[0][0])
    value = l[1][0]
    print("\n****************************")
    print("Emoji: ", emoji," ",description)
    print("Label: ", label)
    print("Value: ", value)
