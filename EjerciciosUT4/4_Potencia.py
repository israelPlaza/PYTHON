def potencia(n, exponente):
    if exponente ==0:
        return 1
    
    return n * potencia(n, exponente -1)

print(potencia(3,2))