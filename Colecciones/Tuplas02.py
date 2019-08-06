# -*- coding: utf-8 -*-

# Autor: Armando Ruiz
# Tuplas en Python 

mi_tupla = (1,'Enmanuel')
print ('Mostrando un elemento de la tupla:',mi_tupla[1])
print ('Tupla:',mi_tupla)


# convierte una lista en tupla
# método list
mi_lista = list(mi_tupla)
print ('Tupla convertida en Lista:',mi_lista)

# convierte una tupla en lista
# método tuple
lista = [2,1992,2,'Alexander']
tupla = tuple(lista)
print ('Lista convertida en Tupla:',tupla)

# comprobar si hay elemento en la tupla
print ('Alexander' in tupla)

# para saber cuantos veces se encuentra un elemento en la tupla
# count
print ('Cuantas veces se encuentra un elemento en la tupla:',tupla.count(2))

# longitud de una tupla
# len
print ('Longitud de la tupla:',len(tupla))

# tuplas unitarias
tupla_unitaria = 'Luz',
print ('Tupla unitaria:',len(tupla_unitaria))

# desempaquetado de tupla
d_tupla = ('Enmanuel',4,4,1994)
nombre, dia, mes, ano = d_tupla
print ('\nDesempaquetado de tupla:')
print ('Nombre:',nombre)
print ('Dia:',dia)
print ('Mes:',mes)
print ('Año:',ano)