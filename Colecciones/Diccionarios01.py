""" Recorrido por diccinarios
  Armando Ruiz
"""
#Definimos nuestro diccionario
Armando = {
    "nombre":"Armando",
    "tareas": [90, 97, 75, 92],
    "pruebas": [88, 40, 94],
    "examenes": [75, 90]
    }
Sebas = {
    "nombre":"Sebas",
    "tareas": [100,92,98,100],
    "pruebas": [82,83,91],
    "examenes": [89,97]
    }
Daniel = {
    "nombre":"Daniel",
    "tareas": [0,87,75,22],
    "pruebas": [0,75,78],
    "examenes": [100,100]
    }

#Definimos un índice para mostrar los elementos del diccionario
indice = 0

#Creamos una lista a partir de nuestro diccionario
estudiantes = [Armando, Sebas, Daniel]

#Hacemos el recorrido de nuestra lista mostrando cada elemento de forma individual
for alumno in estudiantes:
    print (estudiantes[indice]["nombre"])
    print ("Tareas : ", estudiantes[indice]["tareas"])
    print ("Pruebas : ", estudiantes[indice]["pruebas"])
    print (u"Exámenes : ", estudiantes[indice]["examenes"])
    #Debemos usar un índice para tener acceso a los elementos de la lista
    indice += 1