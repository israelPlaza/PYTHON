# while lectura != 42 and suna %5
"""""
lectura = 0
suma = 0

while not(lectura == 42 or suma%5 == 00):
    lectura= int(input("Escribe un número: "))
    suma = suma + lectura
    
    """
    
 #muestra las tablas de multiplicar haasta que algunos de los resultados sea 26
"""""
numero = 1
tabla=1
resultado= 0

while resultado != 26:
    resultado=tabla*numero
    print(f"{tabla} x {numero} = {resultado}")
    numero+=1
    if numero ==11:
        numero=1
        tabla+=1
    """""    
#lea un numero y te diga la longitud        

contador= 0
division=8
numero = int(input("escribe numero "))
while numero > 0:
    numero= int(numero/10)
    contador+=1
 

print(f"tu numero es de longitud {contador}")    
    