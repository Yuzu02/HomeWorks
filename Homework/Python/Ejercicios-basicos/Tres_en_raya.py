def analizar_matriz(matriz):
  # Verificamos si la matriz tiene el tamaño correcto
  if len(matriz) != 3 or len(matriz[0]) != 3: # SI la matriz no tiene 3 filas o la primera fila no tiene 3 columnas
    return "Nulo" # Si no es así, devolvemos Nulo

  # Verificamos si hay un ganador
  for fila in matriz: # Recorremos las filas
    if fila[0] == fila[1] == fila[2]: # Si la primera, segunda y tercera columna de la fila son iguales
      return fila[0] # Devolvemos el caracter de la primera columna
  for i in range(3): # Recorremos las columnas
    if matriz[0][i] == matriz[1][i] == matriz[2][i]: # Si la primera, segunda y tercera fila de la columna son iguales
      return matriz[0][i] # Devolvemos el caracter de la primera fila
  if matriz[0][0] == matriz[1][1] == matriz[2][2]: # Si la primera, segunda y tercera fila de la primera, segunda y tercera columna son iguales
    return matriz[0][0] # Devolvemos el caracter de la primera fila
  if matriz[0][2] == matriz[1][1] == matriz[2][0]: # Si la primera, segunda y tercera fila de la tercera, segunda y primera columna son iguales
    return matriz[0][2] # Devolvemos el caracter de la primera fila

  # Verificamos si hay un empate
  for fila in matriz: # Recorremos las filas
    for caracter in fila: # Recorremos las columnas
      if caracter != "X" and caracter != "O": # Si el caracter no es X ni O
        return "Nulo" # Devolvemos Nulo
  return "Empate" # Si no es así, devolvemos Empate

# Función principal

def main():
    # Pedimos los datos al usuario
    matriz = [] # Creamos una matriz vacía
    for i in range(3): # Recorremos las filas
        fila = [] # Creamos una fila vacía
        for j in range(3): # Recorremos las columnas
         fila.append(input("Introduce el caracter de la fila " + str(i + 1) + " columna " + str(j + 1) + ": ")) # Añadimos el caracter a la fila
        matriz.append(fila) # Añadimos la fila a la matriz
    
    # Mostramos la matriz
    print("Matriz:")
    for fila in matriz: # Recorremos las filas
        print(fila) # Mostramos la fila

    # Analizamos la matriz
    resultado = analizar_matriz(matriz) # Analizamos la matriz
    if resultado == "Nulo": # Si el resultado es Nulo
        print("No hay ganador") # Mostramos el mensaje
    elif resultado == "Empate": # Si el resultado es Empate
        print("Empate") # Mostramos el mensaje
    else: # Si no es así
        print("Ha ganado el jugador " + resultado) # Mostramos el mensaje

    # Preguntamos si queremos volver a jugar
    if input("¿Desea volver a jugar? (s/n): ") == "s":
        main()
        
# Llamamos a la función principal
main()
    
# Comentar o descomentar las pruebas para probar el programa

# Pruebas

# matriz1 = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
# print(analizar_matriz(matriz1))  # Empate
# matriz2 = [["X", "X", "X"], ["O", "O", "X"], ["X", "O", "O"]]
# print(analizar_matriz(matriz2))  # X
# matriz3 = [["O", "O", "O"], ["X", "X", "O"], ["X", "O", "X"]]
# print(analizar_matriz(matriz3))  # O
# matriz4 = [["O", "O", "O"], ["X", "X", "X"], ["X", "O", "X"]]
# print(analizar_matriz(matriz4))  # Nulo
