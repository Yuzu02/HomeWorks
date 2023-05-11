# Algoritmo basico de regresion polinomica
# Make by: @yuzu02 (GitHub)

"""
Los algoritmos de regresión son utilizados para predecir un valor numérico en base a un conjunto de datos.
Los más populares son Regresión lineal, Regresión logística y Regresión polinómica.

Pero en este caso, vamos a ver el algoritmo de Regresión polinómica.
"""

import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib`
from sklearn.linear_model import LinearRegression # pip install scikit-learn
from sklearn.preprocessing import PolynomialFeatures

"""
Supongamos que tenemos un conjunto de datos que representa el precio de una casa en función de su tamaño.
Queremos entrenar un modelo de regresión polinómica para predecir el precio de una casa en función de su tamaño
"""

# Generar datos sintéticos
np.random.seed(0)
x = np.linspace(0, 5, 100)
y = 2 + 1.5*x + 2*np.random.randn(100)

"""
Aclaracion : Cuando entrenamos un modelo de regresion logistica, lo que hacemos es
encontrar la mejor linea que separe los datos. .

Y ahora te preguntaras, ¿Que son los datos sinteticos?

Los datos sinteticos son datos que se generan de forma artificial, es decir, no son datos reales.
Estos datos se generan con el fin de probar algoritmos de machine learning y deep learning tambien probabilidad y estadistica.
"""

# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, y_train = x[:80], y[:80]
x_test, y_test = x[80:], y[80:]

"""
Aca, dividimos los datos en dos conjuntos, uno de entrenamiento y otro de prueba.

El conjunto de entrenamiento es el conjunto de datos que usamos para entrenar el modelo.
El conjunto de prueba es el conjunto de datos que usamos para probar el modelo.
"""

# Vamos a visualizar los datos utilizando un diagrama de dispersión
plt.scatter(x_train, y_train, color='blue')
plt.xlabel('Tamaño de la casa')
plt.ylabel('Precio de la casa')
plt.show()

# Crear un objeto de regresión polinómica
grado = 2
poly_reg = PolynomialFeatures(degree=grado)
x_poly_train = poly_reg.fit_transform(x_train.reshape(-1,1))
x_poly_test = poly_reg.transform(x_test.reshape(-1,1))
regresion_pol = LinearRegression()
regresion_pol.fit(x_poly_train, y_train)

"""
Acabamos de crear un objeto de regresion polinomica. Este objeto tiene metodos y
atributos que nos permiten entrenar el modelo y predecir valores.

Ahora, vamos a entrenar el modelo con los datos de entrenamiento (x_train y y_train)

Aclaracion : Cuando entrenamos un modelo de regresion polinomica, lo que hacemos es
encontrar la mejor curva que se ajuste a los datos.
"""

# Visualizar el modelo de regresión polinómica
plt.scatter(x_train, y_train, color='blue')
plt.plot(x, regresion_pol.predict(poly_reg.transform(x.reshape(-1,1))), color='red')
plt.xlabel('Tamaño de la casa')
plt.ylabel('Precio de la casa')
plt.show()

"""
Ejemplo de predicción

Supongamos que queremos predecir el precio de una casa de 3 habitaciones.
"""

# Predecir el precio de una casa de 3 habitaciones por ejemplo
x_pred = np.array([3])
x_pred = x_pred.reshape(-1,1)
y_pred = regresion_pol.predict(poly_reg.transform(x_pred))

# Graficar la predicción
plt.scatter(x_train, y_train, color='blue')
plt.plot(x, regresion_pol.predict(poly_reg.transform(x.reshape(-1,1))), color='red')
plt.scatter(x_pred, y_pred, color='green')
plt.xlabel('Tamaño de la casa')
plt.ylabel('Precio de la casa')
plt.show()

# Imprimir el precio de la casa de 3 habitaciones
print('El precio de una casa de 3 habitaciones es: ', y_pred)

"""
En este ejemplo, hemos ajustado un modelo de regresión polinómica de segundo grado a nuestros datos 
y lo hemos utilizado para predecir el precio de una casa en función de su tamaño. 
Podemos ver que la línea roja del modelo de regresión polinómica se ajusta mejor a los datos que una línea recta.
"""
