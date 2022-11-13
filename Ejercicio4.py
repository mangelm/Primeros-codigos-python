"""
Un instalador de red cobra según horas 
trabajadas y metros de cable instalados. 
Asumiremos que el precio por hora son 
30€ la hora y el precio por metro del 
cable es 0,5€ sin IVA. Estas dos 
cantidades son fijas (CONSTANTES).

El programa deberá pedirnos:
● las horas trabajadas
● el número de metros instalados
● nos sacará por pantalla (Sacar el 
total de las horas y el coste material 
con iva):
● el precio bruto del trabajador es ....
● el precio del material con IVA es ....
"""


precio_hora = 30
metro_cable= 0.50

horas_trabajadas = int(input("¿Cuantas horas has trabajado?\n"))
cable_instado = float(input("¿Cuantos metros de cable has instalado?\n"))

horas_totales = precio_hora * horas_trabajadas
precio_total_cable = metro_cable * cable_instado * 1.21

print("El precio bruto del trabajador es:",horas_totales,"euros")
print("El precio del material con el IVA es:",precio_total_cable,"euros")
