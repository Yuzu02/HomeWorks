# Calcular la media de una lista de números: Escribe una función que reciba una lista de números y calcule su media aritmética.


# Definimos la función

def media(lista): # Recibe una lista de números
    suma = 0  # Acumulador
    for elemento in lista: # Recorremos la lista
        suma += elemento # Sumamos los elementos
    return suma / len(lista) # Devolvemos la media

# Creamos la lista

lista = [] 

# Pedimos los números y los añadimos a la lista
cantidad = int(input("¿Cuántos números quieres introducir? "))

for i in range(cantidad): # Recorremos la cantidad de números que queremos introducir
    numero = float(input("Introduce un número: ")) # Pedimos el número
    lista.append(numero) # Añadimos el número a la lista
    
# Calculamos la media y la mostramos
print("La media es", media(lista)) 

# Ejemplo de ejecución:

# ¿Cuántos números quieres introducir? 5

# Introduce un número: 1
# Introduce un número: 2
# Introduce un número: 3
# Introduce un número: 4
# Introduce un número: 5

# La media es 3.0 
