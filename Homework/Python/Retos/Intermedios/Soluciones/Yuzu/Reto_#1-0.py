# Calcular el factorial de un número: Escribe una función que calcule el factorial de un número dado.

# Crear una función que reciba un número como argumento.
def factorial(num):
    # Crear una variable que almacene el valor 1.
    factorial = 1
    # Crear un ciclo for que recorra el rango desde 1 hasta el número ingresado.
    for i in range(1, num + 1):
        # Multiplicar la variable factorial por el valor del ciclo for.
        factorial *= i
    # Retornar la variable factorial.
    return factorial

# Crear una función main.
def main():
    # Pedir al usuario que ingrese un número.
    num = int(input("Ingrese un número: "))
    # Crear una condición que determine si el número ingresado es mayor o igual a 0.
    if num >= 0:
        # Si la condición se cumple, mostrar un mensaje que diga que el factorial del número ingresado es igual al valor retornado por la función factorial.
        print(f"El factorial del número {num} es {factorial(num)}.")
    # Si la condición no se cumple, mostrar un mensaje que diga que el número ingresado no es válido.
    else:
        print("El número ingresado no es válido.")
        
# Llamar a la función main.
main()

# Ejemplo de ejecución:

"""
4
El factorial del número 4 es 24.

6
El factorial del número 6 es 720.

0 
El factorial del número 0 es 1.

"""        
