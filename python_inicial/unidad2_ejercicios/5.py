print("Ingrese el primer valor: ")
val1 = input("->: ")
print("Ingrese el segundo valor: ")
val2 = input("->: ")
val3 = int(val1) + int(val2)

lista = []
lista.append(int(val1))
lista.append(int(val2))
lista.append(val3)
print("################")
print("Lista de valores")
for x in range(0, len(lista)):
    print(lista[x])
