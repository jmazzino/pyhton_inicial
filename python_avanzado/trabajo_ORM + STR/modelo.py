from tkinter import *
from sqlite3 import Error
import sqlite3
from base_datos import *
from datetime import datetime

dt = datetime.now()
numero_de_llamada = 0


class Tema:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj

    def add(self):
        """
        Metodo add del ConcreteObserverA esta destinado a realizar la actualizacion de estado
        """
        self.id = id
        print("###############################################")
        print("Se agrego el registro en la base de datos:", dt)

    def delete(self):
        """
        Metodo delete del ConcreteObserverA esta destinado a realizar la actualizacion de estado
        """
        print("###############################################")
        print("Se elimino un registro en la base de datos:", dt)

    def update(self):
        """
        Metodo update del ConcreteObserverA esta destinado a realizar la actualizacion de estado
        """
        print("###############################################")
        print("Se actualizo un registro en la base de datos:", dt)


class Abmc(Tema):
    def contar_llamadas(funcion):
        def envoltura(*args, **kwargs):
            global numero_de_llamada
            numero_de_llamada += 1
            print(
                "Llamada número %s a la función %s"
                % (numero_de_llamada, funcion.__name__)
            )
            return funcion(*args, **kwargs)

        return envoltura

    @contar_llamadas
    def alta(self, nombre, apellido, interno, email):
        """
        Metodo alta, esta destinado a realizar el alta de datos contra la base
        """
        self.nombre = nombre
        self.apellido = apellido
        self.interno = interno
        self.email = email
        agenda = Agenda()
        agenda.nombre = self.nombre
        agenda.apellido = self.apellido
        agenda.interno = self.interno
        agenda.email = self.email
        agenda.save()
        ConcreteObserverA.add(agenda)

    @contar_llamadas
    def baja(self, id):
        """
        Metodo baja esta destinado a realizar la baja de datos contra la base
        """
        agenda = Agenda()
        self.id = id
        borrar = Agenda.get(Agenda.id == self.id)
        borrar.delete_instance()
        ConcreteObserverA.delete(agenda)

    @contar_llamadas
    def mod(self, nombre, apellido, interno, email, id):
        """
        Metodo mod esta destinado a realizar la modificacion de datos contra la base
        """
        agenda = Agenda()
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.interno = interno
        self.email = email
        actualizar = Agenda.update(
            nombre=self.nombre,
            apellido=self.apellido,
            interno=self.interno,
            email=self.email,
        ).where(Agenda.id == self.id)
        actualizar.execute()
        ConcreteObserverA.update(agenda)
