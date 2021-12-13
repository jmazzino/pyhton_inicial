from tkinter import *
from sqlite3 import Error
import sqlite3


class Abmc:
    """
    Clase Abmc destinada a realizar el alta, baja modificacion y consulta de la aplicacion
    """

    def conectar(self):
        """
        Metodo conectar, esta destinado a la conexion con la DB
        """
        try:
            con = sqlite3.connect("agenda.db")
            return con
        except Error:
            print(Error)

    def alta(self, nombre, apellido, interno, email):
        """
        Metodo alta, esta destinado a realizar el alta de datos contra la base
        """
        params = (nombre, apellido, interno, email)
        con = self.conectar()
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO personas VALUES( NULL,?, ?, ?, ?)", params)
        con.commit()

    def baja(self, id):
        """
        Metodo baja esta destinado a realizar la baja de datos contra la base
        """
        params = id
        con = self.conectar()
        cursorObj = con.cursor()
        cursorObj.execute("DELETE from personas where id = {}".format(id))
        con.commit()

    def mod(self, nombre, apellido, interno, email, id):
        """
        Metodo mod esta destinado a realizar la modificacion de datos contra la base
        """
        params = (nombre, apellido, interno, email, id)
        con = self.conectar()
        cursorObj = con.cursor()
        # SQL
        sql1 = """ UPDATE personas
        SET nombre = ? ,
            apellido = ? ,
            interno = ? ,
            email = ?
        WHERE id = ?"""
        cursorObj.execute(sql1, params)
        con.commit()
