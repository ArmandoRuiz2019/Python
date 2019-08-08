class Productos:

    #Constructor
    def __init__ (self, cod,nom, pre, sto):
      self.codigo = cod
      self.nombre = nom
      self.precio = pre
      self.stock = sto
  
    #Sobreescribimos el Método mostrarDetalles 
    def __str__(self):
      cadena = "\nCodigo producto: " + str(self.codigo)
      cadena = "\nProducto: " + str(self.nombre)
      cadena += "\nPrecio del producto: " + str(self.precio)
      cadena +="\nStock disponible: " + str(self.stock) 
      return cadena 


        
        
        
