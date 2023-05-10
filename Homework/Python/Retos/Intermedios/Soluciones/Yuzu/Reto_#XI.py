# Calcular el n-ésimo término de la serie de Fibonacci: Escribe una función que calcule el n-ésimo término de la serie de Fibonacci.

# Crear una función que calcule el n-ésimo término de la serie de Fibonacci.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
# Creamos la funcion main
def main():
    # Solicitamos el numero de terminos de la serie de fibonacci
    n = int(input("Ingresa el numero de terminos de la serie de fibonacci: "))
    # Creamos un ciclo for para imprimir los numeros de la serie de fibonacci
    for i in range(n):
        print("El termino", i+1, "de la serie de fibonacci es: ", fibonacci(i))
        
# Llamamos a la funcion main
main()        

# Ejemplo de ejecución:

"""
2
El término 1 de la serie de Fibonacci es 0.
El término 2 de la serie de Fibonacci es 1.

3
El término 1 de la serie de Fibonacci es 0.
El término 2 de la serie de Fibonacci es 1.
El término 3 de la serie de Fibonacci es 1.

5
El término 1 de la serie de Fibonacci es 0.
El término 2 de la serie de Fibonacci es 1.
El término 3 de la serie de Fibonacci es 1.
El término 4 de la serie de Fibonacci es 2.
El término 5 de la serie de Fibonacci es 3.
"""
