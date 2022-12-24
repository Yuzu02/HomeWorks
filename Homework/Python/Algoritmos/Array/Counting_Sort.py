# Función que ordena una lista de números enteros usando el algoritmo de ordenamiento por conteo
def counting_sort(lista):
  # Obtenemos el máximo elemento de la lista
  maximo = max(lista)

  # Creamos una lista de contadores con tantos elementos como el máximo elemento de la lista
  contadores = [0] * (maximo + 1)

  # Contamos el número de veces que aparece cada elemento en la lista
  for elemento in lista:
    contadores[elemento] += 1

  # Reconstruimos la lista ordenada a partir de los contadores
  lista_ordenada = []
  for elemento in range(len(contadores)):
    lista_ordenada.extend([elemento] * contadores[elemento])

  # Devolvemos la lista ordenada
  return lista_ordenada

# Programa principal

# Creamos una lista de números aleatorios
import random # Importamos el módulo random
lista = [random.randint(0, 100) for i in range(100)]

# La ordenamos
lista_ordenada = counting_sort(lista)

# Mostramos el resultado
print(lista_ordenada)

# Comprobamos que la lista está ordenada
print(lista_ordenada == sorted(lista))

# Ejecución

# $ python3 Counting_Sort.py
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# True

