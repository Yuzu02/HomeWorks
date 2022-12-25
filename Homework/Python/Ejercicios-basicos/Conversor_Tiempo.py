# Función que convierte segundos a horas, minutos y segundos
def conversor_tiempo(tiempo_en_segundos): # tiempo_en_segundos es un parámetro
  # Calculamos el número de días 
  dias = tiempo_en_segundos // 86400 # 86400 segundos son 1 día
  tiempo_en_segundos %= 86400 # El resto de la división son los segundos restantes

  # Calculamos el número de horas
  horas = tiempo_en_segundos // 3600 # 3600 segundos son 1 hora
  tiempo_en_segundos %= 3600 # El resto de la división son los segundos restantes

  # Calculamos el número de minutos
  minutos = tiempo_en_segundos // 60 # 60 segundos son 1 minuto
  tiempo_en_segundos %= 60 # El resto de la división son los segundos restantes

  # Los segundos restantes son los segundos
  segundos = tiempo_en_segundos # No hace falta calcular nada

  # Mostramos el resultado
  print(f"{dias} días, {horas} horas, {minutos} minutos, {segundos} segundos") # f-strings

# función principal

# Entrada de datos
tiempo_en_segundos = int(input("Introduce el tiempo en segundos: "))
# Llamada a la función
conversor_tiempo(tiempo_en_segundos)

# Comentar o descomentar las siguientes líneas para probar el programa

# Pruebas

conversor_tiempo(86400)  # 1 día, 0 horas, 0 minutos, 0 segundos
conversor_tiempo(3600)  # 0 días, 1 horas, 0 minutos, 0 segundos
conversor_tiempo(60)  # 0 días, 0 horas, 1 minutos, 0 segundos
conversor_tiempo(1)  # 0 días, 0 horas, 0 minutos, 1 segundos
