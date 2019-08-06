# -*- coding: utf-8 -*-

# Autor: Armando Ruiz
# Bucle for en Python
# Verificación de correo electronico

valido = False
email = input('Introduce tu correo: ')

for i in range(len(email)):
    if email[i] == '@':
        valido = True

if valido:
    print ('Correo valido!')
else:
    print ('Correo no valido!')