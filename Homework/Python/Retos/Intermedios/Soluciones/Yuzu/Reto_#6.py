# Encontrar el número más pequeño en una lista: Escribe una función que reciba una lista de números y devuelva el número más pequeño.

# Definimos la función que recibe los números y los añade a la lista
lista = [] # Creamos la lista
def pedirNumeros(lista): # Recibe una lista
    cantidad = int(input("¿Cuántos números quieres introducir? ")) # Pedimos la cantidad de números que queremos introducir
    for i in range(cantidad): # Recorremos la cantidad de números que queremos introducir
        numero = float(input("Introduce un número: ")) # Pedimos el número
        lista.append(numero) # Añadimos el número a la lista
    return lista # Devolvemos la lista

# Definimos la función que recibe una lista y devuelve el número más pequeño
def numeroMasPequeno(lista): # Recibe una lista
    numeroMasPequeno = lista[0] # Inicializamos la variable con el primer elemento de la lista
    for elemento in lista: # Recorremos la lista
        if elemento < numeroMasPequeno: # Si el elemento es menor que el número más pequeño
            numeroMasPequeno = elemento # Actualizamos el número más pequeño
    return numeroMasPequeno # Devolvemos el número más pequeño

# Creamos la funcion main
def main():
    pedirNumeros(lista) # Llamamos a la función que pide los números y los añade a la lista
    print("El número más pequeño es", numeroMasPequeno(lista)) # Llamamos a la función que devuelve el número más pequeño y lo mostramos
    lista.sort() # Ordenamos la lista de menor a mayor
    print("La lista ordenada es", lista) # Mostramos la lista ordenada
        
main() # Llamamos a la función main

# Ejemplo de ejecución:

"""
Cuántos números quieres introducir? 5
Introduce un número: 424
Introduce un número: 442
Introduce un número: 41
Introduce un número: 4
Introduce un número: 31

El número más pequeño es 4.0
"""    
