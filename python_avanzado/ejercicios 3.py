"definir una persona nombre apellido y que se presente"

class Persona:

    def __init__(self,nombre,apellido):
        self.__nombre=nombre
        self.__apellido=apellido

    @property
    def get_nombre(self):
        return self.__nombre
    
    @get_nombre.setter
    def get_nombre(self,nombre):
        self.__nombre = nombre

    @property
    def get_apellido(self):
        return self.__apellido
    
    @get_apellido.setter
    def get_apellido(self,apellido):
        self.__apellido = apellido

    def saludar(self):
        return "Hola mi nombre es {} {}".format(self.__nombre, self.__apellido)
        
persona1=Persona("pedro", "marin")

print(persona1.saludar())