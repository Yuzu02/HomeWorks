import string # para usar las constantes ascii_lowercase y ascii_uppercase

# Funciones
def karaca_encriptar(texto): # encripta el texto usando la fórmula de Karaca
  # Convertimos el texto a minúsculas
  texto = texto.lower()
 
  # Encriptamos el texto
  encriptado = "" # texto encriptado
  for caracter in texto: # recorremos el texto
    if caracter in string.ascii_lowercase: # si es una letra
      # Aplicamos la fórmula de encriptación
      indice = (string.ascii_lowercase.index(caracter) + 3) % 26 # índice de la letra encriptada
      encriptado += string.ascii_lowercase[indice] # agregamos la letra encriptada
    else: # si no es una letra
      encriptado += caracter # agregamos el caracter sin encriptar

  return encriptado  # retornamos el texto encriptado

def karaca_desencriptar(texto_encriptado): # desencripta el texto usando la fórmula de Karaca
  # Desencriptamos el texto
  desencriptado = "" # texto desencriptado
  for caracter in texto_encriptado: # recorremos el texto encriptado
    if caracter in string.ascii_lowercase:
      # Aplicamos la fórmula de desencriptación
      indice = (string.ascii_lowercase.index(caracter) - 3) % 26 # índice de la letra desencriptada
      desencriptado += string.ascii_lowercase[indice] # agregamos la letra desencriptada
    else: # si no es una letra
      desencriptado += caracter # agregamos el caracter sin desencriptar

  return desencriptado # retornamos el texto desencriptado

# función principal
def main():
 
# Menu de opciones
 print ("") 
print ("Bienevenido al programa de encriptación de Karaca") # mensaje de bienvenida 
print ("1. Encriptar") # opciones
print ("2. Desencriptar") # opciones
opcion = int(input("Ingrese la opción: ")) # leemos la opción
  
# Encriptar
if opcion == 1: # si la opción es 1
  texto = input("Ingrese el texto a encriptar: ") # leemos el texto a encriptar
  encriptado = karaca_encriptar(texto) # encriptamos el texto
  print ("Texto encriptado: " + encriptado) # mostramos el texto encriptado

# Desencriptar
elif opcion == 2: # si la opción es 2
  texto_encriptado = input("Ingrese el texto a desencriptar: ") # leemos el texto a desencriptar
  desencriptado = karaca_desencriptar(texto_encriptado) # desencriptamos el texto


# llamamos a la función principal
main()

# Ejecución

# Encriptar
# Ingrese el texto a encriptar: Hola
# Texto encriptado: krod

# Desencriptar
# Ingrese el texto a desencriptar: krod
# Texto desencriptado: hola
