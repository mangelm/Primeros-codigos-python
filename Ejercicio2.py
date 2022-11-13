"""
Diseña un programa que lea un carácter 
de teclado y muestre por pantalla el 
mensaje ˂˂Es paréntesis˃˃ sólo si el 
carácter leído es un paréntesis abierto 
o cerrado
"""
parentesis = ""

parentesis = input("Introduce un parentesis:\n")

if parentesis == "(" or parentesis == ")":
    print("Es un parentesis")
else:
    print("No es un parentesis")
