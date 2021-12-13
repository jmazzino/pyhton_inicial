import sqlite3
from sqlite3 import Error
# ############# CREAR BASE DE DATOS


def crearbase():

    try:
        con = sqlite3.connect('agenda.db')
        print("Base creada")
    except Error:
        print(Error)
    finally:
        con.close()

crearbase()

