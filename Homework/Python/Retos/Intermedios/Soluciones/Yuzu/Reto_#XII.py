# Encontrar todos los divisores de un número: Escribe una función que encuentre todos los divisores de un número dado.

# Creamos la funcion divisores
def divisores(n):
    # Creamos un ciclo for para encontrar los divisores
    for i in range(1,n+1):
        # Creamos un condicional para imprimir los divisores
        if n%i == 0:
            print("El numero", i, "es divisor de", n)
            
# Creamos la funcion main
def main():
    # Solicitamos el numero
    n = int(input("Ingresa un numero: "))
    # Llamamos a la funcion divisores
    divisores(n)
        
# Llamamos a la funcion main
main()              

# Ejemplo de ejecución:

"""
Ingresa un numero: 10

El numero 1 es divisor de 10
El numero 2 es divisor de 10
El numero 5 es divisor de 10
El numero 10 es divisor de 10

Ingresa un numero: 7

El numero 1 es divisor de 7
El numero 7 es divisor de 7

Ingresa un numero: 6

El numero 1 es divisor de 6
El numero 2 es divisor de 6
El numero 3 es divisor de 6
El numero 6 es divisor de 6
"""         
