''' 
Created on Agosto,2019 
@author: Armando Ruiz
'''
class Cuenta:

	def __init__(self, valor):
		self.cantidad = valor

	def depositar(self, valor):
		if valor > 0:
			self.cantidad = self.cantidad + valor
		else:
			print ("El valor para depositar es erroneo::")

	def mostrarDetalles(self):
		print ("La cantidad de la cuenta::", self.cantidad)