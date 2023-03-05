# Invertir una cadena de texto: Escribe una función que reciba una cadena de texto y la devuelva invertida.

# Definimos la función

def invertir(cadena): # Recibe una cadena de texto
    invertida = "" # Cadena vacía
    for i in range(len(cadena) - 1, -1, -1): # Recorremos la cadena de texto
        invertida += cadena[i] # Añadimos el carácter a la cadena invertida
    return invertida # Devolvemos la cadena invertida

# Pedimos la cadena de texto y la invertimos

cadena = input("Introduce una cadena de texto: ")

# Mostramos la cadena invertida

print("La cadena invertida es", invertir(cadena))

# Ejemplo de ejecución:

# Introduce una cadena de texto: Yuzu

# La cadena invertida es uzuY
