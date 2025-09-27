""" 
    escribir a has que acabeen "fin"  lowe()  o upper()
    
"""
    
palabra= str(input("Escriba una palabra: "))
while palabra .upper()!="FIN" :
    print(palabra)
    palabra= str(input("Escriba una palabra: "))
    print(palabra)
    
    
    
    """hasta que suma los numeros sean divisibles por 5 o se 
    introducza el numero 42 y en cada ireacion la suma
    de los numeros introducidos"""
suma=1
anterior=1
while suma%5!=0 or suma== 42:
    print(f"{suma} + {anterior} = {suma + anterior}")
    anterior=suma
    suma= int(input("escriba número "))
    print(f"sdasd{suma}")