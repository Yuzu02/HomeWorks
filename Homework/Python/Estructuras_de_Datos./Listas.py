# Listas en Python
# Autor: Yuzu02 (GitHub)

'''Las listas son una estructura de datos que permite almacenar varios valores en una sola variable. 
En Python, las listas se definen entre corchetes y sus elementos se separan por comas.
Además, las listas son mutables, es decir, se pueden modificar los elementos de la lista una vez creada.
Y, por último, las listas son ordenadas, es decir, los elementos de la lista se almacenan en un orden determinado.
'''

# ¿En qué casos se utilizan las listas?

''' 
Las listas se utilizan cuando queremos modificar los elementos de la lista.
Las listas se utilizan cuando queremos almacenar varios valores en una sola variable.
Como por ejemplo, si queremos almacenar los nombres de los alumnos de un curso.
También se utilizan cuando queremos almacenar varios valores de un mismo tipo.
Ya sea números, cadenas de texto, etc.
'''

# ¿En que se diferencian las listas de otras estructuras de datos?

'''
Las listas se diferencian de las tuplas, ya que las listas son mutables y las tuplas no.
Por otro lado, las listas se diferencian de los diccionarios, ya que las listas son ordenadas y los diccionarios no.
También se diferencian de los conjuntos, ya que las listas son ordenadas y los conjuntos no.
En conclusión, las listas se diferencian de las tuplas, diccionarios y conjuntos, ya que las listas son mutables, ordenadas y se pueden indexar.
'''

# Qué métodos y funciones se pueden utilizar con las listas

'''
Existen varios métodos y funciones que se pueden utilizar con las listas.
Por ejemplo, append, insert, index, count, sort, reverse, etc.
También existen varias funciones que se pueden utilizar con las listas.
Como por ejemplo, len, max, min, etc.
Por último, existen varios operadores que se pueden utilizar con las listas.
Como por ejemplo, +, *, in, not in, etc.
'''

# Ventajas y desventajas de las listas

# Desventajas
 
'''
En cuanto a las desventajas, las listas ocupan más espacio en memoria que las tuplas.
También son más lentas que las tuplas.
Además, no se pueden utilizar como claves de un diccionario.
'''

# Ventajas

'''
A pesar de las desventajas, las listas tienen varias ventajas.
Como por ejemplo, que son mutables, es decir, se pueden modificar los elementos de la lista una vez creada (añadir, eliminar, modificar).
También son ordenadas, es decir, los elementos de la lista se almacenan en un orden determinado.
Y, por último, se pueden indexar, es decir, se puede acceder a un elemento de la lista mediante su posición.
'''

# ¡Vamos a ver un como se crean y utilizan las listas!

# Creación de una lista
mi_lista = [1, 2, 3, 4, 5] # Asigamos una lista de 5 elementos a la variable mi_lista

# Acceso a un elemento de la lista
print(mi_lista[2]) # Salida: 3

'''
El primer elemento de la lista se encuentra en la posición 0
El segundo elemento de la lista se encuentra en la posición 1
Y así sucesivamente
'''

# Modificación de un elemento de la lista
mi_lista[2] = 6 # = se utiliza para asignar un valor a una variable

# Imprimimos la lista modificada
print(mi_lista) # Salida: [1, 2, 6, 4, 5]

# Eliminación de un elemento de la lista
del mi_lista[2] # Eliminamos el tercer elemento de la lista

'''
del es una palabra reservada de Python que permite eliminar un elemento de una lista.
De esta forma, eliminamos el tercer elemento de la lista.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [1, 2, 4, 5]

# Añadir un elemento a la lista
mi_lista.append(6) # Añadimos el elemento 6 al final de la lista

'''
append es un método de las listas que permite añadir un elemento al final de la lista.
tan solo debemos pasar como argumento el elemento que queremos añadir.
y, de esta forma, añadimos el elemento 6 al final de la lista.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [1, 2, 4, 5, 6]

# Añadir un elemento en una posición determinada

mi_lista.insert(2, 3) # Añadimos el elemento 3 en la posición 2

'''
insert es un método de las listas que permite añadir un elemento en una posición determinada.
tan solo debemos pasar como argumento la posición en la que queremos añadir el elemento y el elemento que queremos añadir.
y, de esta forma, añadimos el elemento 3 en la posición 2.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [1, 2, 3, 4, 5, 6]

# Mostrar el índice de un elemento de la lista

print(mi_lista.index(3)) # Mostramos el índice del elemento 3

'''
index es un método de las listas que permite mostrar el índice de un elemento de la lista.
tan solo debemos pasar como argumento el elemento del que queremos saber el índice.
y, de esta forma, mostramos el índice del elemento 3.
'''

# Mostrar el número de elementos de la lista
print(len(mi_lista)) # Mostramos el número de elementos de la lista

'''
len es una función de Python que permite mostrar el número de elementos de una lista.
tan solo debemos pasar como argumento la lista del que queremos saber el número de elementos.
y, de esta forma, mostramos el número de elementos de la lista.
'''

# Mostrar el número de veces que aparece un elemento en la lista
print(mi_lista.count(3)) # Mostramos el número de veces que aparece el elemento 3 en la lista

'''
count es un método de las listas que permite mostrar el número de veces que aparece un elemento en la lista.
tan solo debemos pasar como argumento el elemento del que queremos saber el número de veces que aparece.
y, de esta forma, mostramos el número de veces que aparece el elemento 3 en la lista.
'''

#Ordenar una lista
mi_lista.sort() # Ordenamos la lista

'''
sort es un método de las listas que permite ordenar una lista.
tan solo debemos pasar como argumento la lista que queremos ordenar.
y, de esta forma, ordenamos la lista.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [1, 2, 3, 4, 5, 6]

# Invertir una lista
mi_lista.reverse() # Invertimos la lista

'''
reverse es un método de las listas que permite invertir una lista.
tan solo debemos pasar como argumento la lista que queremos invertir.
y, de esta forma, invertimos la lista.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [6, 5, 4, 3, 2, 1]

# Extender una lista
mi_lista.extend([7, 8, 9]) # Extendemos la lista

'''
extend es un método de las listas que permite extender una lista.
tan solo debemos pasar como argumento la lista que queremos extender.
y, de esta forma, extendemos la lista.
'''

# Imprimimos la lista modificada
print(mi_lista) # Salida: [6, 5, 4, 3, 2, 1, 7, 8, 9]

# Quitar el último elemento de la lista]

# Opción 1
mi_lista.pop() # Quitamos el último elemento de la lista

'''
pop es un método de las listas que permite quitar el último elemento de la lista.
tan solo debemos pasar como argumento la lista de la que queremos quitar el último elemento.
y, de esta forma, quitamos el último elemento de la lista.
'''

# Opcion 2
mi_lista.remove(9) # Quitamos el elemento 9 de la lista

'''
remove es un método de las listas que permite quitar un elemento de la lista.
tan solo debemos pasar como argumento el elemento que queremos quitar de la lista.
y, de esta forma, quitamos el elemento 9 de la lista.
'''

# Quitar todos los elementos de la lista
mi_lista.clear() # Quitamos todos los elementos de la lista

'''
clear es un método de las listas que permite quitar todos los elementos de la lista.
tan solo debemos pasar como argumento la lista de la que queremos quitar todos los elementos.
y, de esta forma, quitamos todos los elementos de la lista.
'''

# Quitar la lista
mi_lista = None # Quitamos la lista

'''
None es una palabra reservada de Python que permite quitar una lista.
tan solo debemos pasar como argumento la lista que queremos quitar.
y, de esta forma, quitamos la lista.
'''

# Operaciones con listas

'''
Estas son las operaciones que podemos realizar con las listas.
En este caso por motivo de simplicidad, solo vamos a ver las operaciones con un solo operador (El operador +)
Ya sea el operador + , - , * , / , // , % , ** , < , > , <= , >= , == , != , and , or , not
Permitiendo así la suma, resta, multiplicación, división, división entera, módulo, potencia, menor que, mayor que, menor o igual que, mayor o igual que, igual que, distinto que, and, or, not
Usaremos la suma para representar todas las operaciones basicas , ya que es la que más se usa en las listas.
Solo debemos tener en cuenta se aplica el mismo procedimiento para todas las operaciones basicas y las operaciones lógicas.
'''

# Suma de listas

lista1 = [1, 2, 3] # Creamos la lista 1
lista2 = [4, 5, 6] # Creamos la lista 2

# Sumamos las listas
lista3 = lista1 + lista2 # Sumamos las listas

# Imprimimos la lista 3
print(lista3) # Salida: [1, 2, 3, 4, 5, 6]


# Suma de una lista por un número

lista = [1, 2, 3] # Creamos la lista
lista = lista + 3 # Sumamos la lista por 3

# Imprimimos la lista
print(lista) # Salida: [1, 2, 3, 3, 3, 3]

# Suma de una lista por una cadena

lista = [1, 2, 3] # Creamos la lista
lista = lista + "Hola" # Sumamos la lista por "Hola"

# Imprimimos la lista
print(lista) # Salida: [1, 2, 3, 'H', 'o', 'l', 'a']

# Suma de una lista por una tupla
lista1 = [1, 2, 3] # Creamos la lista 1

lista1 = lista1 + (4, 5, 6) # Sumamos la lista por una tupla

# Imprimimos la lista
print(lista1) # Salida: [1, 2, 3, 4, 5, 6]

# Suma de una lista por un diccionario
lista1 = [1, 2, 3] # Creamos la lista 1
lista1 = lista1 + {"Hola": "Mundo"} # Sumamos la lista por un diccionario

# Imprimimos la lista
print(lista1) # Salida: [1, 2, 3, 'Hola']

# Otras operaciones con listas

'''
Otras operaciones que podemos realizar con las listas.
'''

# Cortes de listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Creamos la lista
lista = lista[1:5] # Cortamos la lista


'''
El valor a la izquierda del : indica el índice desde el que queremos cortar la lista.
El : indica que queremos cortar la lista.
El valor a la derecha del : indica el índice hasta el que queremos cortar la lista.
'''

# Imprimimos la lista
print(lista) # Salida: [2, 3, 4, 5]

# Copiar una lista
lista1 = [1, 2, 3] # Creamos la lista 1
lista2 = lista1.copy() # Copiamos la lista 1

# Imprimimos la lista 2

print(lista2) # Salida: [1, 2, 3]

# Comprobar si un elemento está en una lista

# Opción 1

lista = [1, 2, 3] # Creamos la lista
print(1 in lista) # Comprobamos si el elemento 1 está en la lista

'''
in es un operador de Python que permite comprobar si un elemento está en una lista.
tan solo debemos pasar como argumento el elemento que queremos comprobar y la lista en la que queremos comprobar.
y, de esta forma, comprobamos si el elemento 1 está en la lista.
'''

# Opción 2

lista = [1, 2, 3] # Creamos la lista
print(1 not in lista) # Comprobamos si el elemento 1 no está en la lista

'''
not in es un operador de Python que permite comprobar si un elemento no está en una lista.
tan solo debemos pasar como argumento el elemento que queremos comprobar y la lista en la que queremos comprobar.
y, de esta forma, comprobamos si el elemento 1 no está en la lista.
'''

# Iterar una lista

# Opción 1

lista = [1, 2, 3] # Creamos la lista
for elemento in lista: # Iteramos la lista
    print(elemento) # Imprimimos el elemento
 
'''
i es una variable que usamos para iterar la lista. 
'''
  
# Opción 2

lista = [1, 2, 3] # Creamos la lista
for i in range(len(lista)): # Iteramos la lista
    print(lista[i]) # Imprimimos el elemento
    
''''
range es una función de Python que permite crear una lista de números.
tan solo debemos pasar como argumento el número de elementos que queremos que tenga la lista.
y, de esta forma, creamos una lista de números.
'''
    
'''
Es importante que sepas que [i] es una variable que usamos para iterar la lista.
Por lo tanto, no debes usarla para otra cosa.
'''

# Opción 3 (Más avanzada)

lista = [1, 2, 3] # Creamos la lista
for i, elemento in enumerate(lista): # Iteramos la lista
    print(i, elemento) # Imprimimos el elemento
    
    '''
    enumerate es una función de Python que permite crear una lista de tuplas.
    tan solo debemos pasar como argumento la lista que queremos iterar.
    y, de esta forma, creamos una lista de tuplas.
    '''
    
# Opción 4 (Más avanzada)

lista = [1, 2, 3] # Creamos la lista
for i, elemento in zip(range(len(lista)), lista): # Iteramos la lista
    print(i, elemento) # Imprimimos el elemento
    
    '''
    zip es una función de Python que permite crear una lista de tuplas.
    tan solo debemos pasar como argumento las listas que queremos iterar.
    y, de esta forma, creamos una lista de tuplas.
    '''
    
# Comprensión de lista

# Opción 1

lista = [1, 2, 3, 7, 9, 12] # Creamos la lista

# Creamos la lista con comprensión de lista
lista = [elemento for elemento in lista if elemento % 2 == 0]

'''
elemento es una variable que usamos para iterar la lista.
for elemento in lista es la parte de la comprensión de lista que nos permite iterar la lista.
if elemento % 2 == 0 es la parte de la comprensión de lista que nos permite filtrar los elementos de la lista.
por lo tanto, tan solo nos quedan los elementos pares.
'''

# Imprimimos la lista
print(lista) # Salida: [2, 12]

# Opción 2
lista = [1, 2, 3, 7, 9, 12] # Creamos la lista

# Creamos la lista con comprensión de lista y función lambda
lista = list(filter(lambda elemento: elemento % 2 == 0, lista))

'''
list es una función de Python que permite convertir un iterable en una lista.
filter es una función de Python que permite filtrar los elementos de un iterable.
lambda es una función de Python que permite crear una función anónima.
por lo tanto, tan solo nos quedan los elementos pares.
'''

# Imprimimos la lista
print(lista) # Salida: [2, 12]

# Opción 3

# Creamos la lista con comprensión de lista y función lambda y map
lista = list(map(lambda elemento: elemento * 2, [1, 2, 3, 7, 9, 12]))

'''
map es una función de Python que permite iterar un iterable.
Poder iterar un iterable es muy útil para poder modificar los elementos de un iterable.
Como puedes ver, hemos multiplicado por 2 cada elemento de la lista.
'''

# Imprimimos la lista
print(lista) # Salida: [2, 4, 6, 14, 18, 24]

# Hash de una lista

lista = [1, 2, 3] # Creamos la lista
hash(lista) # Obtenemos el hash de la lista

'''
hash es una función de Python que permite obtener el hash de un objeto.
El hash de un objeto es un número que identifica de forma única a un objeto.
En este caso, el hash de la lista es el mismo que el hash de la lista ordenada.
Es decir, el hash de la lista [1, 2, 3] es el mismo que el hash de la lista [1, 3, 2].
Pero es importante que sepas que el hash de la lista [1, 2, 3] no es el mismo que el hash de la lista [2, 1, 3].
'''

# Esto es importante porque, por ejemplo, si queremos comprobar si dos listas son iguales, podemos hacerlo de la siguiente forma:

lista1 = [1, 2, 3]
lista2 = [1, 3, 2]

hash(lista1) == hash(lista2) # Comprobamos si las listas son iguales

# Otra forma de comprobar si dos listas son iguales es la siguiente:

hash(tuple(lista1)) == hash(tuple(lista2)) # Comprobamos si las listas son iguales

''' Hasta aquí el tutorial de listas en Python. Espero que te haya gustado y que te haya servido de ayuda
Esto es todo por hoy. Nos vemos en el siguiente tutorial. ¡Hasta pronto!  Made by @Yuzu02    
'''

# Ejercicios

# Crea una lista con los números del 1 al 10.
# Crea una lista con los números del 1 al 10 y multiplica por 2 cada elemento de la lista.
# Crea una lista con los números del 1 al 10 y filtra los elementos pares de la lista.
# Crea una lista con los números del 1 al 10 y filtra los elementos impares de la lista.
# Crea una lista con los números del 1 al 10 y filtra los elementos múltiplos de 3 de la lista.
# Utiliza la función enumerate para crear una lista de tuplas con los números del 1 al 10.
# Utiliza la función zip para crear una lista de tuplas con los números del 1 al 10.
# Itera la lista [1, 2, 3, 7, 9, 12] y filtra los elementos pares de la lista.
# Utiliza la función map para crear una lista con los números del 1 al 10 multiplicados por 2.
# Utiliza la función filter para crear una lista con los números del 1 al 10 que sean múltiplos de 3.
# Crea un codigo en el cual utilices todas las funciones de listas que hemos visto en este tutorial.
