import string
import random

# Define la función para generar la contraseña
def generate_password(length=12, chars=string.ascii_letters + string.digits + string.punctuation):
    # Genera una cadena de caracteres aleatorios con una longitud determinada
    # Usando la función random.choice y la concatenación de caracteres
    return ''.join(random.choice(chars) for i in range(length))

# Llama a la función y muestra el resultado en la consola
print(generate_password())
