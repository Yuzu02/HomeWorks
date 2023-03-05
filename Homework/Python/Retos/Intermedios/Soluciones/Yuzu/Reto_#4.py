# Encontrar el número más grande en una lista: Escribe una función que reciba una lista de números y devuelva el número más grande.

# Función que recibe una lista de números y devuelve el número más grande

def maximo(lista):
    max = lista[0] # Inicializamos el máximo con el primer elemento de la lista
    for i in lista: # Recorremos la lista
        if i > max: # Comprobamos si el elemento es mayor que el máximo
            max = i # Si es mayor, lo guardamos como máximo
    return max # Devolvemos el máximo

# Pedimos la lista de números

lista = input("Introduce una lista de números separados por comas: ")
    
# Convertimos la lista de números en una lista de Python
lista = lista.split(",")

# Convertimos los elementos de la lista de cadenas a números
for i in range(len(lista)):
    lista[i] = int(lista[i])
    
# Mostramos el resultado
print("El número más grande es", maximo(lista))

# Ejemplo de ejecución para demostrar el funcionamiento de la solución

# Introduce una lista de números separados por comas: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# El número más grande es 10

# Introduce una lista de números separados por comas: 40,22,10,100,1,5,200
# El número más grande es 200
