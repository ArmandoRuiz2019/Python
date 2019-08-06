from cuenta import Cuenta

class Persona(object):
    def __init__(self,nombre,apellido,cantidad,numCuenta):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuenta = Cuenta(numCuenta,cantidad)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido

    def hacerIngreso(self, cantidad):
        self.__cuenta.ingresarDinero(cantidad)

    def retirarDinero(self, cantidad):
        self.__cuenta.sacarDinero(cantidad)

    def getSaldo(self):
        return self.__cuenta.getSaldo()

    def getNumeroCuenta(self):
        return self.__cuenta.getNumeroCuenta()