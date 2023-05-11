# Algoritmo basico de regresion lineal
# Make by: @yuzu02 (GitHub)

"""
Los algoritmos de regresión son utilizados para predecir un valor numérico en base a un conjunto de datos.
Los más populares son Regresión lineal, Regresión logística y Regresión polinómica.

Pero en este caso, vamos a ver el algoritmo de regresion lineal.
"""
# Importamos las librerias necesarias
import numpy as np # pip install numpy (En la terminal)
import matplotlib.pyplot as plt # pip install matplotlib
from sklearn.linear_model import LinearRegression # pip install sklearb
'''
Antes de, aclaremos que es una regresion lineal

La regresion lineal es un metodo estadistico que trata de modelar la relacion
entre una variable dependiente y una o mas variables independientes mediante el
ajuste de una ecuacion lineal.
'''

# DIgamos que tenemos un conjunto de datos de horas de estudio y calificaciones
horas_estudio = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
calificacion = np.array([60, 70, 80, 85, 90, 92, 94, 96, 98, 100])

"""
Estos datos son de ejjemplo ,esto quiere decir que puedes usar cualesquiera datos
que tengas a la mano para hacer la regresion lineal.

Ahora, vamos a graficar estos datos para ver si hay una relacion lineal entre
las horas de estudio y la calificacion.
"""

# Ahora, grafiquemos los datos
plt.scatter(horas_estudio, calificacion)
plt.xlabel('Horas de estudio')
plt.ylabel('Calificación')
plt.show()

"""
De la grafica, podemos ver que hay una relacion lineal entre las horas de estudio
y la calificacion. Esto significa que podemos usar la regresion lineal para
predecir la calificacion de un estudiante si sabemos cuantas horas estudio.
"""

# Bien, ahora, vamos a crear un modelo de regresion lineal
regresion_lineal = LinearRegression()

"""
Acabamos de crear un objeto de regresion lineal. Este objeto tiene metodos y
atributos que nos permiten entrenar el modelo y predecir valores.
"""

# Entrenamos el modelo con los datos de entrenamiento (horas_estudio y calificacion)
regresion_lineal.fit(horas_estudio.reshape(-1, 1), calificacion)

"""
Aclaracion : Cuando entrenamos un modelo de regresion lineal, lo que hacemos es
encontrar la mejor linea que se ajuste a los datos. En este caso, la mejor linea
que se ajusta a los datos es la que pasa por el medio de todos los puntos.

Para encontrar la mejor linea, el modelo utiliza el metodo de minimos cuadrados
que consiste en minimizar la suma de los cuadrados de los residuos (diferencia
entre el valor real y el valor estimado por el modelo) de los puntos respecto a
la linea.
"""

# Ahora, vamos a predecir la calificacion de un estudiante que estudio 15 horas para un examen en base a nuestro modelo
prediccion = regresion_lineal.predict([[15]])

"""
Aclaracion : Cuando predecimos un valor, lo que hacemos es encontrar el valor
que corresponde a la linea de regresion lineal para el valor de entrada.
"""

# Imprimimos la prediccion de la calificacion posible del estudiante
print(f"La calificación estimada para un estudiante que estudia 15 horas es {prediccion[0]:.2f}")
