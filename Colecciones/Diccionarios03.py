
dicci={1:'AREQUIPA',2:'CUZCO',3:'CAJAMARCA',4:'PUNO',5:'HUARAL',6:'ICA',7:'LIMA',8:'LA LIBERTAD',9:'AYACHUCHO',10:'TARMA'}
res='SI'
while res=='SI':    
    n=input('ingresa un valor de 1 a 10: ')
    if int(n) in range(1,11):
           print(dicci[int(n)])
    else:
        print('fuera de rango')
    res=input('seguir <si - no> ').upper()