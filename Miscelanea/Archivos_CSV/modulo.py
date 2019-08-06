#!/usr/bin/python3
#
import csv

def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si lo es y devuelve una cadena si no."""
    # Intenta convertir la cadena a número, y si se puede, devuelve el número
    try:
        i = int(i)
        return i
    #Si no se puede, nos dice que no se puede
    except ValueError:
        return "No je pue"

class Biblioteca: # Esta es la clase bibliotecas, cuyos métodos permiten gestionarla
    
    campos = ["Título", "Autor", "Editorial"] # Campos que tendrá cada libro
    libros = []

    def __init__(self):
        with open('biblioteca.csv', newline='') as f:
            reader = csv.reader(f)
            self.libros = list(reader)
    
    def agrega_libro(self, *campos):
        """Añade el libro a la biblioteca."""
        self.libros.append(list(campos)) # Añadimos el libro a la colección
    
    def borra_libro(self, libro):
        """Borra un libro de la biblioteca"""
        self.libros.pop(libro)
    
    def edita_libro(self, libro, campo, valor):
        """Edita un campo de uno de los libros de la biblioteca"""
        self.libros[libro][campo] = valor
    
    def guarda(self):
        """Guarda la biblioteca actual en el csv."""
        with open('biblioteca.csv', 'w', newline='') as f: # Abre el archivo csv como el objeto f
            writer = csv.writer(f) # Llama al método que escribe en ese archivo
            writer.writerows(self.libros) # Escribe los libros en el CSV por filas

