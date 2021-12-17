from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import random
import tkinter

import sqlite3
from sqlite3 import Error

root = Tk()
root.geometry("700x600")
root.title("AGENDA")
root.resizable(width=False, height=False)
root.configure(bg="khaki3")


tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=10, minwidth=10, anchor=W)
tree.column("col1", width=25, minwidth=25)
tree.column("col2", width=80, minwidth=80)
tree.column("col3", width=100, minwidth=100)
tree.column("col4", width=100, minwidth=100)
tree.column("col5", width=100, minwidth=100)
tree.heading("#1", text="ID")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Apellido")
tree.heading("#4", text="Interno")
tree.heading("#5", text="E-mail")
tree.place(x=40, y=300)

Label(
    root,
    text="Ingrese sus datos:",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=130)
Label(
    root,
    text="Nombre",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=170)
Label(
    root,
    text="Apellido",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=200)
Label(
    root,
    text="Interno",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=230)
Label(
    root,
    text="E-mail",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=260)
Label(
    root,
    text="ID",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=275, y=170)

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)

entry1.place(x=100, y=170)
entry2.place(x=100, y=200)
entry3.place(x=100, y=230)
entry4.place(x=100, y=260)
entry5.place(x=300, y=170)


def f_bus():
    MsgBox = tkinter.messagebox.askquestion(
        "Busqueda de registro",
        "La busqueda de registro se realiza por ID. Esta seguro de que quiere realizar la busqueda de este registro?",
        icon="warning",
    )
    if MsgBox == "yes":
        id = entry5.get()
        rc = 0
        if not id:
            MsgBox = tkinter.messagebox.showinfo(
                "Busqueda de registro",
                "ERR ID vacio",
                icon="warning",
            )
        else:

            def conectar():
                try:
                    con = sqlite3.connect("agenda.db")
                    return con
                except Error:
                    print(Error)

            def buscarregistro(con):
                # limpieza de tabla
                records = tree.get_children()
                for element in records:
                    tree.delete(element)

                # Consiguiendo datos
                sql = "SELECT * FROM personas where id = {} ORDER BY id DESC".format(id)

                cursorObj = con.cursor()
                cursorObj.execute(sql)

                resultado = cursorObj.fetchall()

                for fila in resultado:
                    tree.insert(
                        "",
                        0,
                        values=fila,
                    )

            con = conectar()
            buscarregistro(con)


def f_salir():
    MsgBox = tkinter.messagebox.askquestion(
        "Salir de la aplicacion",
        "Esta seguro de que quiere salir de la aplicacion",
        icon="warning",
    )
    if MsgBox == "yes":
        root.destroy()


def f_baja():
    MsgBox = tkinter.messagebox.askquestion(
        "Eliminacion de registro",
        "La Eliminacion de registro se realiza por ID. Esta seguro de que quiere realizar la eliminacion de este registro?",
        icon="warning",
    )
    if MsgBox == "yes":
        id = entry5.get()
        rc = 0
        if not id:
            MsgBox = tkinter.messagebox.showinfo(
                "Eliminacion de registro",
                "ERR ID vacio",
                icon="warning",
            )
        else:

            def conectar():
                try:
                    con = sqlite3.connect("agenda.db")
                    return con
                except Error:
                    print(Error)

            def eliminarregistro(con):
                # limpieza de tabla
                records = tree.get_children()
                for element in records:
                    tree.delete(element)

                # Consiguiendo datos
                sql = "DELETE from personas where id = {}".format(id)

                cursorObj = con.cursor()
                cursorObj.execute(sql)
                con.commit()

            con = conectar()
            eliminarregistro(con)
            MsgBox = tkinter.messagebox.showinfo(
                "Elimicacion de registro",
                "Eliminacion Exitosa",
                icon="warning",
            )
            f_muestra()


def f_mod():
    MsgBox = tkinter.messagebox.askquestion(
        "Modificion de registro",
        "La modifcacion de registro se realiza por ID + los datos a modicar, TODOS los datos seran necesarios. Esta seguro de que quiere realizar la modificion de este registro?",
        icon="warning",
    )
    if MsgBox == "yes":
        nombre = entry1.get()
        apellido = entry2.get()
        interno = entry3.get()
        email = entry4.get()
        id = entry5.get()
        rc = 0
        if not id:
            MsgBox = tkinter.messagebox.showinfo(
                "Busqueda de registro",
                "ERR ID vacio",
                icon="warning",
            )
            rc = 1
        if not nombre:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Nombre vacio",
                icon="warning",
            )
            rc = 1
        if not apellido:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Apellido vacio",
                icon="warning",
            )
            rc = 1
        if not interno:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Interno vacio",
                icon="warning",
            )
            rc = 1
        if not email:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR E-mail vacio",
                icon="warning",
            )
            rc = 1

        if rc == 0:

            def conectar():
                try:
                    con = sqlite3.connect("agenda.db")
                    return con
                except Error:
                    print(Error)

            def modificarregistro(con, task):
                # limpieza de tabla
                records = tree.get_children()
                for element in records:
                    tree.delete(element)

                # SQL
                sql1 = """ UPDATE personas
              SET nombre = ? ,
                  apellido = ? ,
                  interno = ? ,
                  email = ?
              WHERE id = ?"""

                cursorObj = con.cursor()
                cursorObj.execute(sql1, task)

                con.commit()

                resultado = cursorObj.fetchall()

                for fila in resultado:
                    print(fila)
                    tree.insert(
                        "",
                        0,
                        values=fila,
                    )

            con = conectar()
            modificarregistro(con, (nombre, apellido, interno, email, id))
            MsgBox = tkinter.messagebox.showinfo(
                "Modificacion de registro",
                "Modificacion Exitosa",
                icon="warning",
            )
            f_muestra()

    else:
        tkinter.messagebox.showinfo(
            "Alta de registro",
            "Alta anulada",
            icon="warning",
        )


def f_alta():
    MsgBox = tkinter.messagebox.askquestion(
        "Alta de registro",
        "Esta seguro de que quiere ingresar este registro",
        icon="warning",
    )
    if MsgBox == "yes":
        nombre = entry1.get()
        apellido = entry2.get()
        interno = entry3.get()
        email = entry4.get()
        rc = 0
        if not nombre:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Nombre vacio",
                icon="warning",
            )
            rc = 1
        if not apellido:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Apellido vacio",
                icon="warning",
            )
            rc = 1
        if not interno:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR Interno vacio",
                icon="warning",
            )
            rc = 1
        if not email:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ERR E-mail vacio",
                icon="warning",
            )
            rc = 1

        if rc == 0:

            def conectar():
                try:
                    con = sqlite3.connect("agenda.db")
                    return con
                except Error:
                    print(Error)

            def insertarregistro(con, nombre, apellido, interno, email):
                params = (nombre, apellido, interno, email)

                cursorObj = con.cursor()
                cursorObj.execute(
                    "INSERT INTO personas VALUES( NULL,?, ?, ?, ?)", params
                )
                con.commit()

            con = conectar()
            insertarregistro(con, nombre, apellido, interno, email)
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "ALTA Exitosa",
                icon="warning",
            )
            f_muestra()

        else:
            MsgBox = tkinter.messagebox.showinfo(
                "Alta de registro",
                "Se encontraron campos vacios",
                icon="warning",
            )
    else:
        tkinter.messagebox.showinfo(
            "Alta de registro",
            "Alta anulada",
            icon="warning",
        )


def f_muestra():
    def conectar():
        try:
            con = sqlite3.connect("agenda.db")
            return con
        except Error:
            print(Error)

    def mostrarregistro(con):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        # Consiguiendo datos
        sql = "SELECT * FROM personas ORDER BY id DESC"

        cursorObj = con.cursor()
        cursorObj.execute(sql)
        resultado = cursorObj.fetchall()

        for fila in resultado:
            tree.insert(
                "",
                0,
                values=fila,
            )

    con = conectar()
    mostrarregistro(con)


def f_oculta():
    # limpieza de tabla
    records = tree.get_children()
    for element in records:
        tree.delete(element)


# defino y ubico los botones
Button(root, text="Alta", fg="black", bg="khaki2", command=f_alta).place(x=40, y=0)
Button(root, text="Mostrar todo", fg="black", bg="khaki2", command=f_muestra).place(
    x=40, y=550
)
Button(root, text="Borrar Vista", fg="black", bg="khaki2", command=f_oculta).place(
    x=140, y=550
)
Button(root, text="Busqueda", fg="black", bg="khaki2", command=f_bus).place(x=100, y=0)
Button(root, text="Modificacion", fg="black", bg="khaki2", command=f_mod).place(
    x=200, y=0
)
Button(root, text="Baja", fg="black", bg="khaki2", command=f_baja).place(x=300, y=0)
Button(root, text="Salir", fg="black", bg="red2", command=f_salir).place(x=650, y=0)

mainloop()
