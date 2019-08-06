import sqlite3
import time
import os

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
resp = ""

def creartabla():
    try:
        cursor.execute("CREATE TABLE usuarios (nombre TEXT, edad NUMERIC, email TEXT , dni TEXT)")
        conexion.commit()
        cursor.close()
        conexion.close()
    except sqlite3.OperationalError as error:
		print("Error al abrir:", error) 

def insertar():
    cursor.execute("INSERT INTO usuarios VALUES ('Charlie', 25, 'charlie@ejemplo.com','10210902')")
    conexion.commit()

def  devolveregistro():
    cursor.execute("SELECT * FROM usuarios")
    usuario = cursor.fetchone()
    print usuario

def insertargrupo():
    usuarios = [('Maria', 23, 'maria@ejemplo.com','10210903'),
                ('Mercedes', 38, 'mercedes@ejemplo.com','10210904'),
                ('Juanita', 19, 'juanita@ejemplo.com','10210905')
                ]
    cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
    conexion.commit()

def listartodos():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print('Nombre: ' + usuario[0]  +  '  Edad:'  + str(usuario[1])  + '  Correo:' + usuario[2] + '  DNI:' + usuario[3]  )
    


def modificarregistro():
    cursor.execute("UPDATE usuarios SET nombre ='Charlie Sanchez', edad=26 WHERE dni='10210902'")
    conexion.commit()


def eliminar():
    cursor.execute("DELETE FROM usuarios  WHERE dni='10210902'")
    conexion.commit()

def menu():
    print ("Menu Opciones")    
    print ("1.-Crear Tabla")
    print ("2.-Insertar")
    print ("3.-Devolver Registro")
    print ("4.-Insertar Varios")
    print ("5.-Listar")
    print ("6.-Modificar")
    print ("7.-Eliminar")

    opc =raw_input("Ingrese Opcion==>")

    if opc=="1":
        creartabla()
    elif opc=="2":
        insertar()
    elif opc=="3":
        devolveregistro()  
    elif opc=="4":
        insertargrupo()
    elif opc=="5":
        listartodos()
    elif opc=="6":
        modificarregistro()
    elif opc=="7":
        eliminar()

while resp!='N':
    menu()   
    resp=raw_input("desea continuar:").upper()
    os.system('cls')
    time.sleep(3)

    