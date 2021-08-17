import fasttext

model = fasttext.load_model("model-es.ftz")
print('***************************************************')
print('Frase: amor y felicidad')
l=model.predict("amor y felicidad", k=3)
print(l)

l=model.predict("amor y felicidad", k=1)
print(l)
print('***************************************************')
print('Frase: tanta muerte y destrucción')
l=model.predict("tanta muerte y destrucción", k=3)
print(l)

l=model.predict("tanta muerte y destrucción", k=1)
print(l)


print('***************************************************')
print('Frase: es un día nuevo')
l=model.predict("es un día nuevo", k=3)
print(l)

l=model.predict("es un día nuevo", k=1)
print(l)