'''
 Rutinas matemáticas básicas: Colección de pequeñas utillerías en Python
 Para Python 3.0 y superior
 Colección de rutinas simples para algunas actividades cotidianas que requieren  desiciones a partir de un número dado.
 A continuaciòn se presenta el contienido de rutinas:
 
** es_par(num)
Toma un número (num) y determina si es par devolviendo True, en otro caso devuelve False

** es_entero(num)
Toma un número x como entrada y devuelva la respuesta booleana True si el número es entero (en la vida real)
y False si no lo es. Nota: Un número entero se define como un número que no tiene parte fraccionaria. Los números 
negativos sin partes fraccionarias también se consideran enteros. de este modo 
es_entero(7.00) # Verdadero
es_entero(7.5)   # Falso
es_entero(-1)     # Verdadero  

** suma_de_digitos(num)
suma_de_digitos que toma como entrada un entero positivo n y devuelva la suma de todos los dígitos de ese número.
Por ejemplo: suma_de_digitos(1234) debería devolver 10 que corresponde a 1 + 2 + 3 + 4.

** factorial(num)
Toma como entrada un entero x y devuelva el factorial de ese número.

** es_primo(num)
es_primo toma un número x como entrada y devuelva el booleano True si x es primo y False si no lo es.

** purificar (lista)
purificar toma una lista de números, quita todos los impares de la lista, y devuelva el resultado.
Por ejemplo, purificar([1,2,3]) devuelve [2].

** producto(lista):
producto toma como entrada una lista de enteros y devuelva el producto de todos los elementos de la lista.
Por ejemplo: producto([4, 5, 5]) devuelve 100.
Restricciones:
> No considera si la lista está vacía. 
> La función devuelve un entero.

** quitar_repetidos(lista)
quitar_repetidos toma una lista de números y quita los elementos de la lista que son iguales.
Por ejemplo: quitar_repetidos([1,1,2,2])  devuelve [1,2].
Restricciones:
> conserva una ocurrencia del número.
> No considera el orden de la lista

** mediana(lista)
mediana toma como entrada una lista y devuelva el valor de la mediana de esa lista.
Por ejemplo: mediana([1,1,2]) devuelve 1.
> La lista puede ser de cualquier tamaño y los números no tienen que estar en un orden en particular.


'''

# *********************************************************************************************
#Toma un número (num) y determina si es par devolviendo True, en otro caso devuelve False
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Argumento de validación        
print es_par(0)

# *********************************************************************************************
'''suma_de_digitos que toma como entrada un entero positivo n y devuelva la suma de todos los dígitos de ese número.
Por ejemplo: suma_de_digitos(1234) debería devolver 10 que corresponde a 1 + 2 + 3 + 4. '''
def es_entero(num):
    if round(num) != num:
        return False
    else:
        return True
        
#Argumento de validación  
print es_entero(5.2)
# *********************************************************************************************

def suma_de_digitos(num):
    strnum = str(num)
    suma = 0
    for x in strnum:
        xnum = int(x)
        suma += xnum
    return suma
        
#Argumento de validación          
print suma_de_digitos(7894)

# *********************************************************************************************
#Toma como entrada un entero x y devuelva el factorial de ese número.
def factorial(num):
    total = 1
    x = 1
    while x <= num:
        total *= x
        x += 1
    return total
    
#Argumento de validación    
print factorial(8)

# *********************************************************************************************
#es_primo toma un número x como entrada y devuelva el booleano True si x es primo y False si no lo es.
def es_primo(num):
    flag = []
    esprimo = True
    temp = False
    peso = 0
    limite = num
    
    while esprimo:
        if num < 2:
            return False
            break
        elif num == 2:
            return True
            break
        else:

            for i in range(num):
                i += 1
                if (num % i) != 0:
                    flag.append(False)
                else: 
                    flag.append(True)
            #print flag  #Señalizador para depurar
            
        for index in flag:
           if index == True:
               peso += 1
        
        if peso == 2:
            return True
        else:
            return False
           
        #Después de las pasadas lo hacemos falso para terminar el bucle
        esprimo = False 
           
#Argumento de validación
print es_primo(811)

# *********************************************************************************************

'''
purificar toma una lista de números, quita todos los impares de la lista, y devuelva el resultado.
Por ejemplo, purificar([1,2,3]) devuelve [2].
'''
numeros = (1, 2, 4,5,6,7,8,9,10,20,33,44,55,66,77,88,99,100 )

def purificar (lista):
    indice = 0
    newlista = []
    for i in lista:
        if (lista[indice] % 2) == 0:
            newlista.append(lista[indice])
        indice += 1
    return newlista
    
    
print purificar(numeros)

# *********************************************************************************************
'''
producto toma como entrada una lista de enteros y devuelva el producto de todos los elementos de la lista.
Por ejemplo: producto([4, 5, 5]) devuelve 100.
Restricciones:
> No considera si la lista está vacía. 
> La función devuelve un entero.
'''
numeros = [2,3,4,5,6,7,8,9,10]

def producto(lista):
    total = 1
    for index in lista:
        total *= index
    return total
    
print producto(numeros)

# *********************************************************************************************

'''
quitar_repetidos toma una lista de números y quita los elementos de la lista que son iguales.
Por ejemplo: quitar_repetidos([1,1,2,2])  devuelve [1,2].
Restricciones:
> conserva una ocurrencia del número.
> No considera el orden de la lista
'''
numeros = [1,5,8,4,2,3,6,5,1,2,8,5,3,6,4,1,2]

def quitar_repetidos(lista):
    tamanio = len(lista)
    newlista = []
    indice = 0
    actualvalue = 0
    while indice < tamanio:
        actualvalue = (lista[indice])
        
        if not(actualvalue in newlista):
            newlista.append(actualvalue)
        
        indice += 1
    
    lista.sort()
    return newlista
    

print quitar_repetidos(numeros)

# *********************************************************************************************

'''
mediana toma como entrada una lista y devuelva el valor de la mediana de esa lista.
Por ejemplo: mediana([1,1,2]) devuelve 1.
> La lista puede ser de cualquier tamaño y los números no tienen que estar en un orden en particular.
'''
valores = [4,5,5,4]

valores.sort()
print "ordenada", valores

def mediana(lista):
    lista.sort()
    suma = 0.0
    promedio = 0.0
    tamanioLista = len(lista)
    #Para contabilizar índice se empieza en 0
    indice = (tamanioLista // 2)
    if (tamanioLista % 2) != 0:
        return lista[indice]
    else:
        #Sino convertimos a float, la división será entera
        suma = float(lista[indice-1] + lista[indice])
        
        promedio = suma / 2
        return promedio
    
print mediana(valores)

# *********************************************************************************************
# *********************************************************************************************
# *********************************************************************************************
# *********************************************************************************************
# *********************************************************************************************
# *********************************************************************************************