''' 
Created on Agosto,20189
@author: Armando Ruiz
''' 
class Productos:
    def __init__( self, pro, labo, far, pre , stk ,tip , cod):
        self.producto = pro
        self.laboratorio = labo
        self.farmacia = far
        self.precio = pre
        self.stock = stk
        self.tipo = tip
        self.codigo = cod

    def imprimirDetalles( self ):
        print("Imprimiendo desde el Metodo")
        print("Producto:", self.producto)
        print("Laboratorio:", self.laboratorio)
        print("Farmacia:", self.farmacia)
        print("Precio:", self.precio)
        print("Stock:", self.stock)
        print("Tipo:", self.tipo)
        print("Codigo:", self.codigo)

    def comprobarstock( self,valor ):
        if int(valor) > int(self.stock):
            print ( "El valor no puede ser mayor al Stock:")
        else:
            self.stock = int(self.stock) - int(valor)
            print ( "Compra Realizada con exito el Stock Actual es:",self.stock)
    
    

		
	

