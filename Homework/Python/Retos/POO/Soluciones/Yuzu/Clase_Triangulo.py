'''
4- Crear una clase "Triángulo" que tenga atributos como base y altura. Luego, crea un objeto de esta clase e imprime sus atributos. Además, agrega un método para calcular el área del triángulo.

• Define la clase "Triángulo" con los atributos de base y altura.

• Crea un objeto de la clase "Triángulo" y establece los valores de sus atributos.

• Agrega un método para calcular el área del triángulo utilizando la fórmula "0.5 * base * altura".

• Imprime los atributos del objeto de la clase "Triángulo" y su área calculada.
'''


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

# Solicitar al usuario que ingrese la base y la altura del triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Crear un objeto de la clase "Triangulo" con la base y la altura ingresadas
mi_triangulo = Triangulo(base, altura)

# Imprimir los atributos del objeto y su área calculada
print("Base:", mi_triangulo.base)
print("Altura:", mi_triangulo.altura)
print("Área:", mi_triangulo.calcular_area())

# Ejemplo de ejecución:
# Base: 5
# Altura: 10
# Área: 25.0
