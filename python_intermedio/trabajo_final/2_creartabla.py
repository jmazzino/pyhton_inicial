import sqlite3
from sqlite3 import Error


def conectar():
    try:
        con = sqlite3.connect("agenda.db")
        return con
    except Error:

        print(Error)


def creartabla(con):

    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE personas(id integer PRIMARY KEY, nombre text, apellido text, interno text, email text)"
    )
    con.commit()
    print("Tabla creada")


con = conectar()

creartabla(con)
