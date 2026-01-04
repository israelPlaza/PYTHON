def imprimir_numeros(n):
    if n ==0 :
        return
    imprimir_numeros(n -1)
    print(n, end=" ")
    
imprimir_numeros(3)