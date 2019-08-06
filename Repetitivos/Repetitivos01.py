#for i in range(0,10):
# print(i)

# edad = 0
# while edad < 18:
# edad = edad + 1
# print ("Felicidades, tienes ") + str(edad)


# secuencia = ["uno", "dos", "tres"]
# for elemento in secuencia:
#  print elemento 

# while True:
# entrada = raw_input("> ")
# if entrada == "adios":
#    break
# else:
#    print (entrada)

edad = 0
while edad < 18:
    edad = edad + 1
    if (edad % 2) == 0:
        continue
    print ("Felicidades, tienes " + str(edad))