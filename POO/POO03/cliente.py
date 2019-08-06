''' 
Created on Agosto,20189
@author: Armando Ruiz
''' 
from cuenta import *

class Cliente :
	def __init__( self, n, d, e, c ) :
		self.nombre = n
		self.direccion = d
		self.edad = e
		self.cuenta = c

	def mostrarDetalles( self ) :
		print ( "Nombre::", self.nombre )
		print ( "Direccion::", self.direccion )
		print ( "Edad::", self.edad )
		self.cuenta.mostrarDetalles()