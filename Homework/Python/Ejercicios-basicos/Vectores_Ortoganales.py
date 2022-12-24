# Función que verifica si dos vectores son ortogonales
def son_ortogonales(vector1, vector2): # vector1 y vector2 son listas de números
  # Verificamos que los vectores tengan la misma longitud
  if len(vector1) != len(vector2): # len() devuelve la longitud de un objeto
    raise ValueError("Los vectores deben tener la misma longitud") # raise lanza una excepción

  # Calculamos el producto escalar
  producto_escalar = sum(v1 * v2 for v1, v2 in zip(vector1, vector2)) # zip() crea una lista de tuplas de elementos de dos listas

  # Si el producto escalar es cero, los vectores son ortogonales
  return producto_escalar == 0 # == compara dos objetos

def main():
    
    print ("Escribe el primer vector: ")
    vector1 = input()
    print ("Escribe el segundo vector: ")
    vector2 = input()
  
    if son_ortogonales(vector1, vector2):
        print("Los vectores son ortogonales")
    else:
        print("Los vectores no son ortogonales")

if __name__ == "__main__": # __name__ es una variable especial que contiene el nombre del módulo
    main() # Llamamos a la función main()

# Comentar las siguientes líneas para probar el código en el IDE

# Pruebas
print(son_ortogonales([1, 0, 0], [0, 1, 0]))  # True
print(son_ortogonales([1, 0, 0], [0, 0, 1]))  # True
print(son_ortogonales([1, 0, 0], [1, 1, 1]))  # False
print(son_ortogonales([1, 0, 0], [1, 0, 0]))  # False

# Ejemplo de excepción
print(son_ortogonales([1, 0, 0], [1, 0]))  # ValueError: Los vectores deben tener la misma longitud.
