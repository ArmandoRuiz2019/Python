# -*- coding: utf-8 -*-

# Autor: Armando Ruiz
# Programa que muestra los datos invertidos de atras hacia delante

maximo = int(input('Ingrese la cantidad de números: '))

numero = [0 for x in range(maximo)]
for i in range(0,len(numero)):
    numero[i] = int(input("Dime el dato número {}: ".format(i+1)))

print ("\nLos datos al reves son: ")
for i in range(len(numero),0,-1):
    print (numero[i-1])