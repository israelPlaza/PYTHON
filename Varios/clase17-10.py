lista =[1,2,3,4,5,6]
print(lista)
print(lista[::-1])

diccionario={}
cadena ="patata"
for i in cadena:
    if i in diccionario:
        diccionario[i] = diccionario[i]+1
    else:
        diccionario[i]=1

print(diccionario)

clave = input("clave:")
valor = input("valor")
aaa={clave:valor}
print(aaa)

#lea una frase por teclado y te cunete cuantas veces aparece la vocal

vocales = {"a": 0,"e":0,"i":0,"o":0,"u":0}

frase= input("Escribe una frase")

for i  in frase:
    if i in vocales:
        vocales[i]+=1

print(vocales)


#Lea un número por teclado y te diga que números le compoenen
#ejemplo leo el 12341
#resultado : 1:1

numero= input("Escribe un nuúmero")
diccionario_numero={}
for i in numero:
    if i in diccionario_numero:
        diccionario_numero[i] = diccionario_numero[i]+1
    else:
        diccionario_numero[i]=1

print(diccionario_numero)

#si la palabra tiene 6 letras lo añada a la clave: 6l
#si la palabra tiene 3 vocales lo añada a la clave: 3v

d= {"6l":[],"3v": []}

palabras = input("Escriba tu palabra:")
vocales= "aeiou"
for i in palabras.lower():
    if len(palabras)==6:
        d["6l"].append(palabras)

    if nvocale >3:
        nvocales +1=1


print(d)