# Definimos la función imprimir_fibonacci que recibe dos parámetros: cantidad y primer_numero
def imprimir_fibonacci(cantidad, primer_numero): 
  # Inicializamos las variables a y b con los dos primeros números de la sucesión
  a, b = 0, primer_numero 
  # Iteramos tantas veces como indique la cantidad
  for i in range(cantidad): 
    # Imprimimos el valor de a
    print(a)
    # Calculamos el siguiente número de la sucesión sumando a y b y actualizamos a y b con estos valores
    a, b = b, a + b

# Solicitamos la cantidad de números de la sucesión de Fibonacci a imprimir
cantidad = int(input("Cantidad de números de la sucesión de Fibonacci a imprimir: "))
# Solicitamos el primer número de la sucesión
primer_numero = int(input("Primer número de la sucesión: "))
# Imprimimos la cantidad de números de la sucesión de Fibonacci a imprimir
print(cantidad)
# Imprimimos el primer número de la sucesión
print(primer_numero)
# Invocamos la función imprimir_fibonacci pasándole como parámetros la cantidad y el primer número de la sucesión
imprimir_fibonacci(cantidad, primer_numero)

# Ejemplo de ejecución:
# Cantidad de números de la sucesión de Fibonacci a imprimir: 10
# Primer número de la sucesión: 1
# 010
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
