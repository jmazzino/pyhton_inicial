""" 
Ejercicio 2 - Mensajes Secretos

Desarrollar una aplicación que permita cifrar un mensaje simple, es decir, el mensaje sólo podrá contener letras mayúsculas y minúsculas entre la A y la Z.
La aplicaicón deberá permitir ingresar un número entero que indique el corrimiento a realizar al alfabeto antes de cifrar el mensaje. 
Ejemplo:
    mensaje: Mayday! Mayday!
    corrimiento: 4
    mensaje cifrado: Qechec! Qechec! """

import random

""" def cifrar(texto,clave):
  longitud=len(texto)
  abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","!"]
  longitud2=len(abc)
  for i in range (0,longitud): #Bucle para recorrer el texto
    for pos in range (0,longitud2): #Bucle para recorrer el Abecedario
      if texto[i]==abc[pos]: #comparo las letras una por una
        pos_abc=pos+int(clave) #Me desplazo en el abecedario en función a la clave
        if pos_abc < longitud2:
           print(abc[pos_abc],end="")
        if pos_abc > longitud2 : #En el caso de que me pase del abecedario, calculo el modulo
           print(abc[pos_abc%longitud2],end="")
    else:
      print(end="") """

#FS
#Ejercicio 2 - Mensajes Secretos

#Desarrollar una aplicación que permita cifrar un mensaje simple, es decir, el mensaje sólo podrá contener letras mayúsculas y minúsculas entre la A y la Z.
#La aplicaicón deberá permitir ingresar un número entero que indique el corrimiento a realizar al alfabeto antes de cifrar el mensaje. 
#Ejemplo:
#    mensaje: Mayday! Mayday!
#    corrimiento: 4
#    mensaje cifrado: Qechec! Qechec!

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def fn_corrimiento(corrimiento=4, msg="Mayday! Mayday!"):
    aux = abc[corrimiento:] + abc[:corrimiento]
    print("original: ", abc)
    print("modi: ", aux)

    codificado = ""
    for m in msg:
        try:
            i = abc.lower().index(str(m).lower())
            if not m.isupper():
                codificado += aux[i].lower()
            else:
                codificado += aux[i]
        except:
            codificado += m
    return codificado



codificado = fn_corrimiento()
print(codificado)
    
