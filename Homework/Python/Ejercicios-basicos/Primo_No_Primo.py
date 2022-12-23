# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificamos si el número es primo
if numero <= 1: # Si el número es menor o igual a 1, no es primo
  print("El número no es primo") # Imprimimos el resultado
else: # Si el número es mayor a 1, verificamos si es primo
  for i in range(2, numero): # Iteramos desde 2 hasta el número ingresado
    if numero % i == 0: # Si el número es divisible por alguno de los números entre 2 y el número ingresado, no es primo
      print("El número no es primo") # Imprimimos el resultado
      break # Salimos del ciclo
  else: # Si el número no es divisible por alguno de los números entre 2 y el número ingresado, es primo
    print("El número es primo") # Imprimimos el resultado

    # Ejemplo de uso
    # Ingrese un número entero: 7
    # El número es primo
    # Ingrese un número entero: 8
    # El número no es primo
