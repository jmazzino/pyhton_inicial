import tkinter

window = tkinter.Tk()

canvas1 = tkinter.Canvas(window, width=400, height=300)
canvas1.pack()

label1 = tkinter.Label(window, text="Ingrese su nombre y presione OK -> ")
canvas1.create_window(200, 110, window=label1)


entry1 = tkinter.Entry(window)
canvas1.create_window(180, 140, window=entry1)


def printEntry():
    nombre = entry1.get()

    label2 = tkinter.Label(window, text="Hola " + nombre + " Bienvenido!")
    canvas1.create_window(200, 230, window=label2)


button1 = tkinter.Button(text="OK", command=printEntry)
canvas1.create_window(280, 140, window=button1)


tkinter.mainloop()
