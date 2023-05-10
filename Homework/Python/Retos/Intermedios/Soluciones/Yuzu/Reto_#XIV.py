# Calcular el número de permutaciones posibles de un conjunto de elementos: Escribe una función que calcule el número de permutaciones posibles de un conjunto de elementos.

# Aclaración: Una permutación es un arreglo de elementos en el que el orden sí importa. Por ejemplo, el conjunto {1, 2} tiene dos permutaciones: {1, 2} y {2, 1}.

# Creamos una función que calcule el número de permutaciones posibles de un conjunto de elementos.
def permutaciones(n):
    # Creamos la variable que almacena el resultado
    resultado = 1
    # Creamos el bucle que va desde 1 hasta n
    for i in range(1, n + 1):
        # Calculamos el resultado
        resultado *= i        
    # Devolvemos el resultado
    return resultado

# Creamos una función que guarde las permutaciones en una lista y las devuelva en forma de lista en lugar de devolver el número de permutaciones.
def permutaciones_lista(n):
    # Creamos la variable que almacena el resultado
    resultado = 1
    # Creamos la lista que almacena las permutaciones
    lista = []
    # Creamos el bucle que va desde 1 hasta n
    for i in range(1, n + 1):
        # Calculamos el resultado
        resultado *= i
        # Añadimos el resultado a la lista
        lista.append(resultado)
    # Devolvemos la lista
    return lista

# Funcion que toma los datos de entrada y los procesa
def main():
    # Creamos la variable que almacena el número de elementos
    n = int(input("Introduce el número de elementos: "))
    # Creamos la variable que almacena el resultado
    resultado = permutaciones(n)
    # Creamos la variable que almacena el resultado en forma de lista
    lista = permutaciones_lista(n)
    # Imprimimos el resultado
    print("El número de permutaciones posibles de un conjunto de elementos de", n, "elementos es:", resultado)
    
    # Preguntamos si quiere ver el resultado en forma de lista
    ver_lista = input("¿Quieres ver el resultado en forma de lista? (S/N): ")
    # Si la respuesta es afirmativa
    if ver_lista == "s" or ver_lista == "S":     
     print("El número de permutaciones posibles desde 1 hasta", n, "es:", lista)
    # Si la respuesta es negativa
    elif ver_lista == "n" or ver_lista == "N":
        print("No se mostrará el resultado en forma de lista")
    # Si la respuesta no es válida
    else:
        print("La respuesta no es válida.")
        
# Ejecutamos la función principal
main()

# Casos test:
# n = 1 --> 1
# n = 5 --> 120
# n = 10 --> 3628800\
# n = 7 -->  5040
# n = 3 --> 6   
