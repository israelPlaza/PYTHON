""" 
Escriba un algoritmo que reciba como entrada las longitudes de los dos catetos a y b
de un triángulo rectángulo y que entregue como salida el largo de la hipotenusa c del
triángulo a través de la aplicación del teorema de Pitágoras: c2=a2+b2 

"""
cateto_a = float(input("Escriba el primer cateto: "))
cateto_b=float(input("Escriba el segundo cateteto: "))
hipotenusa= float(((cateto_a**2)+(cateto_b**2))**0.5)

print(f"La hipotenusa es {hipotenusa} " )