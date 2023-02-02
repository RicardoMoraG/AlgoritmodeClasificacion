# Algoritmo de clasificacion de comentarios sobre peliculas.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Proyecto escolar final de 8vo semestre en la cual desarrollamos un algoritmo que clasifica reseñas de peliculas dependiendo de si son negativas o positivas. Utilizando 5000 comentarios para entrenarlo y otros 100 para testear, siendo estos almacenados en una base de datos de MongoDB.

* `algoritmodeclasificacion.py`: script en el cual se encuentra nuestro algoritmo clasificador de comentarios, el cual se entrenara y despues realizara un test para ver que tan eficiente es para clasificar.
* `Comentarios.json`: Archivo con 5000 comentarios, el cual se utilizara para entrenar nuestro algoritmo.
* `Comentarios_RADA.json`: Archivo con 100 comentarios sin clasificar, el cual se utilizara para realizar el test a nuestro algoritmo.
* `Pytho_A_Mongo_RADA.py`: script con el cual ingresaremos nuestros comentarios a una base de datos de MongoDB.
