''' 
Created on Agosto, 2019 
@author: Armando Ruiz
'''
class Cuenta:

	# La clase ya tiene más de un atributo.
	# En este caso, cambia la cantidad de argumentos que el 
	# constructor recibe
	def __init__( self, ctd, t ):
		self.cantidad = ctd
		self.tipo = t

	def imprimirDetalles( self ):
		# esta salida sólo es para
		# visualizar el momento de la
		# llamada del método
		print ( "Desde el método" ) 
		
		print ( "cantidad::", self.cantidad )
		print ( "tipo::", self.tipo )