class Cuenta(object):

    def __init__(self,numeroCuenta,cantidad):
        self.__numCuenta=numeroCuenta
        self.__saldo = cantidad

    def sacarDinero(self, cantidad):
        self.__saldo -= cantidad

    def ingresarDinero(self, cantidad):
        self.__saldo += cantidad

    def getSaldo(self):
        return self.__saldo

    def getNumeroCuenta(self):
        return self.__numCuenta