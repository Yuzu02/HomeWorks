# Clase Persona

'''
1- Crear una clase "Persona" que tenga atributos como nombre, edad y género. Luego, crea un objeto de esta clase e imprime sus atributos.

• Define la clase "Persona" con los atributos de nombre, edad y género.

• Crea un objeto de la clase "Persona" y establece los valores de sus atributos.

• Imprime los atributos del objeto de la clase "Persona".
'''

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

# Solicitar al usuario que ingrese los datos de la persona
nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: "))
genero = input("Ingresa el género de la persona: ")

# Crear un objeto de la clase Persona con los datos ingresados
p = Persona(nombre, edad, genero)

# Imprimir los atributos del objeto de la clase Persona
print("Nombre:", p.nombre)
print("Edad:", p.edad)
print("Género:", p.genero)

# Ejemplo de ejecución:

# Nombre: Yuzu
# Edad: 17
# Género: Masculino.
