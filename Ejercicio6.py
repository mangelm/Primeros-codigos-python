"""
Queremos hacer un programa que sirva para
a convertir divisas. En primer lugar
el programa nos mostrará el siguiente menú:
 
===================================
  = 1. - Euros a dolares  
    = 2. - Euros a Yenes
   = 3. - Dolares a Euros
   = 4. - Dolares a Yenes
   = 5. - Yenes a Euros
   = 6. - Yenes a Dolares
====================================
= Escoge una opcion de conversion
====================================

Una vez el usuario pulse la tecla correspondiente
en la opción que desea, se mostrará un mensaje
con la conversión elegida, y el programa pedirá
la cantidad de la divisa de origen.
Finalmente el programa calculará la cantidad de
divisas de destino:

===================================
Euros a dolares
Introducir una cantidad de la divisa de origen:
20
===================================
La cantidad de la divisa de destino es:14.25884

http://www.xe.com/es/currencyconverter/
"""
conversor = True


while conversor:
   
   
    print("===================================")
    print("= 1. - Euros a dolares")  
    print("= 2. - Euros a Yenes")
    print("= 3. - Dolares a Euros")
    print("= 4. - Dolares a Yenes")
    print("= 5. - Yenes a Euros")
    print("= 6. - Yenes a Dolares")
    print("====================================")
    divisa = int(input("= Escoge una opcion de conversion: =\n"))
    print("====================================")


    if divisa == 1:
        print("Euros a dolares")
        cantidad=float(input("Introducir una cantidad de la divisa de origen\n"))
        conversion = cantidad * 1.0082742
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
    elif divisa == 2:
        print("Euros a Yenes")
        cantidad=float(input("Introducir una cantidad de la divisa de origen\n"))
        conversion = cantidad * 147.52385
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
   
    elif divisa == 3:
        print("Dolares a Euros")
        cantidad=float(input("Introducir una cantidad de la divisa de origen\n"))
        conversion = cantidad * 0.99201197
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
   
    elif divisa == 4:
        print("Dolares a Yenes")
        cantidad=float(input("Introducir una cantidad de la divisa de origen\n"))
        conversion = cantidad * 146.32887
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
   
    elif divisa == 5:
        print("Yenes a Euros")
        cantidad=float(input("Introducir una cantidad de la divisa de origen"))
        conversion = cantidad * 0.0067789368
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
   
    elif divisa == 6:
        print("Yenes a Dolares")
        cantidad=float(input("Introducir una cantidad de la divisa de origen"))
        conversion = cantidad * 0.0068348686
        print("====================================")
        print("La cantidad de la divisa de destino es:\n", conversion)
        conversor = False
   
   
    else:
        conversor = False

