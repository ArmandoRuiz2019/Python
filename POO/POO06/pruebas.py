''' 
Created on Agosto, 2019
@author: Armando Ruiz


Esta versión incluye el uso de herencia para la clase Cuenta.

- Algo importante a notar es que los atributos de la clase Madre
se han tenido que cambiar de acceso para moder accederlos desde la clase Hija

- En el caso de la clase CuentaDeAhorro no se ha implementado la parte
de los intereses al mes, dado que no estamos en condiciones de hacerlo, aún.

- En el caso de la clase CuentaDeCredito se tuvo que sobreescribir el método "retirar"
 para que se adecue a la especificación, en este se envía un mensaje a la consola cuando no se logra 
 hacer el retiro, mismo que no debería ir, en un sentido estricto de diseño, pues se regresa un valor booleano, 
 sin embargo en esta versión se realizó, para resaltar este caso.
''' 

from cuenta import *
from cuentaahorro import *
from cuentacredito import *

class Pruebas:
	pass

	print ( "\t *********Un objeto Cuenta" )
	cuenta1 = Cuenta( 300 )
	print (cuenta1)
	cuenta1.depositar( 400 )
	print (cuenta1)

	print ( "\n\n\t *********La Cuenta de Ahorro" )
	cuenta2 = CuentaAhorro( 200, 0.2 )
	print (cuenta2) 
	cuenta2.depositar( 8000 )
	print (cuenta2)

	print ( "\n\n\t *********La cuenta de Credito" )
	cuenta3 = CuentaCredito( 200, 100 )
	print (cuenta3) 
	cuenta3.depositar( 8000 )
	print (cuenta3)
	cuenta3.retirar(8250)
	print (cuenta3)
	cuenta3.retirar(150)
	print (cuenta3)
