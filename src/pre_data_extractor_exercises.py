#Ej. 1 - El Vigilante de Columnas:
def validate_structure(row, required_fields):
    
    if not isinstance(row, dict):
        raise TypeError
    if not isinstance(required_fields, list):
        raise TypeError
        
    for r in required_fields:
        if not r in row:
            raise KeyError
    return True


#Ej. 2 - El Purificador de Datos:
def sanitize_data(row, fields_to_float):
    
    if not isinstance(row, dict):
        raise TypeError
    if not isinstance(fields_to_float, list):
        raise TypeError   
    
    floats_converted = dict()


    for f in fields_to_float:
        try:
            raw_value = row[f]
            raw_value = float(raw_value)
        
        except ValueError:
            raw_value = None
        
        floats_converted[f] = raw_value

    return floats_converted


#Ej. 3 - El Traductor de Sensores:

def rename_sensors(row, name_map):

    if not isinstance(row, dict):
        raise TypeError
    
    if not isinstance(name_map, dict):
        raise TypeError
    
    row_translated = dict()

    #Obtener llaves de row
    #Revisar llaves coincidentes con mapa_traducción
    #Si no existe la llave en mapa_traducción se mantiene el nombre viejo
    #El valor de esa llave del mapa_traducción pasa a ser la clave de row_translated
    for r in row:

        if r in name_map:
            translation = name_map[r]
            row_translated[translation] = row[r]
        
        else:
            row_translated[r] = row[r]
    
    return row_translated

#Ej. 3 mas pythonico - El Traductor de Sensores:
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


#Ej. 4 - El Filtro de Realidad:
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


#Ej. 5 - La Micro-Pipeline (Integración Final):
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
        