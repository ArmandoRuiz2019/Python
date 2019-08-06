''' 
Created on Agosto,2019
@author: Armando Ruiz

* Este ejemplo muestra el uso del operador punto con métodos
* Sobretodo muestra la importancia de definir metodos, 
 que definen la agrupación de varias expresiones para resolver
 algún problema.
'''
from cuenta import *

class Pruebas:
	pass

print ("*** 1. Imprimimos atributos desde el archivo principal")

#la cantidad de argumentos que se le pasa al constructor, cambia
cuenta1 = Cuenta( 300, "debito" )

#si fueran muchos atributos, acá aparecerían muchisimas 
#lineas
print (cuenta1.cantidad)
print (cuenta1.tipo)

print ("\n\n*** 2. Imprimimos atributos con el método")
cuenta1.imprimirDetalles()
