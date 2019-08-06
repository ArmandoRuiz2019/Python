#Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

contrasena = "contra"
intentos = 3
while intentos:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -=1