from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sqlite3 import Error
from base_datos import *

import modelo
import tkinter
import sqlite3


class Ventana:
    """
    Clase Ventana esta destinado a realizar la instancia de la ventana principal
    """

    def __init__(self, window):
        """
        Metodo init , esta destinado a la configuracion de la ventana, treeview y botones
        """
        self.root = window
        self.nuevo_c = modelo.Abmc()
        # self.f_alta()
        self.root.geometry("700x600")
        self.root.title("AGENDA")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="khaki3")

        tree = ttk.Treeview(self.root)
        tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        tree.column("#0", width=10, minwidth=10, anchor=W)
        tree.column("col1", width=25, minwidth=25)
        tree.column("col2", width=80, minwidth=80)
        tree.column("col3", width=100, minwidth=100)
        tree.column("col4", width=100, minwidth=100)
        tree.column("col5", width=100, minwidth=100)
        tree.column("col6", width=200, minwidth=100)
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Nombre")
        tree.heading("#3", text="Apellido")
        tree.heading("#4", text="Interno")
        tree.heading("#5", text="E-mail")
        tree.heading("#6", text="STR")
        tree.place(x=40, y=300)

        Label(
            self.root,
            text="Ingrese sus datos:",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=40, y=130)
        Label(
            self.root,
            text="Nombre",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=40, y=170)
        Label(
            self.root,
            text="Apellido",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=40, y=200)
        Label(
            self.root,
            text="Interno",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=40, y=230)
        Label(
            self.root,
            text="E-mail",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=40, y=260)
        Label(
            self.root,
            text="ID",
            fg="black",
            bg="khaki4",
            borderwidth=1,
            relief="solid",
        ).place(x=275, y=170)

        entry1 = Entry(self.root)
        entry2 = Entry(self.root)
        entry3 = Entry(self.root)
        entry4 = Entry(self.root)
        entry5 = Entry(self.root)

        entry1.place(x=100, y=170)
        entry2.place(x=100, y=200)
        entry3.place(x=100, y=230)
        entry4.place(x=100, y=260)
        entry5.place(x=300, y=170)

        def f_salir():
            """
            Metodo f_salir, esta destinado a realizar la salida de la aplicacion
            """
            MsgBox = tkinter.messagebox.askquestion(
                "Salir de la aplicacion",
                "Esta seguro de que quiere salir de la aplicacion",
                icon="warning",
            )
            if MsgBox == "yes":
                self.root.destroy()

        def f_oculta():
            """
            Metodo f_oculta, esta destinado a realizar la limpieza del treeview
            """
            # limpieza de tabla
            records = tree.get_children()
            for element in records:
                tree.delete(element)

        def f_muestra():
            # limpieza de tabla
            records = tree.get_children()
            for element in records:
                tree.delete(element)

            for valor_recuperado in Agenda.select():
                tree.insert(
                    "",
                    0,
                    values=(
                        valor_recuperado.id,
                        valor_recuperado.nombre,
                        valor_recuperado.apellido,
                        valor_recuperado.interno,
                        valor_recuperado.email,
                        valor_recuperado,
                    ),
                )

        def f_alta():
            """
            Metodo f_alta, esta destinado a tomar los datos para luego llamar a la funcion alta
            """
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
                    self.nuevo_c.alta(nombre, apellido, interno, email)

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

        def f_baja():
            """
            Metodo f_baja, esta destinado a tomar los datos para luego llamar a la funcion baja
            """
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
                    self.nuevo_c.baja(id)

                    MsgBox = tkinter.messagebox.showinfo(
                        "Baja de registro",
                        "BAJA Exitosa",
                        icon="warning",
                    )
                    f_muestra()

        def f_mod():
            """
            Metodo f_mod, esta destinado a tomar los datos para luego llamar a la funcion mod
            """
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
                    self.nuevo_c.mod(nombre, apellido, interno, email, id)

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

        def f_bus():
            """
            Metodo f_bus, esta destinado a tomar los datos para luego llamar a la funcion bus
            """
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

                    # limpieza de tabla
                    records = tree.get_children()
                    for element in records:
                        tree.delete(element)

                    agenda = Agenda()
                    self.id = id

                    for valor_recuperado in Agenda.select().where(Agenda.id == self.id):
                        tree.insert(
                            "",
                            0,
                            values=(
                                valor_recuperado.id,
                                valor_recuperado.nombre,
                                valor_recuperado.apellido,
                                valor_recuperado.interno,
                                valor_recuperado.email,
                                valor_recuperado,
                            ),
                        )

        # defino y ubico los botones
        Button(self.root, text="Alta", fg="black", bg="khaki2", command=f_alta).place(
            x=40, y=0
        )

        Button(
            self.root, text="Mostrar todo", fg="black", bg="khaki2", command=f_muestra
        ).place(x=40, y=550)

        Button(
            self.root, text="Borrar Vista", fg="black", bg="khaki2", command=f_oculta
        ).place(x=140, y=550)

        Button(
            self.root, text="Busqueda", fg="black", bg="khaki2", command=f_bus
        ).place(x=100, y=0)

        Button(
            self.root, text="Modificacion", fg="black", bg="khaki2", command=f_mod
        ).place(x=200, y=0)

        Button(self.root, text="Baja", fg="black", bg="khaki2", command=f_baja).place(
            x=300, y=0
        )

        Button(self.root, text="Salir", fg="black", bg="red2", command=f_salir).place(
            x=650, y=0
        )
