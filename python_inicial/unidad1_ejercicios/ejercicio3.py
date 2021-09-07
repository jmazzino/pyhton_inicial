"""
Tarea 1:
Realice un programa partiendo del Ejercicio 1 que multiplique el resultado por un número
aleatorio y lo presente en pantalla."""
from tkinter import *
import random

"""
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
var1 = 5
var2 = "2"
n = random.random()
res = n * (var1 * int(var2))
var = IntVar()
e.config(textvariable=var)
var.set(res)
mainloop()
"""

"""Tarea 2:
Presente un ejemplo y explique el funcionamiento de cómo se u
tiliza el siguiente método: random.randrange()
 random.randrange(A, B, C)
 A es donde empieza el rango
 B donde termina el rango
 C es el step, el incremento pero no se bien que es


 ¿Qué es un método?
 metodo funccion son pequeñas herramientas que estan includas en el paquete gral. Se puede utlizar fuciones externas importandolas, o desarrollandolas
¿Qué significa el punto en la expresión anterior?
es la manera de utlizar un atributo de una funcion
"""
from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = random.randrange(0, 100, 1)
b = random.randrange(0, 100, 1)
c = a * b
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
