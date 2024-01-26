class TanqueDeCombustible:
    def _init_(self):
        self.combustible = 100

        def agregar_combustible(self, cantidad):
            self.combustible += cantidad

        def obtener_combustible(self):
            return self.combustible

        def usar_combustible (self,cantidad):
            self.combustible -= cantidad

class Auto():
    def _init_(self,tanque):
        s.posicion = 0
        self.tanque = tanque

def mover (self,distancia):
    if self.tanque.obtener_combustible()>= distancia / 2:
       self.posicion += distancia
       self.tanque.usar_combustible(distancia / 2)
       print("Has movido el auto exitosamente")
    else
    print("No hay suficiente combustible")

    def obtener_posición(self):
        return self.posicion


tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posición())
print(autito.mover(10))
print(autito.obtener_posición())
print(autito.mover(20))
print(autito.obtener_posición())
print(autito.mover(60))
print(autito.obtener_posición())
print(autito.mover(100))
print(autito.obtener_posición())
print(autito.mover(100))
print(autito.obtener_posición())