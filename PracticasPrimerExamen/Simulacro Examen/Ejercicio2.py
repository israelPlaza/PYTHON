
dato=0
suma=0
contador=0

while suma <=42 :
    dato=input("Escribe el número ")
    contador+=1
    try:
        dato=int(dato)
        suma+=dato
    except:
        suma+ 0

print(f"Has necesitado {contador} para llegar a {suma}")