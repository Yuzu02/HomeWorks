'''
10- Crear una clase "RedSocial" que tenga atributos como nombre, número de usuarios y año de fundación. Luego, crea varios objetos de esta clase y muestra sus atributos. Además, agrega un método para calcular la cantidad promedio de usuarios nuevos por año.

• Define la clase "RedSocial" con los atributos de nombre, número de usuarios y año de fundación.

• Crea varios objetos de la clase "RedSocial" y establece los valores de sus atributos.

• Agrega un método para calcular la cantidad promedio de usuarios nuevos por año dividiendo el número total de usuarios por la cantidad de años desde la fundación.

• Imprime los atributos de cada objeto de la clase "RedSocial" y su cantidad promedio de usuarios nuevos por año calculada.

'''

class RedSocial:
    def __init__(self, nombre, num_usuarios, ano_fundacion):
        self.nombre = nombre
        self.num_usuarios = num_usuarios
        self.ano_fundacion = ano_fundacion
    
    def calcular_promedio_usuarios_nuevos(self):
        anos_desde_fundacion = 2023 - self.ano_fundacion
        promedio_usuarios_nuevos = self.num_usuarios / anos_desde_fundacion
        return promedio_usuarios_nuevos

# Creamos los objetos de la clase RedSocial con los datos de cada red social
facebook = RedSocial("Facebook", 2800000000, 2004)
twitter = RedSocial("Twitter", 330000000, 2006)
instagram = RedSocial("Instagram", 1000000000, 2010)
linkedin = RedSocial("LinkedIn", 740000000, 2002)
tiktok = RedSocial("TikTok", 1300000000, 2016)
yuzulandia = RedSocial("Yuzulandia", 9999999999999999999, 2023)

# Creamos la variable opcion para que el usuario pueda seleccionar una opcion y que el bucle while dependa de esta variable
opcion = -1

# bucle que salga una sola vez para que no se repita el menu
while opcion == -1:
    print("Seleccione una opción:")
    print()
    print("1: Facebook")
    print("2: Twitter")
    print("3: Instagram")
    print("4: LinkedIn")
    print("5: TikTok")
    print("6: Yuzulandia")
    print("0: Salir")
    opcion = input()

    # Evaluamos la opción seleccionada
    if opcion == "1":
        print(facebook.nombre, facebook.num_usuarios, facebook.ano_fundacion, facebook.calcular_promedio_usuarios_nuevos())
        break 
    elif opcion == "2":
        print(twitter.nombre, twitter.num_usuarios, twitter.ano_fundacion, twitter.calcular_promedio_usuarios_nuevos())
        break
    elif opcion == "3":
        print(instagram.nombre, instagram.num_usuarios, instagram.ano_fundacion, instagram.calcular_promedio_usuarios_nuevos())
        break
    elif opcion == "4":
        print(linkedin.nombre, linkedin.num_usuarios, linkedin.ano_fundacion, linkedin.calcular_promedio_usuarios_nuevos())
        break
    elif opcion == "5":
        print(tiktok.nombre, tiktok.num_usuarios, tiktok.ano_fundacion, tiktok.calcular_promedio_usuarios_nuevos())
        break
    elif opcion == "6":
        print(yuzulandia.nombre, yuzulandia.num_usuarios, yuzulandia.ano_fundacion, yuzulandia.calcular_promedio_usuarios_nuevos())    
        break
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        break
        
# Ejemplo de ejecución:
# 1
# Facebook 2800000000 2004 700000000.0
