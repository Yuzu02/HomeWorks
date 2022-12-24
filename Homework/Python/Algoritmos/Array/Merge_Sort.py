# Funcion que ordena una lista de numeros enteros
def merge_sort(lista): 
    if len(lista) > 1: # Si la lista tiene mas de un elemento
        mitad = len(lista) // 2 # Se divide la lista en dos
        izquierda = lista[:mitad] # La lista de la izquierda = lista[:mitad]
        derecha = lista[mitad:] # La lista de la derecha = lista[mitad:]

        merge_sort(izquierda) # Se ordena la lista de la izquierda
        merge_sort(derecha) # Se ordena la lista de la derecha

        i = 0 # Indice de la lista de la izquierda
        j = 0 # Indice de la lista de la derecha
        k = 0 # Indice de la lista original

        while i < len(izquierda) and j < len(derecha): # Mientras no se llegue al final de las listas
            if izquierda[i] < derecha[j]: # Si el elemento de la lista de la izquierda es menor que el de la derecha
                lista[k] = izquierda[i] # Se agrega el elemento de la lista de la izquierda a la lista original
                i += 1 # Se incrementa el indice de la lista de la izquierda
            else: # Si el elemento de la lista de la derecha es menor que el de la izquierda
                lista[k] = derecha[j] # Se agrega el elemento de la lista de la derecha a la lista original
                j += 1 # Se incrementa el indice de la lista de la derecha
            k += 1 # Se incrementa el indice de la lista original
        
        # Se agregan los elementos que no se han agregado a la lista original
        while i < len(izquierda): # Mientras no se llegue al final de la lista de la izquierda
            lista[k] = izquierda[i] # Se agrega el elemento de la lista de la izquierda a la lista original
            i += 1 # Se incrementa el indice de la lista de la izquierda
            k += 1 # Se incrementa el indice de la lista original

        while j < len(derecha): # Mientras no se llegue al final de la lista de la derecha
            lista[k] = derecha[j] # Se agrega el elemento de la lista de la derecha a la lista original
            j += 1 # Se incrementa el indice de la lista de la derecha
            k += 1 # Se incrementa el indice de la lista original

    return lista # Se regresa la lista ordenada

# Funcion principal

# Se crea una lista de numeros enteros
lista = (input("Escribe los elementos de la lista separados por comas: ").split(","))

# Se convierten los elementos de la lista a numeros enteros
for i in range(len(lista)): # Para cada elemento de la lista
    lista[i] = int(lista[i]) # Se convierte el elemento a numero entero
    
main = merge_sort(lista) # Se ordena la lista

print(lista) # Se imprime la lista ordenada

# Ejemplo de ejecución:

# Escribe los elementos de la lista separados por comas: 8,4,23,42,16,15
# [4, 8, 15, 16, 23, 42]

# Escribe los elementos de la lista separados por comas: 12,11,13,5,6
# [5, 6, 11, 12, 13]
