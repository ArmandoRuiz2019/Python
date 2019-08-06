class barbero(object):
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
