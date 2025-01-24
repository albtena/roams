import importlib
from importlib.util import find_spec

from app.util import string as St

APP_PATH = "app"
CRUD_PATH = "crud"
MODEL_PATH = "model"
DAO_PATH = "dao"
DTO_PATH = "dto"
DB_PATH = "db"
CACHE_PATH = "cache"
CONTROLLER_PATH = "controller"
SERVICE_PATH = "service"
JSON_PATH = "json"

# REQUEST_PATH = "request"
FUNTIONALITY_PATH = "func"
WEB_PATH = "web"
EXTERNAL_API_PATH = "external_api"


DAO_CLASS = "Dao"
DAO_EXTENSION = "_dao"


def instance_object(
    directory_list, name, package=None, class_name=None, params=None, body=None
):
    """Instancia un objeto dado un directorio, paquete, nombre

    Args:
        directory_list (str): subdirectorios dentro de /app.
        package (str): nombre del paquete dentro del subdirectorio
        name (str): nombre del modulo
    """
    try:
        module_name = St.text_to_snake(name)

        if not class_name:
            module_class = St.text_to_pascal(name)
        else:
            module_class = class_name

        if not package:
            directory_list = [APP_PATH] + directory_list + [module_name]
        else:
            directory_list = [APP_PATH] + directory_list + [package, module_name]

        module_path = St.get_module(directory_list)

        # Intentar encontrar el módulo especificado
        spec = find_spec(module_path)
        if spec is None:
            raise ImportError(f"No se pudo encontrar el módulo: {module_path}")

        # Importar el módulo dinámicamente
        module = importlib.import_module(module_path)

        # Obtener la clase especificada del módulo
        class_object = getattr(module, module_class)

        if params is not None:
            return class_object(*params)

        if body is not None:
            return class_object(**body)

        return class_object()

    except Exception as e:
        print("ERROR: Util object -> instance_object: " + str(e))
        print(module_path)
        return e


def instance_request(segments, params, type=None):
    """Instancia un objeto request

    Args:
        package (str): nombre del paquete dentro de service/request/funtionality/
        name (str): nombre del modulo
    """
    try:
        if not segments:
            return None

        name = segments[-1]

        if not type:
            type = JSON_PATH

        directory_list = [CONTROLLER_PATH, SERVICE_PATH, type]
        directory_list += segments[:-1]

        return instance_object(
            name=name,
            directory_list=directory_list,
            params=params,
        )

    except Exception as e:
        print("ERROR: Util object -> instance_request: " + str(e))
        return e
