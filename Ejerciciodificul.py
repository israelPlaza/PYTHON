### sorted
lista_tupla = [(1,2,3), (4,-3,6), (7,8,9)]

print("lista ordenada")
print(sorted(lista_tupla,key=lambda x: x[0]*x[1],reverse=True))

print("lista original")
print(lista_tupla)

### filter
lista2=[]

for tupla in lista_tupla:
    if tupla[0]>=0:
        lista2.append(tupla)

print("lista original")
print(lista_tupla)
print("lista filtrada")
print(lista2)

print("lista filtrada con filter")
print(list(filter(lambda x: x[0]>=0,lista_tupla)))
