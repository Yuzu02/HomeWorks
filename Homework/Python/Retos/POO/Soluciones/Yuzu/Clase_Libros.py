'''
6- Crear una clase "Libro" que tenga atributos como título, autor y precio. Luego, crea varios objetos de esta clase y muestra sus atributos. Además, agrega un método para calcular el precio con descuento del libro.

• Define la clase "Libro" con los atributos de título, autor y precio.

• Crea varios objetos de la clase "Libro" y establece los valores de sus atributos.

• Agrega un método para calcular el precio con descuento del libro utilizando una tasa de descuento predefinida.

• Imprime los atributos de cada objeto de la clase "Libro" y su precio con descuento calculado.
'''

class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def calcular_precio_descuento(self):
        tasa_descuento = 0.10
        precio_descuento = self.precio * (1 - tasa_descuento)
        return precio_descuento

# Crear varios objetos de la clase "Libro" y establecer sus atributos
libro1 = Libro("El Quijote", "Miguel de Cervantes", 20.0)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 25.0)
libro3 = Libro("La Odisea", "Homero", 15.0)

# Imprimir los atributos de cada objeto y su precio con descuento calculado
print("Libro 1:")
print("Título:", libro1.titulo)
print("Autor:", libro1.autor)
print("Precio:", libro1.precio)
print("Precio con descuento:", libro1.calcular_precio_descuento())

print("Libro 2:")
print("Título:", libro2.titulo)
print("Autor:", libro2.autor)
print("Precio:", libro2.precio)
print("Precio con descuento:", libro2.calcular_precio_descuento())

print("Libro 3:")
print("Título:", libro3.titulo)
print("Autor:", libro3.autor)
print("Precio:", libro3.precio)
print("Precio con descuento:", libro3.calcular_precio_descuento())

'''
En este caso no tomamos input del usuario, sino que creamos tres objetos de la clase libro y le asignamos los valores a cada uno de ellos para mayor comodidad
Pero el resto del codigo es igual a los retos anteriores , solo que en este caso se crea una clase con tres atributos y un metodo para calcular el precio con descuento

Si se desea que el usuario ingrese los datos de los libros, se puede hacer de la siguiente manera:

libro1 = Libro(input("Ingrese el titulo del libro 1: "), input("Ingrese el autor del libro 1: "), float(input("Ingrese el precio del libro 1: ")))
libro2 = Libro(input("Ingrese el titulo del libro 2: "), input("Ingrese el autor del libro 2: "), float(input("Ingrese el precio del libro 2: ")))
libro3 = Libro(input("Ingrese el titulo del libro 3: "), input("Ingrese el autor del libro 3: "), float(input("Ingrese el precio del libro 3: ")))

Y el resto del codigo es igual
'''
