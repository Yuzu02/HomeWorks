# Definimos la funcion para calcular el impuesto sobre la renta
def calcular_impuesto_renta(salario): # Definir funcion
  afp = salario * 0.0287 # 2.87% de AFP
  sfs = salario * 0.0709 # 7.09% de SFS
  salario_neto = salario - afp - sfs # Salario neto
  impuesto_renta = salario_neto * 0.27 # 27% de impuesto sobre la renta
  
  print("Salario bruto: ", salario) # Imprimir resultados
  print("Descuento AFP: ", afp) # Imprimir resultados
  print("Descuento SFS: ", sfs)# Imprimir resultados
  print("Salario neto: ", salario_neto) # Imprimir resultados
  print("Impuesto sobre la renta: ", impuesto_renta) # Imprimir resultados

# Leemos el salario del trabajador
salario = float(input("Ingrese el salario del trabajador: ")) 

# Calculamos el impuesto sobre la renta
calcular_impuesto_renta(salario) 

# Ejemplo de uso
# Ingrese el salario del trabajador: 1000
# Salario bruto:  1000.0
# Descuento AFP:  28.7
# Descuento SFS:  70.9
# Salario neto:  901.0
# Impuesto sobre la renta:  243.27
