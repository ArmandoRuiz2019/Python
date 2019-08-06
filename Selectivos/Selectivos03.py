nom=""
sue=0
bon=0
nom=input("Ingrese su nombre:")
sue=int(input("Ingrese su sueldo:"))
tser=int(input("Tiempo de Servicio:"))
if tser>=1 and tser<=3:
    bon=sue*0.02
    #print("La Bonificacion de:"+ nom + "es:"+str(bon))
elif tser>=4 and tser<=5:     
    bon=sue*0.03
    #print("La Bonificacion de:"+ nom + "es:"+str(bon))
else:
    bon=sue*0.04
print("La Bonificacion de:"+ nom + "es:"+str(bon))
