"""
Define una funci´on recursiva factorial(n) que calcule el factorial de n
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))