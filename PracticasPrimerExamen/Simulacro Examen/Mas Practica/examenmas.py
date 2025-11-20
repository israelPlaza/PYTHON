notas = [4,8,9,5,10]
notas_aprobadas = [nota for nota in notas if nota >=5]
print(notas_aprobadas)


frase = " pYtHoN-eS-gEnIaL "
frase_bien = frase.strip()
frase_bien2 =frase_bien.lower()
frase_bien3 = frase_bien2.replace("-"," ")
frase_bien4 = frase_bien3.capitalize()
print((frase_bien4))


inventario = {"raton": 10, "teclado": 5, "monitor": 2}

#Auricualres

if inventario.get("auriculares") ==None :
    print("No hay stock")

#aumento  de ratones

inventario["raton"]=15
print("ratones: ",inventario["raton"])

#Añadir producto

inventario["impresora"]=3
print("impresora ",inventario["impresora"])


for producto,stock in inventario.items():
    print(f"Productos {producto} Stock: {stock}")
    
    
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 4},
    {"nombre": "Marta", "nota": 9},
    {"nombre": "Pepe", "nota": 5}
]
# lista nueva solo de aprobados
nota_apro = [alumno["nombre"] for alumno in alumnos if alumno["nota"] >=5]
print(nota_apro)