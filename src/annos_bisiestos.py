def evaluar(anno):
    if anno % 400 == 0:
        return f"{anno} es bisiesto"
    elif anno % 100 == 0:
        return f"{anno} no es bisiesto"
    elif anno % 4 == 0:
        return f"{anno} es bisiesto"
    else:
        return f"{anno} no es bisiesto"

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
