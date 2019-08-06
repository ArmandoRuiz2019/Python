igv = 0.18
precio = int(input("ingresar el precio:"))
cantidad = int(input("ingresar la cantidad:"))
tot = precio * cantidad
imp = tot * igv
neto = tot + imp
input("El total a pagar Es: "+ str(neto) )
