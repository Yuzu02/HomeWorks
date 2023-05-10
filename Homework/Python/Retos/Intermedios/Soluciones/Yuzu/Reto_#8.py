# Generar una lista de números primos: Escribe una función que genere una lista de números primos hasta un número dado.

# Definimos la función que genera una lista de números primos hasta un número dado
def listaNumerosPrimos(numero):
    lista = [] # Inicializamos la lista
    for i in range(2, numero + 1): # Recorremos los números desde el 2 hasta el número introducido
        esPrimo = True # Inicializamos la variable esPrimo a True
        for j in range(2, i): # Recorremos los números desde el 2 hasta el número anterior al número actual
            if i % j == 0: # Si el resto de la división del número actual entre el número actual es 0
                esPrimo = False # El número actual no es primo
                break # Salimos del bucle
        if esPrimo: # Si el número actual es primo
            lista.append(i) # Añadimos el número actual a la lista
    return lista # Devolvemos la lista

# Creamos la función main
def main():
    numero = int(input("Introduce un número: ")) # Pedimos el número
    print("Los números primos hasta", numero, "son", listaNumerosPrimos(numero)) # Mostramos la lista de números primos hasta el número introducido
    
# Llamamos a la función main
main()

# Ejemplo de ejecución:
"""
5
Los números primos hasta 5 son [2, 3, 5]

34
Los números primos hasta 34 son [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

12
Los números primos hasta 12 son [2, 3, 5, 7, 11]

"""    
