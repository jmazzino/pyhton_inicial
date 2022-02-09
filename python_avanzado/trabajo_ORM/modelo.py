from tkinter import *
from sqlite3 import Error
import sqlite3
from base_datos import *


class Abmc:
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

    def baja(self, id):
        """
        Metodo baja esta destinado a realizar la baja de datos contra la base
        """
        self.id = id
        borrar = Agenda.get(Agenda.id == self.id)
        borrar.delete_instance()

    def mod(self, nombre, apellido, interno, email, id):
        """
        Metodo mod esta destinado a realizar la modificacion de datos contra la base
        """
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
