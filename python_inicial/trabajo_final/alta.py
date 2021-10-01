def f_alta():
    MsgBox = tkinter.messagebox.askquestion(
        "Alta de registro",
        "Esta seguro de que quiere ingresar este registro",
        icon="warning",
    )
    if MsgBox == "yes":
        titulo = entry1.get()
        ruta = entry2.get()
        descripcion = entry3.get()
        rc = 0
        if not titulo:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR titulo vacio",
                icon="warning",
            )
            rc = 1
        if not ruta:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR ruta vacio",
                icon="warning",
            )
            rc = 1
        if not descripcion:
            MsgBox = tkinter.messagebox.askquestion(
                "Alta de registro",
                "ERR descripcion vacio",
                icon="warning",
            )
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
