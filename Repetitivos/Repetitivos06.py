from time import sleep
contrasena = "contra"
maxIntentos = 5
intentos = maxIntentos
while intentos != 0:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -=1
        if intentos > 0:
            sleep(10-int(10/maxIntentos*intentos))