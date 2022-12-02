from padre import persona

class Docente(persona):
    titulo                 = str
    edad                   = int
    experienciaProfesional = int
    experienciaDocente     = int
    
    def __init__(self, nombre, apellido, titulo, edad, experienciaProfesional, experienciaDocente):
        super().__init__(nombre, apellido)
        self.titulo                 = titulo
        self.edad                   = edad
        self.experienciaProfesional = experienciaProfesional
        self.experienciaDocente     = experienciaDocente
        
        def BienvenidaDocente(self):
            print("Estimado Docente: " + self.nombre, self.apellido + ". Le damos la bienvenida al INT YAVIRAC " + 
                  "agradecemos contar con sus " + str(self.experienciaDocente + self.experienciaProfesional) + " años de experiencia ")
            
        docente1 = Docente("Dayana", "Tafur", "Desarrollador de software", 24, 2, 1)
        docente1.BienvenidaDocente()    