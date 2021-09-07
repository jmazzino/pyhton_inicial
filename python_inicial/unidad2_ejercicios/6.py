print("Ingrese el primer valor: ")
val1 = input("->: ")
print("Ingrese el segundo valor: ")
val2 = input("->: ")
val3 = int(val1) + int(val2)

dic = {1: val1, 2: val2, 3: val3}

print("################")
print("Lista de valores")
for key in dic:
    print(key, ":", dic[key])
