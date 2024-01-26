from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def_init_(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad}años")

class Estudiante(Persona):
    def _init_(self,nombre,edad,sexo,actividad):
    super()._init_(nombre,edad,sexo,actividad)

     def hacer_actividad(self):
        print(f"Estoy estudiando:{self.actividad}")

class Trabajador(Persona):
    def _init_(self,nombre,edad,sexo,actividad):
    super()._init_(nombre,edad,sexo,actividad)

     def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de:{self.actividad}")


pedrito = Estudiante("Pedrito",25,"No Binario","programación")
dalto = Trabajador("Lucas",21,"Masculino","programación")

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()