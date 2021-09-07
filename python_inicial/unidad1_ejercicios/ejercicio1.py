"""Realice un programa con Tkinter que tome dos valores, uno entero y el otro un string,
realice la suma como enteros y lo presente en pantalla. 

variable1 = “9”
variable2 = int(variable1)
"""

from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
var1 = 5
var2 = "2"
res = var1 * int(var2)
var = IntVar()
e.config(textvariable=var)
var.set(res)
mainloop()
