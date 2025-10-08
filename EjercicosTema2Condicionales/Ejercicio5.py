"""
La empresa Empre S.A. evalúa el rendimiento mensual del personal laboral del
departamento de comercio a partir de la cantidad de nuevas personas que han decidido
subscribirse a nuestros servicios. El incremento del salario mensual es: 0.1 si se han
captado 10% y 0.25 si se han captado 20 o más.
Desarrolla un programa que reciba por consola la cantidad de clientes captados este
mes y tu salario y te muestre por pantalla cuanto vas a cobrar a partir del
rendimiento mensual.
"""

clientes = int(input("Número de clientes: "))
salario = int(input("Salario base: "))

if(clientes >=10 and clientes <20):
    print(f"Salario actualizado es 0.1: {(salario* 0.1)+salario}€")
elif(clientes >=20):
    print(f"Salario actualizado es 0.25: {(salario*0.25)+salario}€")
    
else:
    print("Salario no actualizado ",salario,"€")
    

