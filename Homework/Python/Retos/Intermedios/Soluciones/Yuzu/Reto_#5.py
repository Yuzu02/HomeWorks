# Ordenar una lista de números de menor a mayor: Escribe una función que reciba una lista de números y la ordene de menor a mayor.

# Función que recibe una lista de números y la ordena de menor a mayor

def ordenar(lista):
    lista.sort() # sort() ordena la lista de menor a mayor
    return lista # Devuelve la lista ordenada

# Pedimos la lista de números

lista = input("Introduce una lista de números separados por comas: ")

# Convertimos la lista de números en una lista de Python
lista = lista.split(",") # split() convierte una cadena en una lista de cadenas

# Convertimos los elementos de la lista de cadenas a números
lista = [int(i) for i in lista] # Convertimos cada elemento de la lista de cadenas a números

# Mostramos el resultado
print("La lista ordenada es", ordenar(lista))

# Ejemplo de ejecución para demostrar el funcionamiento de la solución

# Introduce una lista de números separados por comas: 56, 23, 1, 100, 5, 200, 10,86, 24, 78, 45, 12, 3, 4, 5, 6, 7, 8, 9, 10

# La lista ordenada es [1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23, 24, 45, 56, 78, 86, 100, 200]
