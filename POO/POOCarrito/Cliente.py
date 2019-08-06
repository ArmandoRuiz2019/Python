from Carrito import*


class Cliente:

  #Constructor. Esta clase contiene tres atributos, uno de ellos es un carrito que permite a los clientes guardar los productos que se adquieren durante la visita a nuestra tienda.
  def __init__(self, nombre, saldo):
    self.nombre = nombre
    self.saldo = saldo
    self.carrito = Carrito( )
    
  #Sobreescribimos el método mostrarDetalles
  def __str__(self):
    
    cadena = "\nNombre del cliente: " + self.nombre
    cadena +="\nSaldo: " + str(self.saldo) + " pesos"
    return cadena