Class A:
      Def hablar (self):
      Print(“Hola desde A”)

Class F:
      Def hablar (self):
      Print(“Hola desde F”)


Class B(A):
      Def hablar (self):
      Print(“Hola desde B”)


Class C(F):
      Def hablar (self):
      Print(“Hola desde C”)


Class D(B,C):
      Def hablar (self):
      Print(“Hola desde D”)


d = D()

F.hablar(d)