# Creamos la funcion con los condicionales if , elif y else para cada caso de la nota con su literal.
def obtener_literal(nota_final): # Definimos la función
  if nota_final >= 90 and nota_final <= 100: # Si la nota final es mayor o igual a 90 y menor o igual a 100, el literal es A
    literal = 'A' # Asignamos el literal a la variable literal
  elif nota_final >= 80 and nota_final <= 89: # Si la nota final es mayor o igual a 80 y menor o igual a 89, el literal es B
    literal = 'B' # Asignamos el literal a la variable literal
  elif nota_final >= 75 and nota_final <= 79: # Si la nota final es mayor o igual a 75 y menor o igual a 79, el literal es C
    literal = 'C' # Asignamos el literal a la variable literal
  elif nota_final >= 70 and nota_final <= 74: # Si la nota final es mayor o igual a 70 y menor o igual a 74, el literal es D
    literal = 'D' # Asignamos el literal a la variable literal
  else: # Si la nota final es menor a 70, el literal es F
    literal = 'F' # Asignamos el literal a la variable literal
  return nota_final, literal # Devolvemos la nota final y el literal

# Pedimos al usuario que ingrese la nota final del estudiante
nota_final = int(input('Ingrese la nota final del estudiante: '))

# Llamamos a la función y almacenamos el resultado en una variable
resultado = obtener_literal(nota_final)

# Imprimimos en pantalla la nota final y el literal
print(f'La nota final del estudiante es {resultado[0]} y el literal es {resultado[1]}')

# Ejemplo de uso
# Ingrese la nota final del estudiante: 85
# La nota final del estudiante es 85 y el literal es B

# Ingrese la nota final del estudiante: 95
# La nota final del estudiante es 95 y el literal es A

# Ingrese la nota final del estudiante: 65
# La nota final del estudiante es 65 y el literal es F

# Ingrese la nota final del estudiante: 75
# La nota final del estudiante es 75 y el literal es C

# Ingrese la nota final del estudiante: 70
# La nota final del estudiante es 70 y el literal es D
