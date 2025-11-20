valores =[]
dato =""
while dato.lower() != "fin":
    dato= input("Escribe el dato ")
    valores.append(dato)
    
valores.remove("fin")
print(valores)
