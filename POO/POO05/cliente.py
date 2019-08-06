''' 
Created on Agosto, 2019 
@author: Armando Ruiz
''' 

from cuenta import *

class Cliente :
	def __init__( self, n, d, e, c ) :
		self.nombre = n
		self.direccion = d
		self.edad = e
		self.cuenta = c

	def __str__( self ):
		tmp = "Nombre::" + str( self.nombre )
		tmp += "\nDireccion::" + str( self.direccion )
		tmp += "\nEdad::" + str( self.edad )
		tmp += "\nLa cuenta::" + str( self.cuenta )
		return tmp