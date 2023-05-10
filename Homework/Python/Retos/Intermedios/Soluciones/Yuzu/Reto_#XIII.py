# Calcular el número de combinaciones posibles de un conjunto de elementos: Escribe una función que calcule el número de combinaciones posibles de un conjunto de elementos.

# Creamos la función que calcula el número de combinaciones posibles de un conjunto de elementos
def combinaciones(n, k): 
    # Creamos la variable que almacena el resultado
    resultado = 1
    # Creamos el bucle que va desde 1 hasta k
    for i in range(1, k + 1):
        # Calculamos el resultado
        resultado *= (n + 1 - i) / i
    # Devolvemos el resultado
    return resultado

# Creamos la función principal (main)
def main():
    # Pedimos al usuario que introduzca el número de elementos
    n = int(input("Introduce el número de elementos: ")) # Osea, el número de elementos que hay en el conjunto
    # Pedimos al usuario que introduzca el número de elementos a combinar
    k = int(input("Introduce el número de elementos a combinar: ")) # Osea, el número de elementos que se van a combinar
    # Mostramos al usuario el resultado
    print("El número de combinaciones posibles es:", combinaciones(n, k))

# Ejecutamos la función principal
main()

# Casos test:
# n = 5, k = 3 -> 10
# n = 10, k = 5 -> 252
# n = 20, k = 10 -> 184756
# n = 30, k = 15 -> 155117520
# n = 40, k = 20 -> 137846528820    
