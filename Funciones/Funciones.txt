Este mini proyecto te permitirá practicar un poco con funciones, listas, y la traducción de formulas matemáticas a sentencias de programación.

A fin de usar las notas en nuestro programa, necesitaremos que estén incluidas en un contenedor, específicamente una lista.

La rutina presenta los siguientes resultados a partir de una entrada de calificaciones:

Imprime lo siguiente:

el total de calificaciones
suma de las calificaciones
calificación promedio
varianza
desviación estándar

'''

calificaciones = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_calificaciones(calificaciones):
    #Imprime la lista de calificaciones
    for calificacion in calificaciones:
        print calificacion

def calificaciones_sum(lista):
    #Suma la calificaciones
    suma = 0.0
    for i in lista:
        suma += i
        
    return suma
    
def calificaciones_promedio(lista):
    #Calcula el promedio de las calificaciones
    suma = calificaciones_sum(lista)
    return suma / len(lista)
    

def calificaciones_varianza(lista, promedio):
    #Obtiene la valiranza
    n = len(lista)
    s2 = 0
    
    for i in lista:
        s2 += (i - promedio) ** 2
    s2 = s2 / n
    
    return s2
    

def calificaciones_std_deviacion(varianza):
    #Calcula la desviación estándar
    s = varianza ** (0.5)
    return s

#print calificaciones No se pide, pero sino se imprime no nos deja pasar de módulo.
print calificaciones   
print print_calificaciones(calificaciones)
print calificaciones_sum(calificaciones)
print calificaciones_promedio(calificaciones)
print calificaciones_variaza(calificaciones, calificaciones_promedio(calificaciones))
print calificaciones_std_deviacion(calificaciones_varianza(calificaciones, calificaciones_promedio(calificaciones)))