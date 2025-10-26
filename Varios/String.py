print("hola"[-1])
print("hola"[1:3])
print("hola"[::-1])
print ("a" in "hola")


#Cadena de texto
palabra = "holaaa"
palabra.count
contador=0

for letra in palabra:
    cont=0
    for i in palabra:
        if i==letra:
            cont+=1
            print(cont)
            
            
            
            
#te diga si la cadena de texto tiene vocales

palabra= "palabra"

for i in palabra:
    if(i =="a" or i=="e" or i=="i" or i=="o" ):
        print("si tienes vovales")
            