# -*- coding: utf-8 -*-
"""AlgoritmoDeClasificacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yr_HyEnTYIo2zGO2W0v0gUMafuBa2ouz
"""

!pip install dnspython
!pip install sklearn
!pip install pymongo --upgrade
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
from sklearn.metrics import recall_score, precision_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pymongo
import numpy as np

client = pymongo.MongoClient("mongodb+srv://RADA_DB:RADA@rada.scmc2.mongodb.net/test")
db = client.IMDB
df = pd.DataFrame(list(db.Training.find()))
comment = list(df['Comment'].values.astype('U'))
sentiment = list(df['Sentiment'])
#Proceso del algoritmo de clasificación
train_comment, test_comment, train_sentiment, test_sentiment = A(comment, sentiment, test_size=0.2, random_state=42)
vectorizer = CountVectorizer(max_df =0.80, binary = True, stop_words = 'english', max_features = 10000)
vectorizer.fit(train_comment)
train_features = vectorizer.transform(train_comment)
tfidf_transformer = TfidfTransformer(smooth_idf=True,
                                    use_idf=True).fit(train_features)
trainingTF = tfidf_transformer.transform(train_features)
train_features = trainingTF.toarray()
#Entrenamiento del modelo
classifier = SGDClassifier(loss='hinge',   #'hinge'  #'log'
                            penalty='l2',
                            alpha=0.00001,
                            random_state=42,
                            max_iter=5,
                            tol=None)
classifier.fit(train_features, train_sentiment)
print('Predicción sobre el conjunto TRAIN:')
p = classifier.predict(train_features)
print (p)
print( 'Train Recall: ' + str(recall_score(train_sentiment, p) ))
print( "Train Precision: " + str(precision_score(train_sentiment, p)))
print( 'Matriz de confusión: ' )
print(confusion_matrix(train_sentiment, p, labels=[0, 1]))
print('-----------------------------------------')
#Evaluación del conjunto TEST
test_features = vectorizer.transform(test_comment)
p = classifier.predict(test_features)
print('Predicción sobre el conjunto TEST:')
print (p)
print( 'Test Recall: ' + str(recall_score(test_sentiment, p) ))
print( "Test Precision: " + str(precision_score(test_sentiment, p)))
print( 'Matriz de confusión: ' )
print(confusion_matrix(test_sentiment, p, labels=[0, 1]))
print('-----------------------------------------')

#En el siguiente fragmento de código se envia a clasificar un comentario nuevo, se clasifica y muestra si es positivo o negativo.
test = pd.DataFrame(list(db.Comentarios.find()))
comentarios_test = list(test['Comment'].values.astype('U'))
for comentario in comentarios_test:
  features = vectorizer.transform([comentario])
  p = classifier.predict(features)[0]
  #print('Predicción valor introducido:')
  #print('Frase: ' + comentario)
  #print (p)
  print('-----------------------------------------')
  print ("Frase introducida:   " + comentario)
  print ("Sentimiento: " + str(p))