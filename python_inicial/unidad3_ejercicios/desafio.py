from tkinter import *
import random

root = Tk()
root.geometry("300x200")
root.title("Unidad 3 - Desafio")

Label(root, text="Ingrese sus datos:", font=("courier", 11, "bold")).grid(
    row=0, column=1
)
Label(root, text="Titulo").grid(row=2, column=0, sticky=W)
Label(root, text="Ruta").grid(row=4, column=0, sticky=W)
Label(root, text="Descripcion").grid(row=6, column=0, sticky=W)

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry1.grid(row=2, column=1)
entry2.grid(row=4, column=1)
entry3.grid(row=6, column=1)

db = {}


def f_alta():
    titulo = entry1.get()
    ruta = entry2.get()
    descripcion = entry3.get()
    rc = 0
    if not titulo:
        print("ERR titulo vacio")
        rc = 1
    if not ruta:
        print("ERR ruta vacia")
        rc = 1
    if not descripcion:
        print("ERR descripcion vacia")
        rc = 1
    if rc == 0:
        aux = {"Titulo": titulo, "Ruta": ruta, "Descripcion": descripcion}
        print("#####################")
        print("Insertando")
        print(aux)
        db[titulo] = aux
        aux = {}
        print("---------------------")
        print("Muestro que quedo")
        print(db)
        print("#####################")
    else:
        print("#####################")
        print("ERR No se pudo insertar")
        print("ERR Verificar campos vacios")
        print("#####################")


def f_sorpresa():
    color = ["blue", "green", "yellow", "black", "red"]
    colorete = color[random.randrange(0, 4, 1)]
    root.configure(bg=colorete)
    print("cambio color!")


Button(root, text="ALTA", command=f_alta).grid(row=8, column=0)
Button(root, text="SORPRESA", command=f_sorpresa).grid(row=8, column=1)


mainloop()
