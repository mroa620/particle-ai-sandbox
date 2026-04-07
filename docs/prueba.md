import csv
import json

def loadcsv(file_path):

    try:
        with open(file_path, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
        
            csv_import = []
            for fila in lector:
                csv_import.append(fila)
            return csv_import
    
    except FileNotFoundError:
        print("Archivo no encontrado")



def validate_structure(row, required_fields):
    
    if not isinstance(row, dict):
        raise TypeError
    if not isinstance(required_fields, list):
        raise TypeError
        
    for r in required_fields:
        if not r in row:
            raise KeyError
    return True


def sanitize_data(row, fields_to_float):
    
    if not isinstance(row, dict):
        raise TypeError
    if not isinstance(fields_to_float, list):
        raise TypeError   
    
    floats_converted = row.copy()


    for f in fields_to_float:
        try:
            raw_value = row[f]
            raw_value = float(raw_value)
        
        except ValueError:
            raw_value = None
        
        floats_converted[f] = raw_value

    return floats_converted



def rename_sensors(row, name_map):

    if not isinstance(row, dict):
        raise TypeError
    
    if not isinstance(name_map, dict):
        raise TypeError
    
    row_translated = dict()

    for r in row:

        new_key = name_map.get(r, r)
        row_translated[new_key] = row[r]

    return row_translated



def is_valid_row(row, critical_fields):

    if not isinstance(row, dict):
        raise TypeError

    if not isinstance(critical_fields, list):
        raise TypeError
    
    #Buscar los valores de la lista critical_fields en las llaves de row

    for c in critical_fields:

        if not c in row:
            raise KeyError
        elif row[c] is None:
            return False
    
    return True 


def process_physical_data(data_list, config):
    
    if not all(isinstance(item, dict) for item in data_list):
        raise TypeError

    if not isinstance(config, dict):
        raise TypeError 
    
    final_data = []

    for d in data_list:

        try:

            validate_structure(d, config["required_fields"])

            fila_procesada = sanitize_data(d, config["fields_to_float"])

            fila_traducida = rename_sensors(fila_procesada, config["name_map"])

            if is_valid_row(fila_traducida, config["critical_fields"]):
                final_data.append(fila_traducida)


        except TypeError as error:
            print(f"El formato de los datos de entrada no es el correcto: {error}")
        except KeyError as key_error:
            print(f"Alguna de las claves requeridas no existe en el csv: {key_error}")

    return final_data


def save_data(ruta, variable_datos):
    
    with open(ruta, 'w', encoding='utf-8') as archivo:
        escritor = json.dump(variable_datos, archivo, indent=4)




# [BLOQUE DE CONFIGURACIÓN MAESTRO]
CONFIG = {
    "required_fields": ["id_particle", "x", "y", "velocity"], # Deben estar en el CSV
    "fields_to_float": ["x", "y", "velocity"],               # Se convertirán a números
    "name_map": {"x": "pos_x", "y": "pos_y"},                # Renombrado para la IA
    "critical_fields": ["pos_x", "pos_y", "velocity"]        # No pueden ser None
}

# [BLOQUE DE ORQUESTACIÓN]
if __name__ == "__main__":
    # 1. Definimos las rutas
    entrada = "C:/Users/mroa6/Desktop/physical_data_extractor/simulacion_particulas.csv"
    salida = "C:/Users/mroa6/Desktop/physical_data_extractor/datos_limpios.json"

    print("--- Iniciando Physical Data Extractor v0 ---")

    # 2. Entrada: Cargamos los datos del disco
    datos_brutos = loadcsv(entrada)

    if datos_brutos:
        # 3. Cerebro: Procesamos los datos usando nuestra pipeline
        datos_procesados = process_physical_data(datos_brutos, CONFIG)

        # 4. Salida: Guardamos el resultado final
        save_data(salida, datos_procesados)

        print(f"Éxito: Se han procesado {len(datos_procesados)} filas válidas.")
    else:
        print("Error: No se pudieron cargar los datos iniciales.")