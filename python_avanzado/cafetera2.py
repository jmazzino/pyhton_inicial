import time
from abc import ABC, abstractmethod


class Cafe(ABC):

    @abstractmethod
    def preparar(self, insumos):
        pass

    @staticmethod
    def calcular_insumos(insumos, requerido):
        if insumos["cafe"] >= requerido["cafe"] \
                and insumos["agua"] >= requerido["agua"] \
                and insumos["leche"] >= requerido["leche"]:
            insumos["cafe"] = insumos["cafe"] - requerido["cafe"]
            insumos["agua"] = insumos["agua"] - requerido["agua"]
            insumos["leche"] = insumos["leche"] - requerido["leche"]
        else:
            raise MaterialesInsuficientesException("Insumos insuficientes para el cafe solicitado,"
                                                   " contacte mantenimiento")


class Expreso(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 0}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Americano(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 200, "leche": 0}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Doble(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 44, "agua": 200, "leche": 0}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Cortado(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 50}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class ConLeche(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 100}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Lagrima(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 50, "leche": 200}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Capuchino(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 100}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Latte(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 100}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class Machiatto(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 22, "agua": 100, "leche": 0}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class DobleConLeche(Cafe):
    def preparar(self, insumos):
        requerido = {"cafe": 44, "agua": 100, "leche": 100}
        self.calcular_insumos(insumos, requerido)
        time.sleep(5)
        return insumos


class MaquinaCafe:
    menu = {
        1: Expreso,
        2: Americano,
        3: Doble,
        4: Cortado,
        5: ConLeche,
        6: Lagrima,
        7: Capuchino,
        8: Latte,
        9: Machiatto,
        0: DobleConLeche
    }

    def __init__(self, cafe, agua, leche):
        self._cafe = cafe
        self._agua = agua
        self._leche = leche
        self._estado_valido = False

    def procesar_codigo(self, codigo):
        if codigo in range(0, 10):
            self.preparar_cafe(self.menu.get(codigo))
        else:
            raise ValorIngresadoException(codigo)

    def preparar_cafe(self, opcion):
        try:
            if self._estado_valido:
                self.mostar_estado_en_display(f"Preparando pedido Café {opcion.__name__}")
                self.actualizar_insumos(opcion
                                        .preparar(opcion, {"cafe": self._cafe, "agua": self._agua, "leche": self._leche}))
                self.entregar_cafe(opcion.__name__)
                self._estado_valido = self.validar_estado()
            else:
                self.mostar_estado_en_display("El pedido no puede ser preparado, solicite mantenimiento")
        except MaterialesInsuficientesException as e:
            self.mostar_estado_en_display(f"problemas perparando el cafe pedido: {e}")

    def entregar_cafe(self, resultado):
        self.mostar_estado_en_display(f"*******************************")
        self.mostar_estado_en_display(f"El Café {resultado} esta listo!")
        self.mostar_estado_en_display(f"*******************************\n")

    def mostar_estado_en_display(self, mensaje):
        print(mensaje)

    def validar_estado(self):
        if self._cafe < 22:
            raise EstadoCafeteraException("Café insuficiente. Solicite recarga a mantenimiento")
        elif self._agua < 100:
            raise EstadoCafeteraException("Nivel de agua bajo. Solicite revision a mantenimiento")

        return True

    def mantenerse_lista(self):
        while self._estado_valido:
            try:
                codigo = int(input("Por favor seleccione su opción"))
                self.procesar_codigo(codigo)

            except ValorIngresadoException as e:
                self.mostar_estado_en_display(f"El valor {e} no esta dentro de las opciones")

    def encender(self):
        try:
            self._estado_valido = self.validar_estado()
            self.mostar_estado_en_display("Maquina encendida")
            for opcion in self.menu:
                print(f"Opción {opcion}: Cafe {self.menu[opcion].__name__}")
            self.mantenerse_lista()
        except EstadoCafeteraException as e:
            self.mostar_estado_en_display(e)

    def actualizar_insumos(self, insumos):
        self._leche = insumos["leche"]
        self._agua = insumos["agua"]
        self._cafe = insumos["cafe"]


class EstadoCafeteraException(Exception):
    pass


class ValorIngresadoException(Exception):
    pass


class MaterialesInsuficientesException(Exception):
    pass


maquina = MaquinaCafe(100, 1000, 100)
maquina.encender()