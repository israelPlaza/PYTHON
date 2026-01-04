
def imprimir_numeros(n):
    
    def paso(i):
        print(i, end=" ")
        if i < n:
            paso(i+1)
            print(i, end=" ")
    paso(1)

imprimir_numeros(5)
    