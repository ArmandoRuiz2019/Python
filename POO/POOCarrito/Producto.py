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