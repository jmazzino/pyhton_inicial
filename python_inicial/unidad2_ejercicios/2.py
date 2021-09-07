from tkinter import *

root = Tk()
root.title("Unidad 2 Ejercicio 2")
e = Entry(root)
e.pack()
e.focus_set()

lista_feliz = ["manzana", "pera"]

var = IntVar()
e.config(textvariable=var)
var.set("Me compre una " + lista_feliz[0] + " pero perdi la " + lista_feliz[1])

mainloop()
