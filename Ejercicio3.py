"""
 Diseña un programa que, dado un número entero, 
 determine si éste es el doble de un número 
 impar. (Ejemplo: 14 es el doble de 7, que es 
 impar.)
"""
num = 0
doble = 0

num = int(input("Introduce numero:"))

if (num % 2 == 0):
    doble = num / 2
    if (doble%2 == 1):
        print("el doble de este numero es ", doble, "impar")
    else:
        print("Es el doble pero no es impar")

else:
    print ("El numero no tiene doble")
