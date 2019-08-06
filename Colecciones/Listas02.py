# -*- coding: 850 -*-
cursos = {1:"java",2:"c++",3:"python"}
#cursos = "java","c++","python"
#cursos = ["java","c++","python"]
cantcursos = 0
cantcursos =len(cursos)
flag_encontrado = "0"
nomcurso = ""
resp = "S"
opc = 0
while resp != "N":
    print ("menu de opciones")
    print ("1.- Buscar Curso")
    print ("2.- Insertar Curso")
    print ("3.- Listar Cursos")
    opc = int(raw_input(" Seleccione Opcion "))
    if opc == 1 :
        valor = int(raw_input("ingrese curso a buscar:"))
        for i in  cursos:
            if valor == i :
                flag_encontrado = "1"
                nomcurso =cursos[i]
                break
            else :
                flag_encontrado = "0"
        if flag_encontrado == "1":
            print (nomcurso)
        else:
            print ("Curso no existe")
    elif opc == 2:
         print ("aca debe ir el proceso de insertar")   
    elif opc == 3:
         print ("aca debe ir el proceso de listar")       
    else :
        print ("Opcion no existe")
    resp = raw_input("Desea Continuar:").upper
