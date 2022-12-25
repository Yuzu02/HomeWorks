# Función que calcula la ley de Ohm
def ley_de_ohm(v, r, i): # Definimos la función ley_de_ohm con tres parámetros
      
  # Si no se han proporcionado dos parámetros, retornamos "Invalid values"
  if (v is None and r is None) or (v is None and i is None) or (r is None and i is None): # is es un operador de identidad
    return "Invalid values" # Retornamos un valor nulo

  # Si se ha proporcionado el voltaje y la resistencia, calculamos la corriente
  if v is not None and r is not None: # is es un operador de identidad
    return round(v / r, 2) # round es una función que redondea un número

  # Si se ha proporcionado el voltaje y la corriente, calculamos la resistencia
  if v is not None and i is not None: # is es un operador de identidad
    return round(v / i, 2) # round es una función que redondea un número

  # Si se ha proporcionado la resistencia y la corriente, calculamos el voltaje
  if r is not None and i is not None: # is es un operador de identidad
    return round(r * i, 2) # round es una función que redondea un número

# Pedimos los valores al usuario
v = float(input("Introduce el voltaje: ")) #
r = float(input("Introduce la resistencia: "))
i = float(input("Introduce la corriente: "))

if v == 0:
  v = None
if r == 0:
    r = None
if i == 0:
    i = None
    

# Mostramos el resultado
print(ley_de_ohm(v, r, i))


# Comeentar o descomentar para probar el código

# Pruebas
