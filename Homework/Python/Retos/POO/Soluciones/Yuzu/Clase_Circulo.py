'''
3- Crear una clase "Círculo" que tenga atributos como radio y diámetro. Luego, crea un objeto de esta clase e imprime sus atributos. Además, agrega un método para calcular el área del círculo.

• Define la clase "Círculo" con los atributos de radio y diámetro.

• Crea un objeto de la clase "Círculo" y establece los valores de sus atributos.

• Agrega un método para calcular el área del círculo utilizando la fórmula "pi * radio^2".

• Imprime los atributos del objeto de la clase "Círculo" y su área calculada.
'''

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = radio * 2

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Crear un objeto de la clase "Círculo" con el radio ingresado
mi_circulo = Circulo(radio)

# Imprimir los atributos del objeto y su área calculada
print("Radio:", mi_circulo.radio)
print("Diámetro:", mi_circulo.diametro)
print("Área:", mi_circulo.calcular_area())

# Ejemplo de ejecución:
# Radio: 5
# Diámetro: 10
# Área: 78.53999999999999
