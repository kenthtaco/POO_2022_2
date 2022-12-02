
# HERENCIA EN PYTHON

class persona:
   nombre = str
   apellido = str
   
   def __init__(self, nombre, apellido):
       self.nombre = nombre
       self.apellido = apellido
       
   def imprimir(self):
        print(self.nombre, self.apellido)
        
x = persona("Alexander", "Flores")
x.imprimir()

# HERENCIA SIMPLE EN PYTHON

class estudiante(persona):
    pass

y = estudiante("Jeremy", "Cañizares")
y.imprimir()

# AGREGAR ATRIBUTOS A UNA HERENCIA

class student(persona):
    edad = int
    
    def __init__(self, nombre, apellido, edad):
        persona.__init__(self, nombre, apellido)
        self.edad = edad
        
estudiante1 = student("Carlos", "Dell", 30)
estudiante1.imprimir ()


# AGREGAR METODOS A UNA HERENCIA

class Student1(persona):
    edad = int
    semestre = str
    
    def __init__(self, nombre, edad, apellido, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad 
        self.semestre = semestre 
        
    def bienvenido(self):
        print("Bienvenido " + self.apellido + " al " + self.semestre + " ingresas a los " + str(self.edad) + "años")

p5 = Student1("Diego", "Yanez", 29, "Segundo")
p5.bienvenido()        

