# Definimos la funcion valor_absoluto
def valor_absoluto(): 
    numero = int(input("Introduce un numero entero: ")) # Leemos el numero
    
    # Si el numero es negativo lo convertimos en positivo
    if numero < 0: # Si el numero es menor que 0
        numero = numero * -1 # Multiplicamos por -1 para convertirlo en positivo
    
    # Imprimimos el numero    
    print("El valor absoluto es: ", numero)

# Llamamos a la funcion
valor_absoluto()

# Ejemplos de uso

# Introduce un numero entero: 5
# El valor absoluto es:  5


# Introduce un numero entero: -5
# El valor absoluto es:  5
