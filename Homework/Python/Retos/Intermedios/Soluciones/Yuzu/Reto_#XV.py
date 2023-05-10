# Calcular la distancia euclidiana entre dos puntos en un plano cartesiano: Escribe una función que calcule la distancia euclidiana entre dos puntos en un plano cartesiano.

# Aclaración: La distancia euclidiana entre dos puntos en un plano cartesiano se calcula como la raíz cuadrada de la suma de los cuadrados de las diferencias de las coordenadas de los puntos.

# Función que calcule la distancia euclidiana entre dos puntos en un plano cartesiano.
def distancia_euclidiana(x1, y1, x2, y2):
    # Creamos la variable que almacena el resultado
    resultado = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    # Devolvemos el resultado
    return resultado

# Funcion principal (main)
def main():
    # Creamos la variable que almacena la coordenada x del primer punto
    x1 = float(input("Introduce la coordenada x del primer punto: "))
    # Creamos la variable que almacena la coordenada y del primer punto
    y1 = float(input("Introduce la coordenada y del primer punto: "))
    # Creamos la variable que almacena la coordenada x del segundo punto
    x2 = float(input("Introduce la coordenada x del segundo punto: "))
    # Creamos la variable que almacena la coordenada y del segundo punto
    y2 = float(input("Introduce la coordenada y del segundo punto: "))
    # Creamos la variable que almacena el resultado
    resultado = distancia_euclidiana(x1, y1, x2, y2)
    # Imprimimos el resultado
    print("La distancia euclidiana entre los puntos ({}, {}) y ({}, {}) es: {}".format(x1, y1, x2, y2, resultado))
    
# Ejecutamos la función principal
main()

# Casos test:
# (0, 0) y (0, 0) --> 0
# (2, 4) y (3, 2) --> 2.23606797749979
# (1, 1) y (2, 2) --> 1.4142135623730951
# (0, 0) y (1, 1) --> 1.4142135623730951     
# (0, 0) y (2, 2) --> 2.8284271247461903
