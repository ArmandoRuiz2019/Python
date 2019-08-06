''' 
Created on Agosto, 2019
@author: Armando Ruiz
''' 

from cuenta import *

class CuentaCredito(Cuenta):
    """
        En esta versión de la clase se permite el retiro con una
        cantidad de protección(la cantidad de sobregiro)
    """
    def __init__( self, saldoInicial, mSobregiro ):
        Cuenta.__init__(self, saldoInicial)
        self.montoSobregiro = mSobregiro

    """
    Este método se sobreescribe
    """
    def __str__( self ):
        msg = Cuenta.__str__(self)
        msg += ":Monto de Sobregiro:" + str( self.montoSobregiro )
        return msg

    """
    Este método se sobreescribe
    """
    def retirar( self, valor ):
        result = True
        
        if self.cantidad < valor:

            # Not enough balance to cover the amount 
            # requested to withdraw
            # Check if there is enough in the overdraft 
            # protection (if any)
            sobregiroNecesario = valor - self.cantidad

            if ( self.montoSobregiro < sobregiroNecesario ):
                #No overdraft protection or not enough to cover 
                #the amount needed
                print("No se pudo retirar")
                result = False
            else:
                #Yes, there is overdraft protection and enough 
                #to cover the amount
                self.cantidad = 0.0
                self.montoSobregiro -= sobregiroNecesario

        else:     
            #Yes, there is enough balance to cover the amount
            #Proceed as usual
            self.cantidad = self.cantidad - valor
        
        return result