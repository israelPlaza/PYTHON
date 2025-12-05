"""
Define una funci´on recursiva contar digitos(n) que cuente los d´ıgitos de un n´umero pasado
por par´ametro.
"""

def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

print(contar_digitos(2045))