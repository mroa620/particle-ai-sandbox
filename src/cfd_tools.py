import math
import warnings

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


def validate_reynolds(Re):
    
    validation = False
    if Re is None:
        print ("Error: No se recibión un valor de Reynolds válido")

    elif Re < 2000:
        print(f"OK: Re={Re:.0f}. El flujo es laminar")
        validation = True
        
    elif 2000 <= Re <= 4000:
        warnings.warn(f"AVISO TÉCNICO: Re={Re:.0f}. El flujo es transitorio - El solver puede ser inestable")
        validation = True
        
    else:
        print(f"OK: Re={Re:.0f}.El flujo es turbulento")
        validation = True
    
    
    return validation


def froude_calculator(velocidad, longitud, gravedad=9.81):
    #La función de Froude calcula la importancia relativa entre el término de convección forzada y convección natural (afectada por la gravedad)
    
    velocidad, longitud = float(velocidad), float(longitud)
    resultado = None
    try:
        if longitud < 0:
            raise ValueError("La longitud no puede ser negativa")
        else:
            resultado = velocidad / (math.sqrt(gravedad * longitud))
    
    except ZeroDivisionError as e:
        print(f"La longitud no puede ser 0. Error: {e}")
    
    except ValueError as e:
        print(f"La raíz de un número negativo da error: {e}")

    if not resultado is None:
        return resultado

def froude_validation(Fr):

    validation = True

    if Fr is None:
        print("Fr no es válido")
        validation = False

    elif Fr < 1:
        print(f"Fr = {Fr:.02f}. El régimen es subcrítico (flujo lento).")
    
    elif Fr == 1:
        print(f"AVISO TÉCNICO: Fr = {Fr:.02f}. El régimen es crítico - El solver puede ser inestable.")
    
    else:
        print(f"Fr = {Fr:.02f}. El régimen es supercrítico (flujo rápido/torrencial).")
    
    return validation
