class Persona:
    delf_init_(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

    class Artista:
        def_init_(self,habilidad):
            self.habilidad

        def mostrar_habilidad(self):
             print(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Persona,Artista):
    def_init_(self,nombre,edad,nacionalidad,habilidad,empresa,salario):
        Persona._init_(self.nombre,edad,nacionalidad)
        Artista._init_(self,habilidad)
        self.salario = salario
        self.empresa = empresa

       
        def presentarse(self):
            print(f'Hola, soy:{self.nombre},{super().mostrar_habilidad()} y trabajo en {self.empresa}')

    

        roberto = Artista ("Cantar")


Herencia = issubclass(EmpleadoArtista,Persona)
Instancia = isinstance(Roberto,Artista)

Print(instancia)