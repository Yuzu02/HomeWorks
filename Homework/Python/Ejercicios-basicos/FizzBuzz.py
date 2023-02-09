# Fizz Buzz

for i in range(1, 101): # 1 a 100
    if i % 3 == 0 and i % 5 == 0: # si es divisible entre 3 y 5 
        print("fizzbuzz") # imprime fizzbuzz
    elif i % 3 == 0: # si es divisible entre 3
        print("fizz") # imprime fizz
    elif i % 5 == 0: # si es divisible entre 5
        print("buzz") # imprime buzz
    else: # si no es divisible entre 3 o 5
     print(i) # imprime el numero
     
''' Explicacion
El programa imprime los numeros del 1 al 100
Los numeros divisibles entre 3 se reemplazan por fizz
Los numeros divisibles entre 5 se reemplazan por buzz
Los numeros divisibles entre 3 y 5 se reemplazan por fizzbuzz
Los numeros que no son divisibles entre 3 o 5 se imprimen como estan            
'''      
