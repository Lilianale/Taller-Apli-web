class Celular:
def_init_(self,marca,modelo,camara):
self.marca = marca
self.modelo = modelo
self.camara = camara

def llamar(self):
print(f'Estas haciendo un llamado desde un:{self.modelo}')

def cortarr(self):
print(f'Cortaste la llamada desde tu:{self.modelo}')

celular1 = celular ("Samsung,S23,48MP")
celular = celular ("aPPLE,Iphone 15 pro,96MP")

celular2.llamar()