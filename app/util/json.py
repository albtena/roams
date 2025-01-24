import json


def merge_json(obj1, obj2):
    """
    Merge two JSON objects recursively.
    """
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        merged = obj1.copy()
        for key, value in obj2.items():
            if key in merged:
                merged[key] = merge_json(merged[key], value)
            else:
                merged[key] = value
        return merged
    elif isinstance(obj1, list) and isinstance(obj2, list):
        return obj1 + obj2
    elif obj1 != obj2:
        # If both objects are not dictionaries or lists and are different,
        # return a list containing both values
        return [obj1, obj2]
    else:
        # If both objects are not dictionaries or lists and are the same,
        # return either one
        return obj1


def str_to_json(str_json) -> json:
    cleaned_string = str_json.strip("'")
    parsed_json = json.loads(cleaned_string)

    return parsed_json


def remove_repeated_entries(dict, key_filter):
    try:
        unique_entries = []
        keys = []

        for attempt in dict:
            key = attempt[key_filter]
            # Verificar si la clave ya ha sido encontrada
            if key not in keys:
                # Si la clave es nueva, agregar el JSON a la lista filtrada y añadir la clave al conjunto
                unique_entries.append(attempt)
                keys.append(key)

        return unique_entries

    except Exception as e:
        print("ERROR: Util json -> remove_repeated_entries: " + str(e))


def extract_objects_from_dict(dict_: dict, object_target):
    objects = []

    for value in dict_.values():
        if isinstance(value, dict):
            # Si es otro diccionario, llamamos recursivamente
            objects.extend(extract_objects_from_dict(value, object_target))
        elif isinstance(value, object_target):
            # Si es un objeto object_target, lo añadimos a la lista
            objects.append(value)

    return objects


def rename_key_in_list_of_dicts(list_of_dicts, old_key, new_key):
    """
    Renames a key in a list of dictionaries.

    Parameters:
    - list_of_dicts (list): List of dictionaries where key needs to be renamed.
    - old_key (str): Old key name.
    - new_key (str): New key name.

    Returns:
    - list: Modified list of dictionaries with the key renamed.
    """
    for item in list_of_dicts:
        if old_key in item:
            item[new_key] = item.pop(old_key)
    return list_of_dicts


def combine_entries(list_, ident, key_to_combine):
    combined_dict = {}

    for element in list_:
        key = element[ident]

        if key not in combined_dict:
            combined_dict[key] = element
            combined_dict[key][key_to_combine] = [element[key_to_combine]]
        else:
            combined_dict[key][key_to_combine].append(element[key_to_combine])

    # Convert the dictionary back to a list
    return list(combined_dict.values())
