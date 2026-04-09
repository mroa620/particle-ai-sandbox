import json
import pathlib
import datetime
import ast

def create_vars():

    config_final = dict()
    metadata = dict()
    physics = dict()
    fluid_properties = dict()
    dimensionless_params = dict()
    solver_settings = dict()
    initial_conditions = dict()
    

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

        except ValueError:
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
            print("El valor de la viscosidad ha der ser un número positivo (Pa*s)")
        except ValueError:
            print("El valor de la viscosidad ha der ser un número positivo (Pa*s)")
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
            print("El valor de la densidad ha der ser un número positivo (kg/m^3)")
        except ValueError:
            print("El valor de la densidad ha der ser un número positivo (kg/m^3)")
    fluid_properties["density"] = density
    physics["fluid_properties"] = fluid_properties

    while True:
        try:
            char_length = input("Introduce el valor de la longitud característica del problema (m): ")
            char_length = float(char_length)

            if char_length > 0:
                break
            else:
                raise ValueError
        
        except TypeError:
            print("El valor de la longitud característica ha der ser un número positivo (m)")
        except ValueError:
            print("El valor de la longitud característica ha der ser un número positivo (m)")
    dimensionless_params["char_length"] = char_length

    while True:
        try:
            ref_velocity = input("Introduce el valor de la velocidad de referencia del problema (m/s): ")
            ref_velocity = float(ref_velocity)

            if ref_velocity > 0:
                break
            else:
                raise ValueError
        
        except TypeError:
            print("El valor de la velocidad de referencia ha der ser un número positivo (m/s)")
        except ValueError:
            print("El valor de la velocidad de referencia ha der ser un número positivo (m/s)")
    dimensionless_params["reference_velocity"] = ref_velocity
    physics["dimensionless_params"] = dimensionless_params


    while True:
        try:
            time_step = input("Introduce el time-step de la simulación (s): ")
            time_step = float(time_step)

            if time_step > 0:
                break
            else:
                raise ValueError
        except TypeError:
            print("El time step ha der ser un número positivo (s)")
        except ValueError:
            print("El time step ha der ser un número positivo (s)")
    solver_settings["time_step"] = time_step

    while True:
        try:
            t_total = input("Introduce el tiempo total de simulación (s): ")
            t_total = float(t_total)

            if t_total > 0:
                break
            else:
                raise ValueError
        except TypeError:
            print("El tiempo total de la simulación ha der ser un número positivo (s)")
        except ValueError:
            print("El tiempo total de la simulación ha der ser un número positivo (s)")
    solver_settings["total_time"] = t_total

    while True:
        try:
            particle_id = input("Introduce el número de id de la partícula inicial: ")
            particle_id = float(particle_id)
            break

        except TypeError:
            print("El número de id de la partícula ha der ser un número")
    initial_conditions["particle_id"] = particle_id

    while True:
        try:
            pos_initial = []
            pos_initial = input("Introduce la posición inicial de la partícula [ (m), (m)]: ")
            pos_initial = ast.literal_eval(pos_initial)

            if not isinstance(pos_initial, list):
                raise TypeError
            elif len(pos_initial) != 2:
                raise ValueError
            elif not all(isinstance(x, (int, float)) for x in pos_initial):
                raise TypeError
            break

        except (ValueError, TypeError, SyntaxError):
            print("La posición ha de indicarse en una lista de coordenadas [x, y] en (m)")
    
    initial_conditions["pos_initial"] = pos_initial

    while True:
        try:
            vel_initial = []
            vel_initial = input("Introduce la velocidad inicial de la partícula [ (m), (m)]: ")
            vel_initial = ast.literal_eval(vel_initial)
            
            if not isinstance(vel_initial, list):
                raise TypeError
            elif len(vel_initial) != 2:
                raise ValueError
            elif not all(isinstance(x, (int, float)) for x in vel_initial):
                raise TypeError
            
            break

        except (ValueError, TypeError, SyntaxError):
            print("La velocidad ha de indicarse en una lista de coordenadas [x, y] en (m)")

    initial_conditions["vel_initial"] = vel_initial

    config_final["metadata"] = metadata
    config_final["physics"] = physics
    config_final["solver_settings"] = solver_settings
    config_final["initial_conditions"] = initial_conditions

    return config_final


print(create_vars())