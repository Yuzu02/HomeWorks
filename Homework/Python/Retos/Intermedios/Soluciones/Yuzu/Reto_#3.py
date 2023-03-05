# Comprobar si una cadena de texto es un palíndromo: Escribe una función que reciba una cadena de texto y determine si es un palíndromo o no.

# Aclaracion:
# Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.

# Definimos la función

def palindromo(cadena): # Recibe una cadena de texto
    cadena = cadena.lower() # Pasamos la cadena a minúsculas
    cadena = cadena.replace(" ", "") # Eliminamos los espacios
    if cadena == cadena[::-1]: # Comprobamos si la cadena es igual a su inversa
        return True # Devolvemos True si es un palíndromo
    else:
        return False # Devolvemos False si no es un palíndromo
    
# Pedimos la cadena de texto y comprobamos si es un palíndromo

cadena = input("Introduce una cadena de texto: ")

# Mostramos el resultado

if palindromo(cadena):
    print("Es un palíndromo")
    
else:
    print("No es un palíndromo")
    
# Ejemplo de ejecución para demostrar el funcionamiento de la solución

# Introduce una cadena de texto: Yuzu es un dios todo poderoso

# No es un palíndromo

# Introduce una cadena de texto: La ruta nos aporto otro paso natural

# Es un palíndromo
