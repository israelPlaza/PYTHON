"""
Pide por consola dos números y un símbolo de operación ( + - * / ) y realiza la
operación indicada mostrando el resultado.
"""

primero= int(input("Primer número: "))
segundo= int(input("Segundo número: "))
signo=  str(input("operacion a realizar [+ - * /]"))

if(signo == "+"):
    print(primero + segundo)
elif(signo == "-"):
    print(primero - segundo)
elif(signo == "*"):
    print(primero * segundo)
elif(signo == "/"):
    print(primero / segundo)