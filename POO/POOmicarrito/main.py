from productos import *
from carrito import *
import os
#global LstProductos, codigo ,nombre ,precio ,stock 
LstProductos =list()
codigo=""
nombre=""
precio=0
stock=0
		
def registrarproductos():
    print("Registro de Productos")
    codigo = input("El Codigo:")
    nombre = input("El Producto:")
    precio = input("El Precio:")
    stock = input("El Stock:")
    prod = Productos(codigo,nombre,precio,stock)
    print ("Imprimo el Metodo __str__:", prod )
    LstProductos.append(prod)
    
def micarrito():
    resp = ""
    car = Carrito() 
    while resp!='N':
        print("Catalogo de Productos")
        for prod in LstProductos:
            print(prod.codigo,"-",prod.nombre,"-",prod.precio,"-",prod.stock)
        produ = input("Ingrese el Producto que Añadira al Carrito:")  
        car.agregar(produ)
        #print("En mi Canasta Hay:",car.cantidad())
        print("En mi Canasta Hay:",car)
        resp = input("Desea Agregar Otro Producto:")
        os.system('cls')

def menu():
    op = 0
    salir = 3
    while op != salir:
        print ("Menu")
        print("1-Registrar Producto")
        print("2-Añadir Carrito")
        print("3-Salir")
        op = input("Digite Opción:")
        if op == "1":
            registrarproductos()
        elif op == "2":
            micarrito()
        else :
            exit()
menu()






