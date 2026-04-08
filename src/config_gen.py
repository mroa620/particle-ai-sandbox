import json
import pathlib

def create_vars():
    case_name = input("Introduce el nombre del caso: ")
    while True:
        viscosity = input("Introduce el valor de la viscosidad: ")
    density = input("Introduce el valor de la densidad (kg/m^3): ")
    simulation_type = input("Es una simulación 2D o 3D?: ")

    if simulation_type in ["2D","2d"]:
        position = (""
        "x", "y")
        velocity = ("v_x", "v_y")
    elif simulation_type in ["3D","3d"]:
        position = ("x", "y", "z")
        velocity = ("v_x", "v_y", "v_z")
    else:
        print("No has indicado el tipo de simulación.")
        raise ValueError
           
    #id_particula
    t_total = input("Introduce el tiempo total de simulación: ")
    time_step = input("Introduce el time-step de la simulación: ")