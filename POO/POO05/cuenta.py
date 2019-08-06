''' 
Created on Agosto, 2019
@author: Armando Ruiz
''' 

class Cuenta:

	def __init__( self, valor ):
		self.__cantidad = valor

	def depositar( self, valor ):
		if valor > 0:
			self.__cantidad = self.__cantidad + valor
		else:
			print ( "El valor para depositar es erroneo::" )

	"""
	Este método se hereda
	"""
	def __str__( self ):
		return "Metodo Clase Madre::La cantidad de la cuenta::" + str( self.__cantidad )