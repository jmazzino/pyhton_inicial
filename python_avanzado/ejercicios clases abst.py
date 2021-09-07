from abc import ABC,abstractmethod
from math import pi, sqrt

class Figura (ABC):
    
    @abstractmethod
    def dibujar (self):
        pass

    @abstractmethod    
    def calcular_area (self):
        pass
    
class Triangulo (Figura):
    def __init__(self,base,altura):
        self.lados=3
        self.base=base
        self.altura=altura
    
    def dibujar (self):
        dibu = "▲"
        return dibu
            
    def calcular_area (self):
        return self.base * self.altura / 2

class Cuadrado (Figura):
    def __init__(self,lado):
        self.lados=4
        self.lado=lado
    
    def dibujar (self):
        dibu = "⊠"
        return dibu
            
    def calcular_area (self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def dibujar(self):
        dibu = "⚫"
        return dibu
    
    def calcular_area(self):
        return pi * self.radio ** 2 

class Pizarra ():
    def __init__(self):
        return

    def agregar(self, cuadrado, triangulo, circulo):
        self.cuadrado = cuadrado
        self.triangulo = triangulo
        self.circulo = circulo
        figuras = [self.cuadrado, self.triangulo, self.circulo]
        return figuras
            
    def dibujar(self,figuras):
        for i in figuras:
          print("########################")
          print(i.dibujar())
          print(i.calcular_area())
          print("########################") 
        
if __name__ == '__main__':
    triangulo= Triangulo(5,8)
    cuadrado= Cuadrado(5)
    circulo= Circulo(45)
    pizarra=Pizarra()
    
    print(pizarra.dibujar(pizarra.agregar(cuadrado, triangulo, circulo)))