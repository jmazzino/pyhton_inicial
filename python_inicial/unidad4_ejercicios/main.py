import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6


def menu():
    menu_texto = """
Eliga opcion de ejercicio:

1. Ejercicio 1
2. Ejercicio 2
3. Ejercicio 3
4. Ejercicio 4
5. Ejercicio 5
6. Ejercicio 6
7. Salir
"""
    print(menu_texto)
    seleccion = int(input("Eliga opcion de ejercicio: "))
    if seleccion == 1:
        ejercicio1.ej1()
    elif seleccion == 2:
        ejercicio2.ej2()
    elif seleccion == 3:
        ejercicio3.ej3()
    elif seleccion == 4:
        ejercicio4.ej4()
    elif seleccion == 5:
        ejercicio5.ej5()
    elif seleccion == 6:
        ejercicio6.ej6()
    elif seleccion == 7:
        print("Que pases un buen dia")
        quit()
    else:
        print("Ingrese un número del 1 al 7.")


while True:
    menu()
