import msvcrt


def ej6():
    print(
        "Ejercicio 6 Escriba un programa que pida la fecha según el formato 04/12/1973 y lo retorne según el formato 1973/12/04"
    )
    dato = input("Ingrese la fecha de hoy en formato DD/MM/AAAA: ")
    fecha = dato.split("/")
    print(f"La ingresada es {fecha[2]}/{fecha[1]}/{fecha[0]}.")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
