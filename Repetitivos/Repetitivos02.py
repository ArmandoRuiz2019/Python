import os
nom=""
resp=""
ht=0
ph=37
sue=0
con=0
while resp!='N':
    nom=input("Ingrese su nombre:")
    ht=int(input("Ingrese las horas Trabajadas:"))
    sue=ht*ph
    con+=1
    print("El Pago ha Recibir es:"+str(sue))
    resp=input("desea continuar:")
    os.system('cls')
print("La Cantidad de personas evaluadas:"+str(con))  