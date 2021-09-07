"""
Patrones de diseño:
- Estructurales
- Creacionales
- De comportamiento
Abtract Factory, patron creacional.
Aborda la problematica de como crear objetos (todos los patrones creacionales hacen esto)
Se encarga del problema de tener familias de objetos, por ejemplo
tengo un sistema windows entonces todo el toolkit tiene ue ser que admita windows
Si vienen y me traen un sistema mac entonces tengo que traer el toolkit de mac
El problema es que si para cada ssitema operativo voy cambiando el sistema, es un problema.
https://refactoring.guru/es/design-patterns/abstract-factory
"""
from abc import ABC, abstractmethod

class Ciclista:
    def __init__(self, nombre, creadorBicis):
        self.__nombre = nombre
        self.__creadorBicis = creadorBicis

    def crearMountainBike(self):
         return self.__creadorBicis.crearMountainBike()
    def crearFixie(self):
         return self.__creadorBicis.crearFixie()

class CreadorBicis(ABC):
    @abstractmethod
    def crearMountainBike(self):
        pass
    @abstractmethod
    def crearFixie(self):
        pass

class Cannondale(CreadorBicis):
    def crearMountainBike(self):
        return MountainBikeCannondale()
    def crearFixie(self):
        return FixieCannondale()

class Specilized(CreadorBicis):
    def crearMountainBike(self):
        return MountainBikeSpecialized()
    def crearFixie(self):
        return FixieSpecialized()

class Fixie(ABC):
    @abstractmethod
    def frenar(self):
        pass
    @abstractmethod
    def avanzar(self):
        pass

class FixieSpecialized(Fixie):
    def frenar(self):
        return "Frene siendo Fixie Specialized"
    def avanzar(self):
        return "Avance siendo Fixie Specialized"

class FixieCannondale(Fixie):
    def frenar(self):
        return "Frene siendo Fixie Cannondale"
    def avanzar(self):
        return "Avance siendo Fixie Cannondale"

class MountainBike(ABC):
    @abstractmethod
    def frenar(self):
        pass
    @abstractmethod
    def avanzar(self):
        pass

class MountainBikeSpecialized(MountainBike):
    def frenar(self):
        return "Frene siendo MountainBike Specialized"
    def avanzar(self):
        return "Avance siendo MountainBike Specialized"

class MountainBikeCannondale(MountainBike):
    def frenar(self):
        return "Frene siendo MountainBike Cannondale"
    def avanzar(self):
        return "Avance siendo MountainBike Cannondale"

creadorBici = Cannondale()
pepe = Ciclista("pepe", creadorBici)
nuevaBici = pepe.crearMountainBike()
print(nuevaBici.frenar())
print(nuevaBici.avanzar())