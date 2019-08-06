#Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, 
#y no le permita continuar hasta que la haya ingresado correctamente.

contrasena = "contra"
while True:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")




