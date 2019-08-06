''' 
Created on Agosto, 2019
@author: Armando Ruiz

Este ejemplo muestra como se usa el __str__
1. Teníamos para mostrar los detalles del objeto el metodo "mostrarDetalles"
2. Si queremos imprimir un objeto, saca una referencia a la memoria
3. entonces definimos el metodo __string__ que regresa una cadena
4. y ya podemos imprimir un objeto
5. cambiamos mostrarDetalles en todas las clases por este nuevo
''' 

from cuenta import *
from cliente import *

class Pruebas:
	pass
print ( "Desde las pruebas" )
cuenta1 = Cuenta( 300 )
print ( cuenta1 )
cuenta1.depositar( 400 )
print ( cuenta1 )

"""
Imprimimos un objeto y nos mandará una referencia en la memoria
si es que no tenemos reescrito el me´todo __str__
"""
print ("Objeto cuenta::", cuenta1)

cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
print ("Objeto cliente::", cliente )