import msvcrt


def ej3():
    print(
        "Ejercicio 3 Escribir un programa que permita tomar un número por consola y imprima los números entre cero y el número de menor a mayor separados por coma y luego de mayor a menor separado por coma"
    )
    numero = int(input("Ingrese un número: "))
    lista = []
    for x in range(0, numero + 1):
        lista.append(x)
    print(lista, sep=", ")
    lista.reverse()
    print(lista, sep=", ")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
