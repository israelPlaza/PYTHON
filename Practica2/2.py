"""
Define una funci´on recursiva sumar(n) para sumar todos los n´umeros desde 1 hasta n (1 + 2 +
. . . + n).
"""
def sumar(n):
    if n == 1:
        return 1
    else:
        return n + sumar(n-1)

print(sumar(5))