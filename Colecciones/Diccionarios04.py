import os
resp=""
opc=""
espec ={}
citas ={}
con=0
def agregar_especialidades():
   nesp=input("Ingresar especialidad:")
   costo=float(input("Ingresar costo:"))
   espec.update({nesp:costo})
   print("Listando Especialidades ")
   for key, value in espec.items():
       print('%s .- %s' % (key, value))
def agregar_citas():
   nesp=input("Especialidad:")
   pac=input("Paciente:")
   fec=input("Fecha de la Cita:")
   con =len(citas)
   citas.update({"Num_Exp."+str(con):str(con),"OtrosDatos"+str(con):[nesp,pac,fec]})
   print("Listando Citas ")
   for key, value in citas.items():
       print('%s .- %s' % (key, value))
def menuprincipal():
   menu ={"1":"Registrar Citas","2":"Registrar Especialidad","3":"Indicadores","4":"Registrar Pacientes"}
   for key, value in menu.items():
       print('%s ==> %s' % (key, value))
   opc = input("Elija Opcion Valida==>")
   if opc == "1":
       agregar_citas()
   elif opc=="2":
       agregar_especialidades()
   elif opc=="3":
       print("Indicadores")
while resp!="N":
    menuprincipal()
    resp=input("Desea Continuar(s/n):")
    os.system('cls')