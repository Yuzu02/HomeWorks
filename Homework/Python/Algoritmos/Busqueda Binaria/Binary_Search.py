# Algoritmo basico de busqueda binaria (Binary Search)
# Make by: @yuzu02 (GitHub)

"""
Los algoritmos de busqueda binaria son utilizados para buscar un elemento en una lista ordenada. 
De forma iterativa, se compara el elemento a buscar con el elemento en la mitad de la lista
Y se descarta la mitad de la lista en la que no se encuentra el elemento buscado
Luego se repite el proceso con la mitad restante de la lista hasta encontrar el elemento buscado.

Esto da como resultado la posicion del target a traves del indice de la lista
"""

# Funcion de busqueda binaria
def binary_search(arr, target): # arr = lista, target = elemento a buscar
    low = 0 # Inicializamos el limite inferior
    high = len(arr) - 1 # Inicializamos el limite superior
    
    # Mientras el limite inferior sea menor o igual al limite superior
    while low <= high: 
        mid = (low + high) // 2 # Calculamos la mitad de la lista
        if arr[mid] == target: # Si el elemento en la mitad de la lista es igual al elemento buscado
            return mid # Retornamos la posicion del elemento
        elif arr[mid] < target: # Si el elemento en la mitad de la lista es menor al elemento buscado
            low = mid + 1 # El limite inferior se convierte en la mitad de la lista + 1
        else: # Si el elemento en la mitad de la lista es mayor al elemento buscado
            high = mid - 1 # El limite superior se convierte en la mitad de la lista - 1
    # Si el elemento no se encuentra en la lista
    return -1


# Funcion para probar el algoritmo con una lista y target de busqueda predefinidos
def test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    if result == -1:
        print("El elemento no se encuentra en la lista")
    else:
        print("El elemento se encuentra en la posicion", result)


# Funcion para probar el algoritmo con tu propia lista y target de busuqeda
def run():
    arr = list(map(int, input("Ingresa los elementos de la lista separados por un espacio: ").split()))
    target = int(input("Ingresa el elemento a buscar: "))
    result = binary_search(arr, target)
    if result == -1:
        print("El elemento no se encuentra en la lista")
    else:
        print("El elemento se encuentra en la posicion", result)
        
# Ejecucion de las funcion run
if __name__ == '__main__':
    run()
    # test()
    
# Si quieres probar el algoritmo con una lista y target de busqueda predefinidos, ejecuta la funcion test
