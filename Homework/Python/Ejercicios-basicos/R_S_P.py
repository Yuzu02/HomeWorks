# Funcion que determina quién gana la partida
def piedra_papel_tijera(jugadas):
  # Creamos un diccionario con las reglas del juego
  reglas = { # Player 1: Player 2
    
    # R= Piedra. 
    # S= Tijera.
    # P= Papel

    "R": "S", # Piedra gana a Tijera
    "S": "P", # Tijera gana a Papel
    "P": "R" # Papel gana a Piedra

    # Si Player 1 elige Piedra, gana a Tijera
    # Si Player 1 elige Tijera, gana a Papel
    # Si Player 1 elige Papel, gana a Piedra

    # Si Player 2 elige Piedra, pierde con Tijera
    # Si Player 2 elige Tijera, pierde con Papel
    # Si Player 2 elige Papel, pierde con Piedra
    # Si Player 1 y Player 2 eligen lo mismo, es empate
    
  }

  # Inicializamos las variables de conteo
  contador_player1 = 0 # Contador de partidas ganadas por Player 1
  contador_player2 = 0 # Contador de partidas ganadas por Player 2

  # Iteramos sobre las jugadas
  for jugada in jugadas: # jugada = ("R","S")
    player1 = jugada[0] # player1 = "R"
    player2 = jugada[1] # player2 = "S"

    # Verificamos quién gana la partida
    if player1 == player2: # Si es empate, no sumamos nada y
      continue # continuamos con la siguiente partida
    elif reglas[player1] == player2: # Si gana Player 1
      contador_player1 += 1 # Sumamos 1 a las partidas ganadas por Player 1
    else: # Si gana Player 2
      contador_player2 += 1 # Sumamos 1 a las partidas ganadas por Player 2

  # Determinamos quién gana la partida
  if contador_player1 > contador_player2: # Si gana Player 1
    return "Player 1" # Retornamos el nombre del ganador
  elif contador_player2 > contador_player1: # Si gana Player 2
    return "Player 2" # Retornamos el nombre del ganador
  else: # Si es empate
    return "Tie"# Retornamos el nombre del ganador
  
 # Funcion Principal
def main():
   # Inicializamos las variables
   jugadas = [] # Lista de jugadas
   player1 = "" # Jugada del Player 1
   player2 = "" # Jugada del Player 2

   # Pedimos las jugadas
   player1 = input("Jugador 1: ")
   player2 = input("Jugador 2: ")

   # Agregamos las jugadas a la lista
   jugadas.append((player1, player2))

   # Mostramos el resultado
   print(piedra_papel_tijera(jugadas))

# Llamamos a la funcion principal

main()

#Comentar o descomentar las pruebas que se quieran realizar

# Pruebas

# jugadas = [("R","S"), ("S","R"), ("P","S")]
# print(piedra_papel_tijera(jugadas))  # Player 2
# jugadas = [("R","R"), ("S","S"), ("P","P")]
# print(piedra_papel_tijera(jugadas))  # Tie
# jugadas = [("R","S"), ("S","P"), ("P","R")]
# print(piedra_papel_tijera(jugadas))  # Player 1
