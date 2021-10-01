from tkinter import *
from tkinter import messagebox

import random
import tkinter
import alta
import bus

root = Tk()
root.geometry("700x600")
root.title("AGENDA")
root.configure(bg="khaki3")

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
    text="CEU",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=170)
Label(
    root,
    text="Nombre",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=200)
Label(
    root,
    text="Apellido",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=230)
Label(
    root,
    text="Interno",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=260)
Label(
    root,
    text="Puesto",
    fg="black",
    bg="khaki4",
    borderwidth=1,
    relief="solid",
).place(x=40, y=290)

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry1.place(x=100, y=170)
entry2.place(x=100, y=200)
entry3.place(x=100, y=230)
entry4.place(x=100, y=260)
entry5.place(x=100, y=290)


db = {}


def f_bus():
    Label(root, text=db).grid(row=12, column=0, sticky=W)


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
        "Baja de registro",
        "Esta seguro de que quiere dar de baja el registro",
        icon="warning",
    )
    if MsgBox == "yes":
        tkinter.messagebox.showinfo(
            "Baja de registro",
            "Eliminacion completa",
            icon="warning",
        )
    else:
        tkinter.messagebox.showinfo(
            "Baja de registro",
            "Eliminacion anulada",
            icon="warning",
        )


def f_mod():
    MsgBox = tkinter.messagebox.askquestion(
        "Modificacion de registro",
        "Esta seguro de que quiere modififar el registro",
        icon="warning",
    )
    if MsgBox == "yes":
        tkinter.messagebox.showinfo(
            "Modificacion de registro",
            "Modificacion completa",
            icon="warning",
        )
    else:
        tkinter.messagebox.showinfo(
            "Modificacion de registro",
            "Modificacion anulada",
            icon="warning",
        )


def f_alta():
    MsgBox = tkinter.messagebox.askquestion(
        "Alta de registro",
        "Esta seguro de que quiere ingresar este registro",
        icon="warning",
    )
    if MsgBox == "yes":
        ceu = entry1.get()
        nombre = entry2.get()
        apellido = entry3.get()
        interno = entry4.get()
        puesto = entry5.get()
        rc = 0
        if not ceu:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR CEU vacio",
                icon="warning",
            )
            rc = 1
        if not nombre:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR Nombre vacio",
                icon="warning",
            )
            rc = 1
        if not apellido:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR Apellido vacio",
                icon="warning",
            )
            rc = 1
        if not interno:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR Interno vacio",
                icon="warning",
            )
            rc = 1
        if not puesto:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR Puesto vacio",
                icon="warning",
            )
            rc = 1
        if rc == 0:
            aux = {
                "CEU": ceu,
                "Nombre": nombre,
                "Apellido": apellido,
                "Interno": interno,
                "Puesto": puesto,
            }

            print("Insertando")
            print(aux)
            db[ceu] = aux
            aux = {}
            print("---------------------")
            print("Muestro que quedo")
            print(db)
            Label(root, text="ESTA ES LA BASE", fg="green2", bg="black").place(
                x=40, y=350
            )
            consola = Label(root, text=db, fg="green2", bg="black").place(x=40, y=375)
            print("#####################")
            MsgBox = tkinter.messagebox.showinfo(
                "ALTA de registro",
                "ALTA Exitosa",
                icon="warning",
            )
            consola.place_forget()

        else:
            MsgBox = tkinter.messagebox.askquestion(
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
    MsgBox = tkinter.messagebox.askquestion(
        "Baja de registro",
        "Esta seguro de que quiere dar de baja el registro",
        icon="warning",
    )
    if MsgBox == "yes":
        tkinter.messagebox.showinfo(
            "Baja de registro",
            "Eliminacion completa",
            icon="warning",
        )
    else:
        tkinter.messagebox.showinfo(
            "Baja de registro",
            "Eliminacion anulada",
            icon="warning",
        )


Button(root, text="ALTA", fg="black", bg="khaki2", command=f_alta).place(x=0, y=0)
Button(root, text="BUSQUEDA", fg="black", bg="khaki2", command=f_bus).place(x=100, y=0)
Button(root, text="MODIFICACION", fg="black", bg="khaki2", command=f_mod).place(
    x=200, y=0
)
Button(root, text="BAJA", fg="black", bg="khaki2", command=f_baja).place(x=300, y=0)
Button(root, text="Salir", fg="black", bg="red2", command=f_salir).place(x=650, y=0)

mainloop()
