# Función que ordena una lista de elementos aplicando el algoritmo de ordenación rápida (QuickSort)
def quick_sort(lista): # lista es la lista de elementos a ordenar
  
  # Si la lista tiene menos de 2 elementos, ya está ordenada
  if len(lista) < 2: # len(lista) devuelve el número de elementos de la lista
    return lista # Devolvemos la lista sin modificar

  # Elegimos el primer elemento como pivote
  pivote = lista[0] # lista[0] devuelve el primer elemento de la lista

  # Separamos la lista en dos sublistas: una con los elementos menores que el pivote y otra con los mayores
  menores = [x for x in lista[1:] if x <= pivote]
  mayores = [x for x in lista[1:] if x > pivote] 

  # Aplicamos el algoritmo de forma recursiva a cada sublista
  menores_ordenados = quick_sort(menores)
  mayores_ordenados = quick_sort(mayores)

  # Devolvemos la lista ordenada concatenando los elementos ordenados de cada sublista y el pivote
  return menores_ordenados + [pivote] + mayores_ordenados

# Función principal
def main():
    # Pedimos al usuario que introduzca una lista de números separados por comas
    lista = input("Introduce una lista de números separados por comas: ").split(", ")
    
    # Convertimos los elementos de la lista a números enteros
    lista = [int(x) for x in lista]
    
    # Aplicamos el algoritmo de ordenación rápida
    lista_ordenada = quick_sort(lista)
    
    # Mostramos la lista ordenada
    print(lista_ordenada)

# Llamamos a la función principal
main()


# Ejemplo de ejecución:

# Introduce una lista de números separados por comas: 5, 3, 6, 2, 10
# [2, 3, 5, 6, 10]


# Introduce una lista de números separados por comas: 5, 3, 6, 2, 10, 1, 4, 7, 9, 8
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
