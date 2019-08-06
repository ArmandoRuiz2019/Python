''' 
Created on Agosto,2019
@author: Armando Ruiz

Este ejemplo muestra las relaciones entre clases, del tipo "tiene un (a)"
El Cliente tiene una Cuenta.

1. Se tiene que poner un atributo del Cuenta en la clase Cliente
2. En los métodos del Cliente se tienen que usar los métodos de la Cuenta
3. En las pruebas se hace referencia de un objeto Cuenta al objeto Cliente.
'''
from cuenta import *
from cliente import *

class Pruebas:
	pass
print ("Desde las pruebas")
cuenta1 = Cuenta( 300 )
cuenta1.mostrarDetalles()
cuenta1.depositar( 400 )
cuenta1.mostrarDetalles()

cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
cliente.mostrarDetalles()

