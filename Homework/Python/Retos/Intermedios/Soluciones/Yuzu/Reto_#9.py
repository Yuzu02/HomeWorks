# Comprobar si un número es primo: Escribe una función que determine si un número dado es primo o no.

# Crear una función que reciba un número como argumento.
def primo(num):
    # Crear un ciclo for que recorra el rango desde 2 hasta el número ingresado.
    for i in range(2, num):
        # Crear una condición que determine si el número ingresado es divisible por el número del ciclo for.
        if num % i == 0:
            # Si la condición se cumple, retornar un False.
            return False
    # Si la condición no se cumple, retornar un True.
    return True

# Crear una función main.
def main():
    # Pedir al usuario que ingrese un número.
    num = int(input("Ingrese un número: "))
    # Crear una condición que determine si el número ingresado es mayor a 1.
    if num > 1:
        # Si la condición se cumple, crear una condición que determine si la función primo retorna un True.
        if primo(num):
            # Si la condición se cumple, mostrar un mensaje que diga que el número ingresado es primo.
            print(f"El número {num} es primo.")
        # Si la condición no se cumple, mostrar un mensaje que diga que el número ingresado no es primo.
        else:
            print(f"El número {num} no es primo.")
    # Si la condición no se cumple, mostrar un mensaje que diga que el número ingresado no es primo.
    else:
        print(f"El número {num} no es primo.")

# Llamar a la función main.
main()

# Ejemplo de ejecución:

"""
Ingrese un número: 5
El número 5 es primo.

Ingrese un número: 34
El número 34 no es primo.

Ingrese un número: 12
El número 12 no es primo.
"""        
