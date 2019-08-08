class Carrito:

  #Constructor. Se inicializa con una lista vacía.
  def __init__(self):
    self.productos = []

  def agregar(self,productos):
    self.productos.append(productos) 
  

  def __str__(self):
    cadena =  str(len(self.productos))
    for producto in self.productos: 
      cadena += "\n" + str(producto) 
    return cadena 

  def cantidad(self):
    cadena =  str(len(self.productos))
    return cadena
        

  
