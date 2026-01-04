def sumar_elementos_lista(lista, profundidad=1):
    suma = 0
    for elemento in lista:
        
        if isinstance(elemento, list):
            suma += sumar_elementos_lista(elemento, profundidad + 1)
        
        else:
            suma += elemento ** profundidad
    return suma

datos = [1, [2, 3], 2] 
print(sumar_elementos_lista(datos))