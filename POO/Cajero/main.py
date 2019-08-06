from persona import Persona
import os

numCuentas = 2
clientes = []
opcion = 0

persona0 = Persona('Javier', 'Ceballos', 0.0, 0)
persona1 = Persona('Maria', 'Gutierrez', 0.0, 1)
clientes.append(persona0)
clientes.append(persona1)

while ('6' != opcion):
    opcion = input('''Por favor seleccione una operacion:
    1 Ver cuentas
    2 Crear cuenta
    3 Ver saldo
    4 Hacer ingreso
    5 Hacer retirada
    6 Exit
    ''')

    if opcion == '1':

        for cliente in clientes:
            print('Nombre: ' + cliente.getNombre())
            print('Apellido: ' + cliente.getApellido())
            print('Numero de Cuenta: ' + str(cliente.getNumeroCuenta()))
            print('\n')
        input("Pulse Enter para continuar...")
    elif opcion == '2':
        nombre = input('Introduzca nombre: ')
        apellido = input('Introduzca apellido: ')

        persona = Persona(nombre, apellido, 0.0, numCuentas)
        numCuentas += 1
        clientes.append(persona)
        print("Cuenta creada")
        input("Pulse Enter para continuar...")
        os.system('cls')
    elif opcion == '3':
        cuenta = input('Por favor indique el numero de cuenta:')
        print('El saldo de la cuenta ' +cuenta+' es de: '+str(clientes[int(cuenta)].getSaldo())+' Soles')
        input("Pulse Enter para continuar...")
        os.system('cls')
    elif opcion == '4':
        cuenta = input('Por favor indique el numero de cuenta al que desea hacer el ingreso:')
        cantidad = input('Por favor indique la cantidad a ingresar:')
        clientes[int(cuenta)].hacerIngreso(int(cantidad))
        print('Se ha realizado el ingreso')
        input("Pulse Enter para continuar...")
        os.system('cls')
    elif opcion == '5':
        cuenta = input('Por favor indique el numero de cuenta al que desea hacer el ingreso:')
        cantidad = input('Por favor indique la cantidad a retirar:')
        clientes[int(cuenta)].retirarDinero(int(cantidad))
        print('Se ha realizado la retirada')
        input("Pulse Enter para continuar...")
        os.system('cls')

print('Fin del programa')