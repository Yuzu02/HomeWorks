# Importamos las librerias necesarias

import random
import string

# Definimos la función que genera la contraseña
def generate_password(length, use_uppercase, use_digits, use_punctuation):
    """
    Genera una contraseña aleatoria con la longitud especificada.
    """
    # Definimos los caracteres que se pueden usar
    chars = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
    if use_uppercase: # Si se especifica que se usen mayúsculas
        chars += string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if use_digits: # Si se especifica que se usen dígitos
        chars += string.digits # 0123456789
    if use_punctuation: # Si se especifica que se usen signos de puntuación
        chars += string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  
    
    password = ''.join(random.choice(chars) for i in range(length)) # Genera la contraseña
    return password # Retorna la contraseña

# Generamos una contraseña de acuerdo a los parámetros especificados por el usuario

length = int(input("Ingrese la longitud de la contraseña: ")) # Pedimos la longitud de la contraseña
use_uppercase = input("¿Usar mayúsculas? (s/n): ") == 's' # Pedimos si se usan mayúsculas
use_digits = input("¿Usar dígitos? (s/n): ") == 's' # Pedimos si se usan dígitos
use_punctuation = input("¿Usar signos de puntuación? (s/n): ") == 's' # Pedimos si se usan signos de puntuación
password = generate_password(length, use_uppercase, use_digits, use_punctuation) # Generamos la contraseña

# Mostramos la contraseña generada
print("La contraseña generada es: " + password) # Mostramos la contraseña generada


'''
Ejemmplo de uso

Ingrese la longitud de la contraseña: 10
Ingrese si se usan mayúsculas (s/n): s
Ingrese si se usan dígitos (s/n): s
Ingrese si se usan signos de puntuación (s/n): s
La contraseña generada es: 4$9!3%9&
'''
