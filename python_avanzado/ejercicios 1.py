""" Ejercicios clase 1

Ejercicio 1 - Casino

Estas a cargo de la seguridad del casino, y hay un ladron dando vueltas que intenta llevarse el dinero!
Para evitar que este ladron se lleve el dinero, tiene que haber un guardia en su camino.

Desarrollar una aplicación que permita generar una lista (máximo 15 caracteres)
que representa el piso del casino con el siguiente formato:

Ejemplo de entrada:
x x x x G x $ x L

Donde:  x - Espacio vacio
		$ - Dinero
		G - Guardia
		L - Ladron

El piso del casino siempre contendra un solo $ y un solo L, mientras que puede haber más de 1.

En caso de que no haya un guardia en el camino del ladron, mostrar el mensaje "ALARMA!!", en caso contrario, se debe imprimir "OK".

Salida Esperada para el ejemplo:
ALARMA """

import random

def piso(largo=15):
    piso = ["x" for x in range(largo)]
    pos= random.sample(range(1, largo) ,4)
    piso[pos[0]]= "$"
    piso[pos[1]]= "L"
    piso[pos[2]]= "G"
    piso[pos[3]]= "G"

    return "".join(piso)

def veri(piso):
    print(*piso) 
    ladron = piso.find('L')
    dinero = piso.find('$')
    if (ladron < dinero):
        return piso[ladron:dinero].find('G') == -1
    else:
        return piso[dinero:ladron].find('G') == -1

for x in range(40):
    print("ALARMA" if veri(piso(15)) else "OK")
    
