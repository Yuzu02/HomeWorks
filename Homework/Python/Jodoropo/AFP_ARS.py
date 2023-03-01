# Creamos una clase Persona que tenga los atributos nombre, apellido, salario, descuento AFP y descuento ARS.
class Persona:
    # Creamos el constructor de la clase
    def __init__(self, nombre, apellido, salario): # self es el objeto que se crea de la clase Persona
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.afp = salario * 0.0287 # AFP es el 2.87% del salario
        self.ars = salario * 0.0304 # ARS es el 3.04% del salario
    
    # Creamos un metodo para mostrar la informacion de la persona
    def mostrar_informacion(self):
        print("Datos de la persona:")
        print() # Los print() son para darle un poco de espacio al codigo a la hora de mostrar la informacion en la terminal. 
        print(f"Nombre: {self.nombre}") # f es para formatear la cadena
        print(f"Apellido: {self.apellido}")
        print(f"Salario: {self.salario}")
        print(f"Descuento AFP: {self.afp:.2f}") # .2f es para mostrar solo 2 decimales
        print(f"Descuento ARS: {self.ars:.2f}")

# Estructura de datos para almacenar los datos de las personas
personas = []

# Creamos un ciclo para ingresar los datos de las personas
opcion = "s"

# Si la opcion es s, se ingresan los datos de una nueva persona
while opcion.lower() == "s": # El metodo lower() convierte la cadena a minusculas
    print()
    print("Algortimo para mostrar el nombre, Apellido, Salario, Descuento AFP y ARS")
    print() 
    nombre = input("Ingrese su nombre: ") 
    apellido = input("Ingrese su apellido: ")
    salario = float(input("Ingrese su salario: "))
    print()
    
    # Creamos un objeto de la clase Persona
    persona = Persona(nombre, apellido, salario)
    personas.append(persona) # Agregamos el objeto persona a la lista personas
    persona.mostrar_informacion() 
    
    print() 
    opcion = input("¿Desea ingresar los datos de otra persona? (s/n) ")
    print()
