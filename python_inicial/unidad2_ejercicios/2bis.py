import tkinter

window = tkinter.Tk()
window.title("Button GUI")
lista_feliz = ["manzana", "pera"]
button_widget = tkinter.Button(
    window, text="Me comi una " + lista_feliz[0] + " pero perdi la " + lista_feliz[1]
)
button_widget.pack()
tkinter.mainloop()
