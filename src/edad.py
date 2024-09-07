from datetime import datetime
def evaluar(dia, mes, anno):
     try:
        fecha_nacimiento = datetime(anno, mes, dia)
    except ValueError:
        return "Fecha de nacimiento inválida."
    
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    
    
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
