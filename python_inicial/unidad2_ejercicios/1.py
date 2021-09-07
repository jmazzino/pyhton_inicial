from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

lista_feliz = ["manzana", "pera", "banana", "uva", "mandarina", "anana", "melon"]
# print(lista_feliz[2])
var = IntVar()
e.config(textvariable=var)
var.set(lista_feliz[2])
mainloop()
