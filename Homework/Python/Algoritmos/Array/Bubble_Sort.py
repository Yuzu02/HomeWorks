# Función que ordena una lista de números enteros usando el algoritmo de ordenación por burbuja
def bubble_sort(lista): # lista es una lista de números enteros
  # Iteramos tantas veces como elementos haya en la lista
  for i in range(len(lista)): # i es el índice del elemento actual
    # Iteramos desde el segundo elemento hasta el último
    for j in range(1, len(lista)): # j es el índice del elemento actual
      # Si el elemento actual es mayor que el anterior, los intercambiamos
      if lista[j] < lista[j-1]: # j-1 es el índice del elemento anterior
        lista[j], lista[j-1] = lista[j-1], lista[j]
  # Devolvemos la lista ordenada
  return lista

# Función principal
def main(): # No recibe parámetros
    # Pedimos al usuario que introduzca una lista de números enteros
    lista = input("Introduce una lista de números enteros separados por comas: ")
    # Separamos los elementos de la lista
    lista = lista.split(",")
    # Convertimos los elementos de la lista a números enteros
    for i in range(len(lista)): # i es el índice del elemento actual
        lista[i] = int(lista[i]) # Convertimos el elemento actual a número entero    
    # Ordenamos la lista 
    lista = bubble_sort(lista) # lista es una lista de números enteros
    # Mostramos la lista ordenada
    print("Lista ordenada:", end=" ") # Mos
    for i in range(len(lista)): # i es el índice del elemento actual
        if i == len(lista)-1: # Si es el último elemento
         print(lista[i]) # Lo mostramos sin la coma
        else: # Si no es el último elemento
         print(lista[i], end=", ") # end=" " hace que no se salte una línea al final

# Llamamos a la función principal
main()

# Ejemplo de uso

# Lista desordenada: [5, 2, 4, 6, 1, 3]
# Lista ordenada: [1, 2, 3, 4, 5, 6]

# lista desordenada: [75, 2, 4, 6, 1, 3]
# lista ordenada: [1, 2, 3, 4, 6, 75]
