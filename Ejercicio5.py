"""
Un programa leerá tres números
 por teclado. La salida del programa
 será sacar por pantalla si el usuario
  ha introducido estos números por
  orden de menor a mayor o no.
ej:
● si el usuario entra 1,4,6 el programa
   dirá “ números en orden”
● si el usuario entra 5,7,3 el
    programa dirá " números desordenados"

"""

numero = int(input("Introduce un número\n"))
numero2 = int(input("Introduce otro número\n"))
numero3 = int(input("Introduce un último número\n"))

if numero < numero2 and numero2 < numero3:
    print("Los numeros estan ordenados")
else:
    print("Los numeros estan desordenados")

""" 
if (numero<numero2 and numero<numero3):
    print ("Los números están ordenados")
else:
    print ("Los números están desordenados") 
"""

