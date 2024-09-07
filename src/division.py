def evaluar(dividendo, divisor):
    
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    
    
    es_exacta = (residuo == 0)
    
   
    if es_exacta:
        respuesta = "La división es exacta. \n"
    else:
        respuesta = "La división no es exacta. \n"
    
    respuesta += "Cociente: " + str(cociente) + "\n"
    respuesta += "Residuo: " + str(residuo)
    
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
