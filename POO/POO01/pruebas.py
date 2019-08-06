''' 
Created on Agosto,2019 
@author: Armando Ruiz
Este ejemplo muestra el uso del operador punto.
Con este operador se accede a atributos y métodos, definidos en la 
clase.
Usamos la salida estandar sólo para ver que los datos de nuestro objeto 
se han creado de manera adecuada.
'''
from cuenta import *
class Pruebas:
    #La sentencia pass es una operación nula ; No pasa nada cuando se ejecuta. 
    #El pass también es útil en lugares donde su código eventualmente irá, 
    # pero aún no se ha escrito
	pass

print (" probando \n en dos lineas ")
cuenta1 = Cuenta( 300 )
print (cuenta1.cantidad)