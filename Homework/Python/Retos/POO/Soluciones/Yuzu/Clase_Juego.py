'''
9- Crear una clase "Juego" que tenga atributos como nombre, género y clasificación de edad. Luego, crea varios objetos de esta clase y muestra sus atributos. Además, agrega un método para verificar si un jugador cumple con la clasificación de edad del juego.

• Define la clase "Juego" con los atributos de nombre, género y clasificación de edad.

• Crea varios objetos de la clase "Juego" y establece los valores de sus atributos.

• Agrega un método para verificar si un jugador cumple con la clasificación de edad del juego comparando la edad del jugador con la clasificación de edad del juego.

• Imprime los atributos de cada objeto de la clase "Juego" y realiza algunas verificaciones de clasificación de edad para demostrar el funcionamiento del método.
'''


class Juego:
    def __init__(self, nombre, genero, clasificacion_edad):
        self.nombre = nombre
        self.genero = genero
        self.clasificacion_edad = clasificacion_edad

    def verificar_edad(self, edad_jugador):
        return edad_jugador >= self.clasificacion_edad  
        
try:
    # Solicitar la edad del jugador
    edad_jugador = int(input("Ingrese la edad del jugador: "))
    if edad_jugador < 0:
        raise ValueError("La edad del jugador no puede ser negativa.")
except ValueError as e:
    print("Error:", e)

# Crear varios objetos de la clase "Juego"
juego1 = Juego("The Legend of Zelda: Breath of the Wild", "Aventura", 12)
juego2 = Juego("Call of Duty: Modern Warfare", "Shooter", 18)
juego3 = Juego("Animal Crossing: New Horizons", "Simulación", 3)

# Imprimir los atributos de cada objeto
print("Juego 1:")
print("Nombre:", juego1.nombre)
print("Género:", juego1.genero)
print("Clasificación de edad:", juego1.clasificacion_edad)

print()

print("Juego 2:")
print("Nombre:", juego2.nombre)
print("Género:", juego2.genero)
print("Clasificación de edad:", juego2.clasificacion_edad)

print()

print("Juego 3:")
print("Nombre:", juego3.nombre)
print("Género:", juego3.genero)
print("Clasificación de edad:", juego3.clasificacion_edad)


# Verificar si el jugador cumple con la clasificación de edad de cada juego

if juego1.verificar_edad(edad_jugador) and juego2.verificar_edad(edad_jugador) and juego3.verificar_edad(edad_jugador):
    print("El jugador cumple con la clasificación de edad para jugar todos los juegos")
    print()
else:    
    if juego1.verificar_edad(edad_jugador):
      print("El jugador cumple con la clasificación de edad para jugar", juego1.nombre)
      print()

    if juego2.verificar_edad(edad_jugador):
     print("El jugador cumple con la clasificación de edad para jugar", juego2.nombre)
     print()
    
    if juego3.verificar_edad(edad_jugador):
      print("El jugador cumple con la clasificación de edad para jugar", juego3.nombre)
      print()
      
    else:
      print("Lo siento, el jugador no cumple con la clasificación de edad para jugar ningún juego")    
        
'''
Como en el reto de los libros por comodidad he asignado los juegos y sus atributos a variables , sin necesidad de tomar los datos del usuario.
Pero si se quisiera tomar los datos del usuario se podria hacer de la siguiente manera:

juego1 = Juego(input("Ingrese el nombre del juego: "), input("Ingrese el genero del juego: "), int(input("Ingrese la clasificacion de edad del juego: ")))
juego2 = Juego(input("Ingrese el nombre del juego: "), input("Ingrese el genero del juego: "), int(input("Ingrese la clasificacion de edad del juego: ")))
juego3 = Juego(input("Ingrese el nombre del juego: "), input("Ingrese el genero del juego: "), int(input("Ingrese la clasificacion de edad del juego: ")))

Mismo procedimiento aplicado en el reto de los libros, solo que en este caso el reto es mas interesante ya que se puede hacer uso de la funcion verificar_edad
Por lo cual se puede verificar si el jugador cumple con la clasificacion de edad de cada juego.
'''
