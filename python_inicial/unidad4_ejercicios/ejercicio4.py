import msvcrt


def ej4():
    print(
        "Ejercicio 4 Escriba un programa que permita tomar una palabra retorne las vocales que contenga junto con la cantidad de veces que se repite. "
    )
    palabra = input("Ingrese una palabra: ")
    letras = []
    veces = []
    repeticion = []

    for x in palabra:
        if x == "a":
            letras.append(x)
        elif x == "e":
            letras.append(x)
        elif x == "i":
            letras.append(x)
        elif x == "o":
            letras.append(x)
        elif x == "u":
            letras.append(x)

    palabra = list(dict.fromkeys(palabra))
    for y in letras:
        veces.append(letras.count(y))

    letras = list(dict.fromkeys(letras))

    for z in range(0, len(letras)):
        repeticion.append([letras[z], veces[z]])

    print(repeticion)
    print("Presione una tecla para continuar...")
    msvcrt.getch()
