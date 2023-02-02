import pymongo
import pandas as pd
import json

# Conectamos nuestro MongoDB a Python
client = pymongo.MongoClient("mongodb://localhost:27017")
# Con Pandas leemos el archivo CSV de los comentarios a importar
df = pd.read_csv("Comentarios_RADA.csv")
# Convertimos los datos a un diccionario para poder importarlos de manera ordenada y separada a MongoDB
data = df.to_dict(orient = "records")
# Accedemos a la base de datos donde insertaremos los comentarios
db = client["Prueba"]
# Con insert_many importamos los comentarios a la coleccion Comentarios de la BD Prueba
db.Comentarios.insert_many(data)