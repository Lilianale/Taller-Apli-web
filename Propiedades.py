class Persona:
    def_init_(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

@property
   def nombre(self):
     return self._nombre

@nombre.setter
    def nombre(self,new_nombre):
     self.__nombre = new_nombre

@nombre.deleter
def nombre(self):
    del self.__nombre

dalto = Persona("Lucas",21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

del dalto.nombre

print("que haces maquinola, suscribete")
