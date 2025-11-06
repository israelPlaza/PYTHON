
#Variables
dato=""
contador_int = 0
contador_float = 0
contador_bool = 0
contador_str = 0

#Programa
    #El while para que itere hasta que se escriba salir
while (dato.lower()!="salir" ):
    print("Introduce valores por teclado. Escribe 'salir' para terminar.")
    dato=input()
    
    if(dato.lower() == "true"):#if para saber si es true
        print(f"Entrada: {dato}")
        conversor=(bool)(dato)
        print(f"Tipo detectado: {conversor}")
        print(f"Valor convertido: {conversor}")
        contador_bool +=1
    elif(dato.lower() == "false"):#if para saber si es fasle
        print(f"Entrada: {dato}")
        conversor=False
        print(f"Tipo detectado: {conversor}")
        print(f"Valor convertido: {conversor}")
        contador_bool +=1
    else:
        try:# El try para que intente ceonvertir a int
            conversor= int(dato)
            print(f"Entrada: {dato}")
            print(f"Tipo detectado: int")
            print(f"Valor convertido: {conversor}")
            contador_int+=1
        except ValueError:#Si no puede pasa al siguiente try
            try:# El try para que intente ceonvertir a float
                conversor= float(dato)
                print(f"Entrada: {dato}")
                print(f"Tipo detectado: float")
                print(f"Valor convertido: {conversor}")
                contador_float +=1
            except ValueError:#la última excepción string, por que sabemos que al pasar el input siempre es String
                if(dato.lower() != "salir"):
                    print(f"Entrada: {dato}")
                    print(f"Tipo detactado: String")
                    print(f"Valor convertido: {dato}")
                    contador_str += 1
            
    print() #Escrbimos un salto para mostrar el total de forma mas visual

#para finalizar mostramos el total
print("Has utilizado:")
print(f"int: {contador_int}")
print(f"float: {contador_float}")
print(f"bool: {contador_bool}")
print(f"str: {contador_str}")
