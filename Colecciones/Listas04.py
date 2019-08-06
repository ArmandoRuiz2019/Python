# -*- coding: utf-8 -*-

# Autor: Armando Ruiz
# Listas en Python

# creando una lista
print ('operaciones con listas')
print ('____________________________________________________________')
nombre_lista = ['Enmanuel','Alexander','Kevin','Zarine',4,1.94]
mi_lista = ['Luz','Ana Isabel']
print ('Lista:',nombre_lista)

# acceder a un elemento especifico de la lista
print ('Accediendo a un elemento de la lista:',nombre_lista[0])

# acceder a una porción de la lista
print ('Muestra el rango de los elemento de la lista:',nombre_lista[0:2])

# acceder a los dos ultimos elementos de la lista
print ('Accediendo a los ultimos elemento de la lista:',nombre_lista[2:])

# agregar elementos a una lista
# append lo agrega al final de la lista
nombre_lista.append('Indiana')
print ('Agregando un elemento a la lista:',nombre_lista)

# agregar elementos a una lista
# insert lo agrega en cualquier parte de la lista dependiendo del parametro
nombre_lista.insert(0,'Ozzie')
print ('Insertando un elemento a la lista:',nombre_lista)

# agregar varios elementos a una lista
# extend
nombre_lista.extend(['Neritza','Nereida'])
print ('Agregando varios elemento a la lista:',nombre_lista)

# para saber el indice de un elemento de la lista
# index
print ('Muestra el indice de un elemento de la lista:',nombre_lista.index('Kevin'))

# comprobar si un elemento esta en la lista
print ('Comprueba si el elemento esta en la lista:','Enmanuel' in nombre_lista)

# eliminar un elemento de la lista
nombre_lista.remove('Ozzie')
print ('Eliminar un elemento de la lista:',nombre_lista)

# eliminar el ultimo elemento de la lista
nombre_lista.pop()
print ('Eliminar el ultimo elemento de la lista:',nombre_lista)

# sumando nombre_lista + mi_lista
lista = nombre_lista+mi_lista
print ('Sumando listas:',lista)

# multiplicar una lista
print ('Multiplicando la lista:',mi_lista * 3)