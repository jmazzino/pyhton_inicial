import random
import msvcrt

def ej5():
    print("Ejercicio 5 Escriba un programa que tome 5 números cualesquiera y determine cuales son divisibles por 2")
    print("NUMEROS RANDOM:")
    numeros = []
    for x in range(0, 5):
        numeros.append(random.randint(0, 100000))
    print(numeros)
    for y in numeros:
        if (y % 2) == 0:
            print(f"El número {y} es divisible por 2.")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        else:
            print(f"El número {y} no es divisible por 2.")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
    print("NUMERO POR CONSOLA:")
    seleccion = int(input("Ingrese un número: "))
    if (seleccion % 2) == 0:
        print(f"El número {seleccion} es divisible por 2.")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
    else:
        print(f"El número {seleccion} no es divisible por 2.")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
