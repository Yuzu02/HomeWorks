def leet_speak(text): # Definir función

    leet_dict = { # Definir diccionario
        'a': '4', 'A': '4',
        'b': '8', 'B': '8',
        'c': '(', 'C': '(',
        'd': '|)', 'D': '|)',
        'e': '3', 'E': '3',
        'f': '|=', 'F': '|=',
        'g': '6', 'G': '6',
        'h': '#', 'H': '#',
        'i': '1', 'I': '1',
        'j': '_|', 'J': '_|',
        'k': '|<', 'K': '|<',
        'l': '|_', 'L': '|_',
        'm': '|\/|', 'M': '|\/|',
        'n': '|\|', 'N': '|\|',
        'o': '0', 'O': '0',
        'p': '|D', 'P': '|D',
        'q': '9', 'Q': '9',
        'r': '|2', 'R': '|2',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
        'u': '|_|', 'U': '|_|',
        'v': '\/', 'V': '\/',
        'w': '\/\/', 'W': '\/\/',
        'x': '%', 'X': '%',
        'y': '`/', 'Y': '`/',
        'z': '2', 'Z': '2',
    }
    leet_text = '' # Definir variable
    for char in text: # Definir ciclo
        if char in leet_dict: # Definir condición
            leet_text += leet_dict[char] # Definir variable
        else: # Definir condición
            leet_text += char # Definir variable
    return leet_text # Devolver variable

text = input("Ingresa un texto: ") #  Pedir texto
print("Texto en lenguaje hacker: ", leet_speak(text)) # Imprimir texto

# Ejemplo de uso

# Ingresa un texto: Yuzu
# Texto en lenguaje hacker: `/|_|2|_|
