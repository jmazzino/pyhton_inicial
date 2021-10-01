import msvcrt


def ej2():
    print(
        "Ejercicio 2 Escribir un programa que tome el valor del nombre del usuario por consola y luego lo imprima en pantalla."
    )
    numero = int(input("Ingrese el número: "))
    parciales = [numero]
    total = 1
    for x in range(1, numero):
        parciales.append(x)
    for x in parciales:
        total = total * x
    print(f"El factorial de {numero} es {total}.")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
