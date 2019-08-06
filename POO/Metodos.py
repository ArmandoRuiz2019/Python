class barbero:
      codigo = ''
      nombre = ''
      especialidad =''
      correo = ""
      turno = 0
      
      def __init__ (self, codigo, nombre, especialidad, correo,turno):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad
        self.correo = correo
        self.turno = turno
        print ("se ha creado el objeto")

      def mensajeturno(self):
          if self.turno>=8 and self.turno <12:
              msj="Trabaja de dia"
          elif self.turno>=12 and self.turno <=18:
              msj="Trabaja de tarde"
          else:
              msj="Trabaja de Noche"
          print ("El Barbero:" , self.nombre ,msj)

barbero1 = barbero("B1", "Armando", "Afeitado", "aruiz.eu.ruiz@gmail.com",9)
barbero1.mensajeturno()

barbero2 = barbero("B2", "Juanita", "Corte", "juanita.ruiz@gmail.com",10)
barbero2.mensajeturno()

barbero3 = barbero("B3", "Esteban", "Tinte", "esteban.ruiz@gmail.com",13)
barbero3.mensajeturno()

barbero4 = barbero("B4", "Oscar", "Corte", "oscar.ruiz@gmail.com",19)
barbero4.mensajeturno()




