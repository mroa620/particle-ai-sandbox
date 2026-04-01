def reynolds_calculator(densidad, velocidad, longitud, dyn_visc):
    #Esta función hace el cálculo del número de Reynolds para saber si el flujo es laminar o turbulento
    resultado = None

    try:
        densidad, velocidad, longitud, dyn_visc = float(densidad), float(velocidad), float(longitud), float(dyn_visc)
        resultado = (densidad * velocidad * longitud) / dyn_visc
    
    except ZeroDivisionError as e:
        print(f"La viscosidad dinámica no puede ser 0. Error: {e}")
    except ValueError as e:
        print(f"Alguna de las variables es un string. Error: {e}")
   
    if not resultado is None:
        return resultado