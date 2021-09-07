from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_cuadro(self) -> None:
        pass

    @abstractmethod
    def produce_rueda(self) -> None:
        pass

    @abstractmethod
    def produce_asiento(self) -> None:
        pass

    @abstractmethod
    def produce_canasto(self) -> None:
        pass

    @abstractmethod
    def produce_luz(self) -> None:
        pass

    @abstractmethod
    def produce_motor(self) -> None:
        pass

    @abstractmethod
    def produce_gps(self) -> None:
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

    def produce_cuadro(self) -> None:
        self._product.add("Cuadro")

    def produce_rueda(self) -> None:
        self._product.add("Rueda")

    def produce_asiento(self) -> None:
        self._product.add("Asiento")

    def produce_canasto(self) -> None:
        self._product.add("Canasto")

    def produce_luz(self) -> None:
        self._product.add("Luz")

    def produce_motor(self) -> None:
        self._product.add("Motor")

    def produce_gps(self) -> None:
        self._product.add("Gps")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:

        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_cuadro()
        self.builder.produce_rueda()
        self.builder.produce_asiento()

    def build_full_featured_product(self) -> None:
        self.builder.produce_cuadro()
        self.builder.produce_rueda()
        self.builder.produce_asiento()
        self.builder.produce_canasto()
        self.builder.produce_luz()
        self.builder.produce_motor()
        self.builder.produce_gps()
        

if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Bicicleta de componentes basicos PRE BUILD: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Bicicleta con todos los componentes PRE BUILD: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Bicicleta con componentes customizados: ")
    builder.produce_cuadro()
    builder.produce_rueda()
    builder.produce_canasto()
    builder.product.list_parts()

    print("\n")