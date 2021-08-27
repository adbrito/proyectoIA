"# proyectoIA" 

Link del dataset betsentiment-ES-tweets-sentiment-teams.csv(para pruebas): https://drive.google.com/file/d/1XBw2PdbZqQgiHwlVNBV-0-0wu2iM4bie/view?usp=sharing
Link del dataset data.csv (para el entrenamiento de la red): https://drive.google.com/file/d/1L2tt9KmKzUlqQaRuW5hmOcPVxMwh4JP3/view?usp=sharing

## Use 
### main.py generate 100 random elements
```
python main.py

```
Los scripts son los siguientes:
	prueba.py --> Entrena al modelo con los hiperparametros mostrados en el documento
	confusion_matrix.py --> Realiza la matriz de confusion
	leermodelo.py --> Llama a filter_tweets.py para procesar los tweets extraidos en b.json a un archivo csv y una vez que termina, leermodelo lee el csv y lo pasa en el modelo, el resultado es guardado en el archivo tweets_predict_all
Existe el archivo requirements.txt para instalar las dependencias


# interface

## tweet-covid-ai
App Frontend en javascript
'''
npm start
'''
Si se hacen pruebas locales, connectar con la api en Forms.jsx

## tweet-covid-ai-api

App Backend en python con FastAPI

Install requeriments.txt
'''
uvicorn main:app --reload
'''
