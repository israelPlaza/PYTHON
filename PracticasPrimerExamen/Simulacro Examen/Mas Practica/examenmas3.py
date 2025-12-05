dato=1

dato =int(input("escribe un numero psotivio: "))
while dato <=0:
    dato =int(input("escribe un numero psotivio: "))
    if dato <=0:
        print("Error, intentalo de nuevo")

for x in range(1,11):
    print(f"{dato} x {x} = {dato*x}")