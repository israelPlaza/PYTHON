#Escribí un programa para solicitar al usuario tres números y mostrar en pantalla
# al menor de los tres. 
"""
primero=0
segundo=0
tercero=0

primero=int((input("Escriba el primer número: ")))
segundo=int((input("Escriba el segundo número: ")))
tercero=int((input("Escriba el tercero número: ")))

if primero >segundo and primero > tercero:
    print("Primero es mayor ",primero)
elif segundo > primero and segundo > tercero:
    print("Segundo es mayor ", segundo)
else:
    print("Tercero es mayor ", tercero)   
"""
    
"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de
piezas a procesar y luego ingrese la longitud de cada perfil;
sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30
son aptas.
Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
"""
piezas=0
longitud=0
contador=0

piezas=int(input("¿Cuántas piezas necesitas? "))

for i in range(piezas):
    longitud= float(input("¿ De qué tamaño las necesita? "))
    if longitud > 1.20 and longitud < 1.30 :
        contador+=1

print("El número de piezas válidas es: ",contador)        
