# -*- coding: utf-8 -*-

# Autor: Armando Ruiz
# Diccionarios en Python

mi_diccionario = {'Venezuela':'Caracas','Alemania':'Berlin','Francia':'Paris'}
print (mi_diccionario['Venezuela'])
print (mi_diccionario)

# agregar un elemento al diccionario
mi_diccionario['Italia'] = 'Lisboa'
print (mi_diccionario)

# modificar un elemento del diccinario
mi_diccionario['Italia'] = 'Roma'
print (mi_diccionario)

# eliminar un elemento del diccionario
del mi_diccionario['Francia']
print (mi_diccionario)

tupla = ['Venezuela','España','Alemania']
diccionario = {tupla[0]:'Caracas',tupla[1]:'Madrid',tupla[2]:'Berlin'}
print (diccionario)

# acceder a un elemento del diccionario
print (diccionario[tupla[0]])
print (diccionario['Venezuela'])

# diccionario almacena una tupla
# diccionario dentro de un diccionario con una tupla
jugador = {'Nombre':'Michael','Apellido':'Jordan','Equipo':'Chicago','Anillos':{'Temporadas':[1991,1992,1993,1996,1997,1998]}}
print (jugador)
print (jugador['Equipo'])
print (jugador['Anillos'])

# métodos para los diccionarios
# método keys me devuelve todas las claves del diccionario
print (jugador.keys())

# método values me devuelve los valores del diccionario
print (jugador.values())

# método len me devuelve la longitud del diccionario
print (len(jugador))