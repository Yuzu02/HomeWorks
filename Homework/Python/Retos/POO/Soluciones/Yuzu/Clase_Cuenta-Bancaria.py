'''
7- Crear una clase "CuentaBancaria" que tenga atributos como nombre del titular de la cuenta, número de cuenta y saldo. Luego, crea un objeto de esta clase e imprime sus atributos. Además, agrega métodos para depositar y retirar dinero de la cuenta.

• Define la clase "CuentaBancaria" con los atributos de nombre del titular de la cuenta, número de cuenta y saldo.

• Crea un objeto de la clase "CuentaBancaria" y establece los valores de sus atributos.

• Agrega métodos para depositar y retirar dinero de la cuenta, actualizando el saldo en consecuencia.

• Imprime los atributos del objeto de la clase "CuentaBancaria", su saldo actual y realiza algunas transacciones de depósito y retiro para demostrar el funcionamiento de los métodos.

'''

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

# Solicitar los datos del usuario
titular = input("Ingrese el nombre del titular: ")
numero_cuenta = input("Ingrese el número de cuenta: ")
saldo = float(input("Ingrese el saldo inicial: "))

# Crear un objeto de la clase "CuentaBancaria"
cuenta = CuentaBancaria(titular, numero_cuenta, saldo)

# Imprimir los atributos del objeto
print("Titular:", cuenta.titular)
print("Número de cuenta:", cuenta.numero_cuenta)
print("Saldo:", cuenta.saldo)

# Permitir al usuario seleccionar si desea depositar, retirar o ambas
opcion = input("¿Desea depositar (D), retirar (R) o ambas (A)? ")

if opcion.upper() == "D":
    cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
    cuenta.depositar(cantidad_deposito)
    print("Nuevo saldo después de depositar:", cuenta.saldo)

elif opcion.upper() == "R":
    cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(cantidad_retiro)
    print("Nuevo saldo después de retirar:", cuenta.saldo)

elif opcion.upper() == "A":
    cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
    cuenta.depositar(cantidad_deposito)
    cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(cantidad_retiro)
    print("Nuevo saldo después de depositar y retirar:", cuenta.saldo)

else:
    print("Opción inválida")
    
# Ejemplo de ejecución:
# Titular: Yuzu Lied
# Número de cuenta: 123456789
# Saldo: 1000.0
# Nuevo saldo después de depositar: 2000.0
# Nuevo saldo después de retirar: 1500.0   
