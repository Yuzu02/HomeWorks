# Calcular la raíz cuadrada de un número: Escribe una función que calcule la raíz cuadrada de un número utilizando el método de Newton-Raphson.

# Definimos la función que calcula la raíz cuadrada de un número utilizando el método de Newton-Raphson
def raizCuadrada(numero):
    estimacion = numero / 2 # Inicializamos la estimación con la mitad del número
    while True: # Bucle infinito
        nuevaEstimacion = (estimacion + numero / estimacion) / 2 # Calculamos la nueva estimación
        if abs(estimacion - nuevaEstimacion) < 0.0001: # Si la diferencia entre la estimación y la nueva estimación es menor que 0.0001
            return nuevaEstimacion # Devolvemos la nueva estimación
        estimacion = nuevaEstimacion # Actualizamos la estimación
        
# Creamos la función main
def main():
    numero = int(input("Introduce un número: ")) # Pedimos el número
    print("La raíz cuadrada de", numero, "es", raizCuadrada(numero)) # Mostramos la raíz cuadrada del número
    
# Llamamos a la función main
main()

# Ejemplo de ejecución:

"""
332
La raíz cuadrada de 332 es 18.2208671582886

144
La raíz cuadrada de 144 es 12.000000000000005

100
La raíz cuadrada de 100 es 10.000000000000002
"""    

# Metodo de Newton-Raphson
"""
El método de Newton-Raphson para calcular la raíz cuadrada de un número es el siguiente:
1. Inicializamos la estimación con la mitad del número.
2. Calculamos la nueva estimación.
3. Si la diferencia entre la estimación y la nueva estimación es menor que 0.0001, devolvemos la nueva estimación.
4. Actualizamos la estimación con la nueva estimación.
5. Volvemos al paso 2 y repetimos el proceso hasta que se cumpla la condición.
6. Devolvemos la nueva estimación que es la raíz cuadrada del número que hemos introducido.
7. Fin del metodo.
"""
