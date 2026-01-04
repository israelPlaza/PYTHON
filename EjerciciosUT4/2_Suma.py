def sumar(n):
    if n ==0 or n ==1:
        return 1
    return n + sumar(n -1)

print(sumar(4))