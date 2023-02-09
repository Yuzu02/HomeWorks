# Definición de funciones

def is_prime(number): # Definimos la función que verifica si un número es primo
    if number <= 1: # Si el número es menor o igual a 1
        return False # Retorna False
    for i in range(2, number): # Para cada número entre 2 y el número
        if number % i == 0: # Si el número es divisible por el número actual
            return False # Retorna False
    return True # Retorna True

# Definimos la función que verifica si un número es fibonacci
def is_fibonacci(number): # number es el número a verificar
    a = 0 # Inicializamos a en 0
    b = 1 # Inicializamos b en 1
    while b < number: # Mientras b sea menor que el número
        c = a + b # c es igual a la suma de a y b
        a = b # a es igual a b
        b = c # b es igual a c
    return b == number # Retorna True si b es igual al número, False en caso contrario

# Definimos la función que verifica si un número es par o impar
def check_number(number): # number es el número a verificar
    if is_prime(number): # Si el número es primo
        print(f"{number} es primo") # Imprime que el número es primo
    else: # Si no
        print(f"{number} no es primo") # Imprime que el número no es primo
         
    if is_fibonacci(number): # Si el número es fibonacci
        print(f"{number} es fibonacci") # Imprime que el número es fibonacci
    else: # Si no
        print(f"{number} no es fibonacci") # Imprime que el número no es fibonacci
         
    if number % 2 == 0: # Si el número es divisible entre 2
        print(f"{number} es par") # Imprime que el número es par
    else: # Si no
        print(f"{number} es impar") # Imprime que el número es impar

number = int(input("Introduce un número: ")) # Solicitamos un número al usuario
check_number(number) # Llamamos a la función check_number con el número introducido por el usuario

# Ejemplo de uso

# Introduce un número: 5
# 5 no es primo
# 5 no es fibonacci
# 5 es impar

# Introduce un número: 8
# 8 no es primo
# 8 es fibonacci
# 8 es par
