cursos = ('Java', 'C++', 'Python', 'Vbasic')
encontro=0
loncur=len(cursos)
indice=int(raw_input("Ingrese el Curso a Listar:"))
for i in range(0,3):
      if indice == i:
        encontro = 1
        print(cursos[i])
if encontro == 0:
    print("No se encontro el curso")