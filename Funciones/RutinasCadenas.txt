'''
 Rutinas con cadenas: Colección de pequeñas utillerías en Python
 Para Python 3.0 y superior
 Colección de rutinas de texto, permiten el tratamiento de cadenas de texto en diversas circunstancias tal como se describe a continuación:
 
** reverse(texto)
reverse tome como entrada el string texto y lo devuelva en sentido inverso. Por ejemplo: reverse("abcd") devuelve "dcba".

** anti_vocal(texto)
anti_vocal toma como entrada un string texto y devuelva el texto sin las vocales.
Por ejemplo: anti_vocal("¡Hola tu!") devuelve "¡Hl t!".

** puntaje_scrabble(texto)
puntaje_scrabble toma como entrada un string palabra y devuelva el puntaje de scrabble para esa palabra.
Restricciones: 
> Como entrada solamente recibire una palabra sin espacios ni puntuación.
> Aquí no incluimos multiplicadores de puntaje.
> Funciona aunque las palabras contengan mayúsculas.
> Suponemos que solamente recibe strings no vacíos.

** censor (texto, palabra)
censor toma como entrada dos strings texto y palabra y devuelva el texto con la palabra reemplazada por asteriscos.
Por ejemplo: censor("this hack is wack hack", "hack") devuelve "this **** is wack ****"
Restricciones: 
> Los strings no aceptan puntuación ni mayúsculas.

** contar(secuencia, item)
contar toma como entrada una lista secuencia y un valor item y devuelva el número de veces que aparece el elemento (item) en la lista.
Por ejemplo: contar([1,2,1,1],1) devuelve-->  devolver 3
Restricciones: > Hay un método para listas en Python para esto, pero se presenta una forma larga para practicar.
>La función devuelve un entero.
> El elemento que ingreses puede ser un entero, string, float, o incluso otra lista.


'''

# *********************************************************************************************
#reverse tome como entrada el string texto y lo devuelva en sentido inverso. Por ejemplo: reverse("abcd") devuelve "dcba".
def reverse(texto):
    actual = ""
    indice = 1
    longitud = len(texto)
    while indice <= longitud:
        actual = actual + texto[-indice]
        indice = indice + 1 
    return actual
        
print reverse("carlos")

# *********************************************************************************************

#anti_vocal toma como entrada un string texto y devuelva el texto sin las vocales.
Por ejemplo: anti_vocal("¡Hola tu!") devuelve "¡Hl t!".

def anti_vocal(texto):
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    
    cadena = ""
    for i in texto:
        if i in vocales:
            cadena += ""
        else:
            cadena +=  i
    
    return cadena
    
print anti_vocal("Paulina")


# *********************************************************************************************

'''puntaje_scrabble toma como entrada un string palabra y devuelva el puntaje de scrabble para esa palabra.
Restricciones: 
> Como entrada solamente recibire una palabra sin espacios ni puntuación.
> Aquí no incluimos multiplicadores de puntaje.
> Funciona aunque las palabras contengan mayúsculas.
> Suponemos que solamente recibe strings no vacíos.
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10} 
         
def puntaje_scrabble(texto):
    #Garantiza que todas las cadenas sean en minùsculas
    texto = texto.lower()
    suma = 0
    for i in texto:
        if i in score:
            suma = suma + score[i]
    return suma
        
print puntaje_scrabble("Paulina")

# *********************************************************************************************

'''
censor toma como entrada dos strings texto y palabra y devuelva el texto con la palabra reemplazada por asteriscos.
Por ejemplo: censor("this hack is wack hack", "hack") devuelve "this **** is wack ****"
Restricciones: 
> Los strings no aceptan puntuación ni mayúsculas.
'''
def censor (texto, palabra):
    if palabra in texto:
        mask = ""
        for i in palabra:
            mask += "*"
                
    return texto.replace(palabra, mask)    
        
print censor("hola paulina hermosa","paulina")

# *********************************************************************************************

'''
contar toma como entrada una lista secuencia y un valor item y devuelva el número de veces que aparece el elemento (item) en la lista.
Por ejemplo: contar([1,2,1,1],1) devuelve-->  devolver 3
Restricciones: > Hay un método para listas en Python para esto, pero se presenta una forma larga para practicar.
>La función devuelve un entero.
> El elemento que ingreses puede ser un entero, string, float, o incluso otra lista.
'''
lista = ([1,2,1,1],1)
 
def contar(secuencia, item):

    indice = 0
    contador = 0
    for i in secuencia:
        if item == secuencia[indice]:
            contador += 1            
        indice += 1 
        
    return contador


print contar(lista,1)

# *********************************************************************************************




# *********************************************************************************************