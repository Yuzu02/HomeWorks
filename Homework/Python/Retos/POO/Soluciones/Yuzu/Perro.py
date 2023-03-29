'''
2- Crear una clase "Perro" que tenga atributos como nombre, raza y edad. Luego, crea un objeto de esta clase e imprime sus atributos.

• Define la clase "Perro" con los atributos de nombre, raza y edad.

• Crea un objeto de la clase "Perro" y establece los valores de sus atributos.

• Imprime los atributos del objeto de la clase "Perro".
'''

class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Solicitar al usuario que ingrese los datos del perro
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))

# Crear un objeto de la clase Perro con los datos ingresados
mi_perro = Perro(nombre, raza, edad)
print("Nombre:", mi_perro.nombre)
print("Raza:", mi_perro.raza)
print("Edad:", mi_perro.edad)

# Ejemplo de ejecución:

# Nombre: Angelica
# Raza: Pitbull
# Edad: 3
