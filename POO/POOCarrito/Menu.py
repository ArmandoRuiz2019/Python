from Tienda import*

class Menu:

  #Constructor
  def __init__(self):
    
    self.bienvenido = "Bienvenido a la Tiendita"
    self.tienda = Tienda()

  #Método que crea un objeto cliente.
  def registra_cliente(self):

    print("Ingrese nombre: ")
    nombre = input() 
    print("Ingrese su saldo: ")
    saldo = input()
    clienteDeLaTienda = Cliente( nombre, saldo )
    self.tienda.asigna_cliente( clienteDeLaTienda )

    
  def menu_principal( self ):

    while True:
      mensaje = "\t\t\t***** MENU PRINCIPAL \n"
      mensaje += "1. Agregar producto al carrito\n"
      mensaje += "2. Eliminar producto del carrito\n"
      mensaje += "3. Conocer el status del carrito\n"
      mensaje += "4. Comprar productos\n"
      mensaje += "5. Mostrar estadisticas\n"
      mensaje += "6. Salir\n"

      print ( mensaje )
      eleccion = input( "Teclee una opcion:" )
    
      if eleccion == "1":
        self.menu_agrega_producto()
      elif eleccion == "3":
        self.menu_status_carrito()
      elif eleccion == "6":
        break

  def menu_agrega_producto( self ):

    mensaje = "\t\t\t***** MENU AGREGA PRODUCTO AL CARRITO\n"
    mensaje += "\t\t\tEstos son los productos con los que contamos:\n\n"
    
    print ( mensaje )
    self.tienda.imprimir_almacen()
    eleccion = input( "\nTeclee el producto a agregar:" )
    self.tienda.agrega_producto_a_carrito( int(eleccion) )
    print ("SALIDA::Se agrego el producto elegido\n\n")


  def menu_status_carrito( self ):
    mensaje = "\t\t\t***** MENU STATUS CARRITO\n"
    print( mensaje )
    self.tienda.conoce_status_carrito()
    print ("SALIDA::Se mostraron los productos del carrito\n\n")

  def menu_bienvenida( self ):

    mensaje = "\t\t\tBienvenido a la tienda: PATO \n"
    mensaje += "\t\t\tPara comprar es necesario que se registre \n"
    print( mensaje )