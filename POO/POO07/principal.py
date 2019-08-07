from productos import *
global LstProductos, codigo ,producto ,laboratorio ,farmacia ,precio ,stock ,tipo
LstProductos =list()
codigo=""
producto=""
laboratorio=""
farmacia=""
precio=0
stock=0
tipo="1"
def registrarmedicamento():
    print("Registro de Medicamento")
    codigo = input("El Codigo:")
    producto = input("El Producto:")
    laboratorio = input("El Laboratorio:")
    farmacia = input("La Farmacia:")
    precio = input("El Precio:")
    stock = input("El Stock:")
    tipo = input("El Tipo:")
    #"Usando el Constructor para adicionar datos")
    med = Productos(producto,laboratorio,farmacia,precio,stock,tipo,codigo)
    #"Imprimiendo los Valores de las Variables usando el Metodo")
    #med = Productos(producto,laboratorio,farmacia,precio,stock,tipo,codigo).imprimirDetalles()
    #"Añadiendo a la Lista")
    LstProductos.append(med)
    
def listarmedicamento():
    print("Listando Medicamentos")
    for med in LstProductos:
        print(med.codigo,"-",med.producto,"-",med.precio,"-",med.stock)

def buscarmedicamento():
    print("Buscando Medicamentos")
    cod = input("Ingrese el codigo de medicamento a buscar:")
    for med in LstProductos:
        if med.codigo == cod:
            print(med.producto,"-",med.precio)
            

def comprarmedicamento():
    print("Comprar Medicamento")
    cod = input("Ingrese el codigo de medicamento a comprar:")
    for med in LstProductos:
        if med.codigo == cod:
            print(med.producto,"-",med.precio,"-",med.stock)
            stock=med.stock
            cant= int(input("Ingrese la cantidad a comprar:"))
            med = Productos(producto,laboratorio,farmacia,precio,stock,tipo,codigo).comprobarstock(cant)            

def menu():
    op = 0
    salir = 4
    while op != salir:
        print ("Menu")
        print("1-Registrar Medicamento")
        print ("2-Listar Medicamento")
        print ("3-Buscar Medicamento")
        print ("4-Comprar Medicamento")
        print ("5-Salir Medicamento")

        op = input("Digite Opción:")

        if op == "1":
            registrarmedicamento()
        elif op == "2":
            listarmedicamento()
        elif op == "3":
            buscarmedicamento()
        elif op == "4":
            comprarmedicamento()
        else :
            exit()

menu()






