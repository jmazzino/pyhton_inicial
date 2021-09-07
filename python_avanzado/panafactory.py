from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_vigilante(self) -> None:
        pass

    @abstractmethod
    def produce_medialuna(self) -> None:
        pass

    @abstractmethod
    def produce_bombacrema(self) -> None:
        pass

    @abstractmethod
    def produce_tortita(self) -> None:
        pass

    @abstractmethod
    def produce_ricota(self) -> None:
        pass

    @abstractmethod
    def produce_lemonpie(self) -> None:
        pass

    @abstractmethod
    def produce_copitos(self) -> None:
        pass


class ConcreteBuilder1(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:

        product = self._product
        self.reset()
        return product

      

    def produce_vigilante(self) -> None:
        self._product.add("Vigilante")

    def produce_medialuna(self) -> None:
        self._product.add("MediaLuna")

    def produce_bombacrema(self) -> None:
        self._product.add("BombaCremaPastelera")

    def produce_tortita(self) -> None:
        self._product.add("TortitasdeAzucar")

    def produce_ricota(self) -> None:
        self._product.add("Tricota")

    def produce_lemonpie(self) -> None:
        self._product.add("Lemon pie")

    def produce_copitos(self) -> None:
        self._product.add("Copitos de chocolate y dulce de leche")


class Product1():

    def __init__(self) -> None:
        self.comanda = []

    def add(self, part: Any) -> None:
        self.comanda.append(part)

    def list_comanda(self) -> None:
        print("\n")
        print(f"Comanda: {', '.join(self.comanda)}", end="")
    
class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:

        self._builder = builder

       

if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("\n")

    print("Pedido: ")
    builder.produce_vigilante()
    #builder.produce_medialuna()
    #builder.produce_tortita()

    builder.product.list_comanda()

    print("\n")