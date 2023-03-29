'''
8- Crear una clase "Coche" que tenga atributos como modelo, marca y velocidad máxima. Luego, crea un objeto de esta clase e imprime sus atributos. Además, agrega métodos para acelerar y frenar el coche.

• Define la clase "Coche" con los atributos de modelo, marca y velocidad máxima.

• Crea un objeto de la clase "Coche" y establece los valores de sus atributos.

• Agrega métodos para acelerar y frenar el coche, actualizando su velocidad en consecuencia.

• Imprime los atributos del objeto de la clase "Coche", su velocidad actual y realiza algunas acciones de aceleración y frenado para demostrar el funcionamiento de los métodos.
'''

class Coche:
    FRICCION_CARRETERA = 0.1

    def __init__(self, modelo, marca, velocidad_maxima):
        self.modelo = modelo
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, cantidad):
        aceleracion_real = cantidad - (self.FRICCION_CARRETERA * self.velocidad_actual)
        if aceleracion_real < 0:
            aceleracion_real = 0
        if (self.velocidad_actual + aceleracion_real) <= self.velocidad_maxima:
            for i in range(int(aceleracion_real)):
                self.velocidad_actual += 1
        else:
            self.velocidad_actual = self.velocidad_maxima

    def frenar(self, cantidad):
        frenado_real = cantidad + (self.FRICCION_CARRETERA * self.velocidad_actual)
        if frenado_real < 0:
            frenado_real = 0
        if (self.velocidad_actual - frenado_real) >= 0:
            for i in range(int(frenado_real)):
                self.velocidad_actual -= 1
        else:
            self.velocidad_actual = 0

# Solicitar los datos del usuario
modelo = input("Ingrese el modelo del coche: ")
marca = input("Ingrese la marca del coche: ")
velocidad_maxima = float(input("Ingrese la velocidad máxima del coche: "))

# Crear un objeto de la clase "Coche"
coche = Coche(modelo, marca, velocidad_maxima)

# Imprimir los atributos del objeto
print("Modelo:", coche.modelo)
print("Marca:", coche.marca)
print("Velocidad máxima:", coche.velocidad_maxima)
print("Velocidad actual:", coche.velocidad_actual)

# Permitir al usuario seleccionar si desea acelerar o frenar el coche
opcion = input("¿Desea acelerar (A) o frenar (F)? ")

if opcion.upper() == "A":
    cantidad_aceleracion = float(input("Ingrese la cantidad de aceleración: "))
    coche.acelerar(cantidad_aceleracion)
    print("Velocidad actual después de acelerar:", coche.velocidad_actual)

elif opcion.upper() == "F":
    cantidad_frenado = float(input("Ingrese la cantidad de frenado: "))
    coche.frenar(cantidad_frenado)
    print("Velocidad actual después de frenar:", coche.velocidad_actual)

else:
    print("Opción inválida")
    
# Ejemplo de ejecución:
# Modelo: 2020
# Marca: Toyota
# Velocidad máxima: 200.0
# Velocidad actual: 0

# Velocidad actual después de acelerar: 100.0
# Velocidad actual después de frenar: 50.0
