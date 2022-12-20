# Definimos las variables que vamos a utilizar y las inicializamos en 0
positivos = 0 # Cantidad de números positivos
negativos = 0 # Cantidad de números negativos
pares = 0 # Cantidad de números pares 
impares = 0 # Cantidad de números impares
mayores_que_10 = 0 # Cantidad de números mayores que 10
menores_que_50 = 0 # Cantidad de números menores que 50

# Pedimos al usuario que ingrese la cantidad de números que desea leer
cantidad = int(input("Ingrese la cantidad de números que desea leer: "))

# Iteramos la cantidad de veces que el usuario ingresó
for i in range(cantidad):
  numero = int(input(f"Ingrese el número {i+1}: "))
  if numero > 0: # Si el número es positivo, sumamos 1 a la variable positivos  
    positivos += 1 
  elif numero < 0: # Si el número es negativo, sumamos 1 a la variable negativos
    negativos += 1 
  if numero % 2 == 0: # Si el número es par, sumamos 1 a la variable impares
    pares += 1 
  else: # Si el número es impar, sumamos 1 a la variable pares
    impares += 1 
  if numero > 10:# Si el número es mayor a 10, sumamos 1 a la variable mayores_que_10
    mayores_que_10 += 1
  if numero < 50:# Si el número es menor a 50, sumamos 1 a la variable menores_que_50
    menores_que_50 += 1 

# Imprimimos los resultados
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números mayores que 10: {mayores_que_10}")
print(f"Cantidad de números menores que 50: {menores_que_50}")

# Ejemplo de uso
# Ingrese la cantidad de números que desea leer: 5
# Ingrese el número 1: -1
# Ingrese el número 2: 6
# Ingrese el número 3: -7
# Ingrese el número 4: 28
# Ingrese el número 5: -3
# Cantidad de números positivos: 2
# Cantidad de números negativos: 3
# Cantidad de números pares: 2
# Cantidad de números impares: 3
# Cantidad de números mayores que 10: 1
# Cantidad de números menores que 50: 5
