import sqlite3
import os
import time

bd = sqlite3.connect("tpv.db")
cursor = bd.cursor()
resp=""

def cargainventario():
	try:
		productos = [
		"""
		INSERT INTO productos(nombre, precio, estado, codcat,barra) 
		values ("Pizza Pollo",28.7,"1",1,"10210902") ,
		("Pizza Vegetariana",18.3,"1",1,"10210903") ,
		("Pizza Quezo",16.2,"1",1,"10210904") ,
		("Pizza Carne",21.3,"1",2,"10210905") ,
		("Pizza Fruta",30.1,"1",2,"10210906")

		"""
	]
		for sentencia in productos:
			cursor.execute(sentencia)
			bd.commit() #Guardamos los cambios al terminar el ciclo
		print("Productos insertados correctamente")
	except sqlite3.OperationalError as error:
		print("Error al abrir:", error) 



def listar():
	try:
		sentencia = "SELECT nombre,precio,estado,codcat FROM productos;"
		cursor.execute(sentencia)
		productos = cursor.fetchall()
		
		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
		print("|{:^50}|{:^20}|{:^10}|{:^10}|".format("Nombre", "Precio", "Estado", "Categoria"))
		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))

		for nombre, precio, estado, codcat in productos:
			print("|{:^50}|{:^20}|{:^10}|{:^10}|".format(nombre, precio, estado, codcat))
		
		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
	except sqlite3.OperationalError as error:
		print("Error al abrir:", error)


def buscar():
	try:
		busqueda = int(raw_input("Ingrese o pistole el codigo de barra: "))
		
		sentencia = "SELECT nombre,precio,estado,codcat FROM productos WHERE barra = "+ str(busqueda)

		cursor.execute(sentencia)
		
	
		productos = cursor.fetchall()
		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
		print("|{:^50}|{:^20}|{:^10}|{:^10}|".format("Nombre", "Precio", "Estado", "Categoria"))
		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))


		for nombre, precio, estado, codcat in productos:
			print("|{:^50}|{:^20}|{:^10}|{:^10}|".format(nombre, precio, estado, codcat))
	

		print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
	except sqlite3.OperationalError as error:
		print("Error al abrir:", error)


def eliminar():
	try:
		busqueda = int(raw_input("Ingrese el codigo del producto: "))
		
		sentencia = "delete FROM productos WHERE codigo = "+ str(busqueda)

		cursor.execute(sentencia)
		bd.commit()
	
		listar()
	except sqlite3.OperationalError as error:
		print("Error al abrir:", error)

def actualizar():
	try:
		busqueda = int(raw_input("Ingrese el codigo del producto: "))
		nomprod = raw_input("Ingrese el nombre del producto: ")
		preprod = int(raw_input("Ingrese el precio del producto: "))
	

		sentencia =" UPDATE productos SET nombre = " + "'" + nomprod +"'," + " precio = " + str(preprod)  + " WHERE codigo =" + str(busqueda)

		cursor.execute(sentencia)
		bd.commit()
	
		listar()
	except sqlite3.OperationalError as error:
		print("Error al abrir:", error)


def menuprincipal():
    opc="0"
    print ("menu principal")
    print ("1.-Carga de Inventario")
    print ("2.-Listado")
    print ("3.-Buscar")
    print ("4.-Eliminar")
    print ("5.-Actualizar")
	
    opc=raw_input("Elija Opcion:")
    if opc=="1":
        cargainventario()        
    elif opc=="2":
        listar()        
    elif opc=="3":
        buscar()
    elif opc=="4":
        eliminar()
    elif opc=="5":
        actualizar()
    else:
        print ("Opcion No Existe")
            
while resp!='N':
    menuprincipal()   
    resp=raw_input("desea continuar:").upper()
    os.system('cls')