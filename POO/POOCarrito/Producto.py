#Por Tania Cárdenas
#Mayo de 2019
#Versión 5

#Esta clase es el cimiento del programa, permite reconocer el nombre del artículo, su precio, además de facilitar a los clientes su código de barras, marca y número de piezas disponibles para que puedan elegir de manera sencilla entre las opciones que ofrece nuestro establecimiento.


class Producto:

  #Constructor
  def __init__ (self, nombre, valor, piezas):
    self.nombre = nombre
    self.precio = valor
    self.piezas = piezas

  #Sobreescribimos el Método mostrarDetalles 
  def __str__(self):
  
    cadena = "\nTipo de producto: " + str(self.nombre)
    cadena += "\nPrecio del producto: " + str(self.precio)
    cadena +="\nPiezas disponibles: " + str(self.piezas) 
    return cadena 