import csv

# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 

csvarchivo = open('ejemplo08/datos.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
for reg in entrada:
	print(reg)  # Mostrar registro
	nombre, provincia, consumo = next(entrada)  # Leer campos
	print(nombre, provincia, consumo)  # Mostrar campos
	
del nombre, provincia, consumo, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
del csvarchivo  # Borrar objeto