import msvcrt


def ej1():
    print(
        "Ejercicio 1 Escribir un programa que tome el valor del nombre del usuario por consola y luego lo imprima en pantalla."
    )
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}!")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
