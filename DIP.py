#class Diccionario:
    #def verificar_palabra(self, palabra):
       # Lógica para verificar palabras  
        #pass

#class CorrectorOrtográfico:
 #   def __init__(self):
  #      self.diccionario = Diccionario()

#    def corregir_texto(self.texto):
 #       usamos el diccionario para corregir el texto
  #      pass


  from abc import ABC, abstractmethod

  class VerificadorOrtográfico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
 #Lógica para verificar palabras si están en el diccionario
 pass

class CorrectorOrtográfico:
    def __init__(self, verificador):
    self..verificador = verificador

    def corregir_texto(self, texto)
    #  usamos el verificador para corregir el texto


    corrector = CorrectorOrtográfico(Diccionario())