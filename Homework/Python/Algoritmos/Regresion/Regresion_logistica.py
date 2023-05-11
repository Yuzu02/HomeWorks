# Algoritmo basico de regresion logistica
# Make by: @yuzu02 (GitHub)

"""
Los algoritmos de regresión son utilizados para predecir un valor numérico en base a un conjunto de datos.
Los más populares son Regresión lineal, Regresión logística y Regresión polinómica.

Pero en este caso, vamos a ver el algoritmo de regresion logistica.
"""

import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from sklearn.linear_model import LogisticRegression # pip install sklearn
from sklearn.datasets import make_classification 
from sklearn.model_selection import train_test_split

"""
Antes de, aclaremos que es una regresion logistica 

La regresion logistica es un metodo estadistico que trata de modelar la relacion
entre una variable dependiente y una o mas variables independientes mediante el
ajuste de una funcion logistica.

La regresion logistica es usada para clasificar datos, es decir, predecir a que
clase pertenece un dato.
 
Bien dicho esto

Supongamos que tenemos un conjunto de datos que representa si un paciente tiene o no una enfermedad,
y las características del paciente que podrían estar relacionadas con la enfermedad, como la edad, 
el género, el índice de masa corporal (IMC), etc. Queremos entrenar un modelo de regresión 
logística para predecir si un paciente tiene o no la enfermedad en función de estas características.

"""

# Generar datos sintéticos
X, y = make_classification(n_samples=1000, n_features=5, n_informative=3, n_redundant=1, random_state=1)

"""
Aclaracion : Cuando entrenamos un modelo de regresion logistica, lo que hacemos es
encontrar la mejor linea que separe los datos. .

Y ahora te preguntaras, ¿Que son los datos sinteticos?

Los datos sinteticos son datos que se generan de forma artificial, es decir, no son datos reales.
Estos datos se generan con el fin de probar algoritmos de machine learning y deep learning tambien probabilidad y estadistica.
"""

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

"""
Aca, dividimos los datos en dos conjuntos, uno de entrenamiento y otro de prueba.

El conjunto de entrenamiento es el conjunto de datos que usamos para entrenar el modelo.
El conjunto de prueba es el conjunto de datos que usamos para probar el modelo.
"""

# Vamos a visualizar los datos utilizando un diagrama de dispersión en 2D 
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

"""
Con este diagrama podemos ver que si hay una relación no lineal entre las características y las etiquetas de clase.

En el diagrama, podemos ver que los datos se pueden separar en dos grupos, uno con etiqueta 0 y otro con etiqueta 1.

Esto significa que podemos usar un modelo de regresión logística para clasificar los datos.
"""

# Ahora creamos un objeto de regresión logística
regresion_logistica = LogisticRegression(random_state=1)

"""
Un objeto de regresión logística tiene métodos y atributos que nos permiten entrenar el modelo y predecir valores.
"""

# Entrenar el modelo con los datos de entrenamiento
regresion_logistica.fit(X_train, y_train)

"""
Entrenar el modelo significa encontrar la mejor linea que separe los datos.
"""

# Evaluar la precisión del modelo en los datos de prueba
precision = regresion_logistica.score(X_test, y_test)

# Imprimir la precisión del modelo
print(f"La precisión del modelo es {precision:.2f}")

"""
La precisión del modelo es 0.91

Esto significa que el modelo es capaz de predecir correctamente el 91% de los datos de prueba.
"""
