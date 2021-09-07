'''# La cafetería

Se desea desarrollar una aplicación que permita controlar una máquina de café instantáneo de una universidad


La máquina cuenta con una botonera de 10 dígitos (0-9) para que los usuarios puedan indicar el tipo de café deseado. 
Si bien para todos los tipos de café se utiliza la misma cantidad de agua, la cantidad (gramos) de café puede variar según el tipo indicado 
por el usuario. Por ejemplo:

* Café simple utiliza 22gr de café
* Café doble utiliza 44gr de café.

La máquina cuenta además con un display que le permite mostrar su estado al usuario.

Taner en cuenta que para poder preparar un café, la máquina debe contar con la suficiente cantidad de agua y gramos de cafe.


Casos de uso:

* Preparar un café de forma exitosa
* Intentar preparar un café inexistente (código fuera del rango 0-9)
* Intentar preparar un café sin la suficiente cantidad de café.
* Intentar preparar un café sin la suficiente cantidad de agua.
* Intentar preparar un café sin la suficiente cantidad de algún otro ingrediente como leche.
* Intentar preparar un café y que la máquina se encuentre averiada.'''

import random

## Excepciones 
class OpcionInvalidaException(Exception):
    pass

class NoHayCafeException(Exception):
    pass

class NoHayAguaException(Exception):
    pass

class NoHayLecheException(Exception):
    pass

class maquinaAveriadaException(Exception):
    pass


class MaquinaDeCafe:
    
    CONS_CANTIDAD_AGUA = 5000
    CONS_CANTIDAD_CAFE = 2000
    CONS_CANTIDAD_LECHE = 3000
    CONS_ESTADO = "OK"
    CONS_USAR_AGUA = 150
    CONS_USAR_LECHE = 100
    
    def __init__(self, estado=CONS_ESTADO, cantidadDeCafe=CONS_CANTIDAD_CAFE, 
                cantidadDeAgua=CONS_CANTIDAD_CAFE, cantidadDeLeche=CONS_CANTIDAD_LECHE, name=None):
        self.estado = estado
        self.cantidadDeCafe = cantidadDeCafe
        self.cantidadDeAgua = cantidadDeAgua
        self.cantidadDeLeche = cantidadDeLeche
        self.name = name
        self.tipo_cafe = {
            0: {"cafeSimple": {"gramos": 22, "agua": True}},
            1: {"cafeDoble": {"gramos": 44, "agua": True}},
            2: {"cafeConLeche": {"gramos": 20, "leche": True}},
            3: {"cafeLargo": {"gramos": 20, "leche": True}},
            4: {"cafeManchando": {"gramos": 30, "leche": True}},
            5: {"cafeMoka": {"gramos": 30, "agua": True}},
            6: {"cafeLagrima": {"gramos": 40, "agua": True}},
            7: {"cafeLatte": {"gramos": 15, "leche": True }},
            8: {"cafeExpreso": {"gramos": 50, "agua": True}},
            9: {"cafeCortado": {"gramos": 25, "leche": True}}
        }


    def hacer_cafe(self, opcion):

        self.chequear_estado()
        self.chequear_opcion(opcion)
        cafe_name = list(self.tipo_cafe[opcion].keys())[0]
        gramos = self.tipo_cafe[opcion][cafe_name]["gramos"]
        self.chequear_cafe_disponible(gramos)
        if 'agua' in self.tipo_cafe[opcion][cafe_name]:
            self.chequear_agua_disponible() 
            self.actualizar_cantidad_agua()
        if 'leche' in self.tipo_cafe[opcion][cafe_name]:
            self.chequear_leche_disponible()
            self.actualizar_cantidad_leche()
        
        self.actualizar_cantidad_cafe(gramos)
        cafe = Cafe(self.tipo_cafe[opcion])
    
        return cafe
        


    def chequear_estado(self):

        if self.estado == "OK":
            pass
        else:
            raise maquinaAveriadaException(f"La maquina esta averiada, el estado actual es: {self.estado}")

    def chequear_opcion(self, opcion):

        if opcion >=0 and opcion <10:
            pass
        else:
            raise OpcionInvalidaException("Por favor selecciona una opcion correcta [0-9]")


    def chequear_cafe_disponible(self, gramos):
        
        if self.cantidadDeCafe >= gramos:
            pass
        else:
            raise NoHayCafeException(f"No hay suficiente cafe disponible, actual: {self.cantidadDeCafe}, necesario: {gramos}")

    def chequear_agua_disponible(self):

        if self.cantidadDeAgua >= self.CONS_USAR_AGUA:
            pass
        else:
            raise NoHayAguaException(f"No hay suficiente agua disponible, actual: {self.cantidadDeAgua}, necesario: {self.CONS_USAR_AGUA}")

    def chequear_leche_disponible(self):
        
        if self.cantidadDeLeche >= self.CONS_USAR_LECHE:
            pass
        else:
            raise NoHayLecheException(f"No hay suficiente leche disponible, actual: {self.cantidadDeLeche}, necesario: {self.CONS_USAR_LECHE}")


    def actualizar_cantidad_cafe(self, gramos):
        self.cantidadDeCafe -= gramos

    def actualizar_cantidad_agua(self):
        self.cantidadDeAgua -= self.CONS_USAR_AGUA

    def actualizar_cantidad_leche(self):
        self.cantidadDeLeche -= self.CONS_USAR_LECHE


    def display(self):
        return "Estado: %s\nCantidad de Cafe: %d\nCantidad de Agua: %d \nCantidad de Leche: %d\n" % (self.estado, 
        self.cantidadDeCafe, self.cantidadDeAgua, self.cantidadDeLeche)

    def averiar(self):
        self.estado = "NotOK"



class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola! {self.nombre}"

    def pedir_cafe(self, maquina, opcion):
        return maquina.hacer_cafe(opcion)


class Cafe:
   
    def __init__(self, tipo_cafe):
        self.tipo_cafe = tipo_cafe

    def ver_cafe(self):
        return self.tipo_cafe




### main
if __name__ == "__main__":
    

    ## creación de las personas
    persona1 = Persona("Maria")
    persona2 = Persona("Jose")
    persona3 = Persona("Pablo")

    ## maquinas de cafe de pruebas
    maquinaBuena = MaquinaDeCafe(name="Buena")
    maquinaAveriada = MaquinaDeCafe(estado="NotOK", name="Averiada")
    maquinaConPocaAgua= MaquinaDeCafe(cantidadDeAgua=150, name="PocaAgua")
    maquinaSinLeche= MaquinaDeCafe(cantidadDeLeche=0, name="NoTieneLeche")
    maquinaConPocoCafe = MaquinaDeCafe(cantidadDeCafe=72, name="PocoCafe")

    ## listas con las personas y maquinas de cafes para random
    personas = [persona1, persona2, persona3]
    maquinas = [maquinaBuena, maquinaAveriada, maquinaConPocaAgua, maquinaSinLeche, maquinaConPocoCafe]

    ## random
    repeticiones = random.randint(5,15)
    repeticiones = 1
    print(f"repeticiones: {repeticiones}")
    
    try:
        for r in range(repeticiones):
            x_persona = random.randrange(len(personas))
            x_maquina = random.randrange(len(maquinas))
            x_maquina = 0
            opcion = random.randrange(10)
            print(personas[x_persona].saludar())
            print(f"Maquina de Café: {maquinas[x_maquina].name}\n{maquinas[x_maquina].display()}")
            print(f"La persona escogio la opción: {opcion}")
            cafe = personas[x_persona].pedir_cafe(maquinas[x_maquina], opcion)
            print(f"El cafe que pedi es: {cafe.ver_cafe()}")
            print(f"Maquina de Café: {maquinas[x_maquina].name}\n{maquinas[x_maquina].display()}")
    except Exception as e:
        print(f"Ocurrio un error, mensaje: {e}")
              


