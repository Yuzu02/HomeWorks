# Función que convierte temperaturas entre Celsius, Fahrenheit y Kelvin
def convertir_temperatura(valor, medida_inicial, medida_final): # valor es un número, medida_inicial y medida_final son cadenas
  if medida_inicial == "C" and medida_final == "F": # Si la medida inicial es Celsius y la final es Fahrenheit
    return valor * 9/5 + 32 # Retornamos el valor convertido a Fahrenheit
  elif medida_inicial == "F" and medida_final == "C": # Si la medida inicial es Fahrenheit y la final es Celsius
    return (valor - 32) * 5/9 # Retornamos el valor convertido a Celsius
  elif medida_inicial == "C" and medida_final == "K": # Si la medida inicial es Celsius y la final es Kelvin
    return valor + 273.15 # Retornamos el valor convertido a Kelvin
  elif medida_inicial == "K" and medida_final == "C": # Si la medida inicial es Kelvin y la final es Celsius
    return valor - 273.15 # Retornamos el valor convertido a Celsius
  else: # Si no se cumplen las condiciones anteriores
    return "Ingrese medidas válidas (C, F o K)" # Retornamos un mensaje de error

# Solicitamos el valor de la temperatura a convertir
valor = float(input("Valor de la temperatura a convertir: "))
# Solicitamos la medida inicial de la temperatura
medida_inicial = input("Medida inicial de la temperatura (C, F o K): ")
# Solicitamos la medida final de la temperatura
medida_final = input("Medida final de la temperatura (C, F o K): ")
# Imprimimos el valor de la temperatura a convertir
print(valor)
# Imprimimos la medida inicial de la temperatura
print(medida_inicial)
# Imprimimos la medida final de la temperatura
print(medida_final)
# Invocamos la función convertir_temperatura pasándole como parámetros el valor, la medida inicial y la medida final
print(convertir_temperatura(valor, medida_inicial, medida_final))

# Ejemplo de ejecución:
# Valor de la temperatura a convertir: 100
# Medida inicial de la temperatura (C, F o K): C
# Medida final de la temperatura (C, F o K): F
# 100.0
# C
# F
# 212.0
