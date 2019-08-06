    
''' 
Created on Agosto, 2019
@author: Armando Ruiz
Este ejemplo muestra el uso de herencia en Python, con dos clases muy simples (semánticamente no tienen mucho sentido)

En este caso sólo se muestra:
a) La síntáxis para herencia (en "CuentaHija")
b) La herencia de métodos de una clase madre (Cuenta) a una hija (CuentaHija)
	con el método "depositar"
c) Que al heredar hay me´todos que el algoritmo de la madre no es "suficiente" para la hija
	con el método "__str__"
''' 

from cuenta import *
from cuentahija import *
from cliente import *

class Pruebas:
	pass

	print ( "\t *********La clase madre" )
	cuenta1 = Cuenta( 300 )
	print (cuenta1)
	cuenta1.depositar( 400 )
	print (cuenta1)

	print ( "\n\n\t *********La clase hija" )
	cuenta2 = CuentaHija( 200, "debito" )
	print (cuenta2) 
	cuenta2.depositar( 8000 )
	print (cuenta2)

	print ( "\n\n\t *********La clase Cliente" )

	cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
	print ("Objeto cliente::", cliente )