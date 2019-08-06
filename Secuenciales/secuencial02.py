igv = 0.18
precio = int(raw_input("ingresar el precio:"))
cantidad = int(raw_input("ingresar la cantidad:"))
tot = precio * cantidad
imp = tot * igv
neto = tot + imp
raw_input("El total a pagar Es: "+ str(neto) )
