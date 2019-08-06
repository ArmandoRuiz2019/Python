cursos = ['Java', 'C++', 'Python', 'Vbasic']
cursos.append('Excel')    
encontro=0
loncur=len(cursos)
indice=int(input("Ingrese el Curso a Listar:"))
for i in range(0,5):
      if indice == i:
        encontro = 1
        print(cursos[i])
if encontro == 0:
    print("No se encontro el curso")

 