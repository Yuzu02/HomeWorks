'''
5- Crear una clase "Rectángulo" que tenga atributos como longitud y ancho. Luego, crea un objeto de esta clase e imprime sus atributos. Además, agrega métodos para calcular el área y el perímetro del rectángulo.

• Define la clase "Rectángulo" con los atributos de longitud y ancho.

• Crea un objeto de la clase "Rectángulo" y establece los valores de sus atributos.

• Agrega métodos para calcular el área del rectángulo utilizando la fórmula "longitud * ancho" y el perímetro utilizando la fórmula "2 * (longitud + ancho)".

• Imprime los atributos del objeto de la clase "Rectángulo", su área y su perímetro calculados.
'''

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)

# Solicitar al usuario que ingrese la longitud y el ancho del rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Crear un objeto de la clase "Rectangulo" con la longitud y el ancho ingresados
mi_rectangulo = Rectangulo(longitud, ancho)

# Imprimir los atributos del objeto, su área y su perímetro calculados
print("Longitud:", mi_rectangulo.longitud)
print("Ancho:", mi_rectangulo.ancho)
print("Área:", mi_rectangulo.calcular_area())
print("Perímetro:", mi_rectangulo.calcular_perimetro())

# Ejemplo de ejecución:
# Longitud: 5
# Ancho: 10
# Área: 50
# Perímetro: 30
