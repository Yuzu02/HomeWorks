# Definición de la función tennis_game
def tennis_game(game): # game es una lista de strings con los puntos de cada jugador

    score = {'P1': 0, 'P2': 0} # Diccionario que guarda el puntaje de cada jugador
    for point in game: # Itera sobre cada punto
        score[point] += 1 # Suma 1 al puntaje del jugador que hizo el punto
        if score['P1'] >= 4 and score['P2'] >= 4: # Si ambos jugadores tienen 4 o más puntos
            if score['P1'] == score['P2']: # Si ambos jugadores tienen el mismo puntaje
                print("Deuce") # Imprime Deuce
            elif score['P1'] - score['P2'] == 1: # Si el puntaje del jugador 1 es 1 mayor al del jugador 2
                print("Ventaja P1") # Imprime Ventaja P1
            elif score['P2'] - score['P1'] == 1: # Si el puntaje del jugador 2 es 1 mayor al del jugador 1
                print("Ventaja P2") # Imprime Ventaja P2
            elif score['P1'] - score['P2'] >= 2: # Si el puntaje del jugador 1 es 2 o más mayor al del jugador 2
                print("Ha ganado el P1") # Imprime Ha ganado el P1
                return # Retorna
            elif score['P2'] - score['P1'] >= 2: # Si el puntaje del jugador 2 es 2 o más mayor al del jugador 1
                print("Ha ganado el P2") # Imprime Ha ganado el P2
                return # Retorna
        else: # Si no se cumple ninguna de las condiciones anteriores
            if score['P1'] == 0: # Si el puntaje del jugador 1 es 0
                print("Love - ", end='') # Imprime Love - (end='' evita que se imprima un salto de línea)
            elif score['P1'] == 1: # Si el puntaje del jugador 1 es 1
                print("15 - ", end='') # Imprime 15 - (end='' evita que se imprima un salto de línea)
            elif score['P1'] == 2: # Si el puntaje del jugador 1 es 2
                print("30 - ", end='') # Imprime 30 - (end='' evita que se imprima un salto de línea)
            elif score['P1'] == 3: # Si el puntaje del jugador 1 es 3
                print("40 - ", end='') # Imprime 40 - (end='' evita que se imprima un salto de línea)
            if score['P2'] == 0: # Si el puntaje del jugador 2 es 0
                print("Love") # Imprime Love
            elif score['P2'] == 1: # Si el puntaje del jugador 2 es 1
                print("15") # Imprime 15
            elif score['P2'] == 2: # Si el puntaje del jugador 2 es 2
                print("30") # Imprime 30
            elif score['P2'] == 3: # Si el puntaje del jugador 2 es 3
                print("40") # Imprime 40

game = input("Ingrese el juego: ") # Ejemplo: P2 P1 P2 P1 P2 P1 P2 P2
tennis_game(game) # Llama a la función

'''
Ejemplo de uso
game = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
tennis_game(game)
'''
