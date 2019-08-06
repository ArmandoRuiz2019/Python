''' 
Created on Agosto, 2019
@author: Armando Ruiz
''' 

from cuenta import *

class CuentaAhorro(Cuenta):
	"""
		En esta versión de la clase sólo incluye como comportamiento
		extra "la tasa de interes"
	"""
	def __init__( self, saldoInicial, tInteres ):
		Cuenta.__init__(self, saldoInicial)
		self.tasaInteres = tInteres

	"""
	Este método se sobreescribe
	"""
	def __str__( self ):
		msg = Cuenta.__str__(self)
		msg += ":tasa de interes:" + str( self.tasaInteres ) 
		return msg