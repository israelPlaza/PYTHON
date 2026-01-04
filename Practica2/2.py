
def sumar(n):
    if n == 1:
        return 1
    else:
        return n + sumar(n-1)

print(sumar(5))