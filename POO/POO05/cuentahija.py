''' 
Created on Agosto, 2019
@author: Armando Ruiz
''' 

from cuenta import *

class CuentaHija(Cuenta):

	def __init__( self, valor, tipo ):
		Cuenta.__init__(self, valor)
		self.__tipo = tipo