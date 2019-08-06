from Cliente import *
from Producto import *
import csv

#Una tienda tiene productos que se ofrecen a los clientes que 
#deseen adquirir y disfrutar de nuestro servicio. 
#Se importan las clases Producto y Cliente para que la tienda 
#se relacione con estas clases.

class Tienda:
  
	def __init__( self ):
		self.cliente = None
		self.almacen = []
		self.set_almacen()
	
	def set_almacen( self ): 

		csvarchivo = open('d:/Productos.csv')  # Abrir archivo csv
		entrada = csv.reader(csvarchivo)  # Leer todos los registros

		for reg in entrada:
			nombre,precio,cantidad = next(entrada)  # Leer campos
			self.almacen.append( Producto(nombre, precio, cantidad))

		del nombre, precio, cantidad, entrada  # Borrar objetos
		csvarchivo.close()  # Cerrar archivo
		del csvarchivo  # Borrar objeto

	def asigna_cliente( self, cliente ):
		self.cliente = cliente

	def imprimir_almacen( self ):
		cont = 1
		for producto in self.almacen:
			print ( str( cont ) + ". " + str( producto ) )
			cont = cont+1

	def agrega_producto_a_carrito( self, opcion ):
		producto = self.almacen[ opcion-1 ]
		self.almacen.remove( producto )		
		self.cliente.carrito.agregar( producto )

	def conoce_status_carrito( self ):
		print ( self.cliente.carrito )