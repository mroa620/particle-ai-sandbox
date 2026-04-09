import json
import pathlib
import datetime

def create_vars():

    config_final = dict()
    metadata = dict()
    physics = dict()
    settings = dict()
    fluid_properties = dict()
    dimensionless_params = dict()

    while True:
        try:
            case_name = input("Introduce el nombre del caso: ")
            if case_name == "":
                raise ValueError
            else:
                break
        
        except ValueError:
            print("Es obligatorio escribir un nombre para el caso.")
    metadata["project_name"] = case_name    
    
    while True:
        try:
            user_name = input("Nombre de quién registra la simulación: ")
            if user_name == "":
                raise ValueError
            else:
                break
        except ValueError:
            print("Es obligatorio escribir un nombre de autor del proyecto.")
    metadata["author"] = user_name    
    
    while True:
        try:
            version = input("Introduce el número de versión del proyecto: ")
            version = float(version)
            break

        except TypeError:
            print("La versión del proyecto ha der ser un número")
    metadata["version"] = version

    date = datetime.date.today()
    date = str(date)
    metadata["date"] = date

    while True:
        try:
            viscosity = input("Introduce el valor de la viscosidad dinámica (Pa*s): ")
            viscosity = float(viscosity)

            if viscosity > 0:
                break
            else:
                raise ValueError
        
        except TypeError:
            print("El valor de la viscosidad ha der ser un número positivo")
        except ValueError:
            print("El valor de la viscosidad ha der ser un número positivo")
    fluid_properties["viscosity"] = viscosity

    while True:
        try:
            density = input("Introduce el valor de la densidad (kg/m^3): ")
            density = float(density)

            if density > 0:
                break
            else:
                raise ValueError
        
        except TypeError:
            print("El valor de la densidad ha der ser un número positivo")
        except ValueError:
            print("El valor de la densidad ha der ser un número positivo")
    fluid_properties["density"] = density

           

    #id_particula
    t_total = input("Introduce el tiempo total de simulación: ")
    time_step = input("Introduce el time-step de la simulación: ")

    return