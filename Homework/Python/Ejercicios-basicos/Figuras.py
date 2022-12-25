# Función que dibuja una figura
def dibujar_figura(lado, figura): # lado y figura son parámetros
  
    # Comprobamos que la figura es correcta  
    if figura == "cuadrado": # lado es un parámetro
        for i in range(lado): # figura es un parámetro
            print("*" * lado) # lado es un parámetro
    elif figura == "triangulo": # lado es un parámetro
        for i in range(lado): # figura es un parámetro
            print("*" * (i + 1)) # lado es un parámetro
    elif figura == "rectangulo": # lado es un parámetro
        for i in range(lado): # figura es un parámetro
            print("*" * (lado + 5)) # lado es un parámetro
    else: # si no es ninguna de las anteriores
        print("Figura no reconocida") # Muestra un mensaje de error
        
# Entrada de datos
lado = int(input("Introduce el lado: ")) # lado es un parámetro
figura = input("Introduce la figura (cuadrado, triangulo, rectangulo): ") # figura es un parámetro

# Llamada a la función
dibujar_figura(lado, figura) # lado y figura son argumentos

# Comentar o descomentar las siguientes líneas para probar el programa

# Pruebas

# dibujar_figura(5, "cuadrado") # Dibuja un cuadrado de lado 5
# dibujar_figura(5, "triangulo") # Dibuja un triángulo de lado 5
# dibujar_figura(10, "rectangulo") # Dibuja un cuadrado de lado 10
