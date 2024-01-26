class Persona:
    delf_init_(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

   class Empleado(Persona):
        delf_init_(self,nombre,edad,nacionalidad,trabajo,salario):
        super()._init_(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

     
    class Estudiante(Persona):
        delf_init_(self,nombre,edad,nacionalidad,notas,universidad):
        super()._init_(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

    




        roberto = Empleado("Roberto",43,"argentino","Cantar","Programador",100000)

    roberto.hablar()