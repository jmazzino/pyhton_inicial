from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
var1 = 5
var2 = "2"
res = str(var1) + var2
var = IntVar()
e.config(textvariable=var)
var.set(res)
mainloop()
