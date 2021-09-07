"""Pregunta:              		
¿Cree que para guardar y recuperar información es mejor un diccionario o una lista?         	
Justifique su respuesta.
Es lo mismo va a depender de la complejidad de lo que vamos a guardar. La diferencia
esta en que los diccionarios tienen ese valor de indice como clave y es mas util.

"""
import tkinter

window = tkinter.Tk()

dic = {"identificador": "", "nombre": "", "apellido": "", "telefono": ""}
num = 0
for x in dic:
    num = num + 1

button_widget = tkinter.Button(
    window, text="El número de elementos del diccionario es: " + str(num)
)
button_widget.pack()

tkinter.Label(window, text="###################").pack()

for x in dic:
    tkinter.Label(window, text="Clave -> " + x).pack()
    tkinter.Label(window, text="------------------------").pack()


tkinter.mainloop()
