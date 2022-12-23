# Descripción: Ejercicio 6  - Escribir una función que reciba un número entero y devuelva True si es par o False si es impar.

# Pedimos al usuario que ingrese un número entero
def es_par(numero): # Definimos la función
  if numero % 2 == 0: # Si el número es divisible por 2, es par
    return "El número es par" # Devolvemos el resultado
  else: # Si el número no es divisible por 2, es impar
    return "El número es impar" # Devolvemos el resultado

numero = int(input("Ingrese un número entero: ")) # Pedimos al usuario que ingrese un número entero
resultado = es_par(numero) # Llamamos a la función y guardamos el resultado
print(resultado) # Imprimimos el resultado

# Ejemplo de uso
# Ingrese un número entero: 7
# El número es impar
# Ingrese un número entero: 8
# El número es par
