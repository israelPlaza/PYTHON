lista = [1, 2, 3, 4]
suma_total = sum(lista)

resultado= list(filter(lambda x : suma_total % x ==0 , lista))

print(resultado)