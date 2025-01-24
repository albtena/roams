from fastapi.encoders import jsonable_encoder

from pydantic import ValidationError

from app.core.response.response import JSONResponseKeys
from app.core.response.error import ResponseError

from app.util import string as St


class MissingParameterError(Exception):
    """Excepción para parámetros obligatorios faltantes."""

    pass


class UseCaseKeys:
    NO_MORE_DATA = "no_more_data"
    DATA_AVAILABLE = "data_available"
    NO_DATA = "no_data"


# Definimos la metaclase
class UseCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        # Iteramos sobre todos los atributos de la clase
        for attr_name, attr_value in attrs.items():
            # Verificamos si el atributo es un método y si su nombre empieza con "ntf"
            if callable(attr_value) and attr_name.startswith("ntf"):

                # Aqui vendria cualquier decorador que queremos que se ejecute cuando
                # un metodo comience por ntf, por ejemplo para notificar el resultado de la ejecución

                # attrs[attr_name] = notify(attr_value)
                pass

        return super().__new__(cls, name, bases, attrs)


class UseCase(metaclass=UseCaseMeta):
    LIMIT_QUERY = "limit"  # Key para determinar cuantas filas por consulta
    PAGE_QUERY = "page"  # Key para determinar el numero de paquete de filas

    # Limite de filas maximo para una query fraccionada
    MAX_QUERY_LIMIT = 20

    def __init__(self, id_funtionality):
        self.id_funtionality = id_funtionality

    def validate_content(self, content, pydantic_class):
        try:
            # Valida y filtra el diccionario
            data = pydantic_class(**content)
            return data  # Muestra solo los atributos válidos

        except ValidationError as e:
            errors = e.errors()  # Lista de errores
            error_messages = [
                f"{error['loc'][0]}: {error['msg']}" for error in errors
            ]  # Mensajes detallados

            # Construye un mensaje de error general
            error_message = f"Missing or invalid fields:  {'; '.join(error_messages)}"
            ResponseError.response_error(description=error_message)

    def get_mandatory_value_from_dict(self, content, key, firts_item=False):
        try:
            if isinstance(content[key], list) and firts_item:
                return content[key][0]
            else:
                return content[key]

        except (KeyError, IndexError) as e:
            if key is not None:
                error_msg = f"Mandatory parameter '{key}' not found"
            else:
                error_msg = f"Mandatory parameter not found"

            return ResponseError.response_error(description=error_msg)
            # raise MissingParameterError(error_msg + str(key)) from e

    def get_posible_value_from_dict(self, content, key, firts_item=False):
        try:
            if isinstance(content[key], list) and firts_item:
                return content[key][0]
            else:
                return content[key]

        except (KeyError, IndexError) as e:
            return None

    def get_offset_limit(self, content):
        try:
            page = content.get(self.PAGE_QUERY, None)
            page = (
                self.get_mandatory_value_from_dict(content, self.PAGE_QUERY)
                if page is not None
                else None
            )

            # Si hay page
            if page is not None:
                # Si hay limit coge el valor si no se le asigna el por defecto
                limit = content.get(self.LIMIT_QUERY, self.MAX_QUERY_LIMIT)
                if isinstance(limit, int):
                    return int(limit) * int(page), int(limit)
                else:
                    limit = self.get_mandatory_value_from_dict(
                        content, self.LIMIT_QUERY
                    )
                    return int(limit) * int(page), int(limit)

            # Si solo esta limit y no hay page
            limit = content.get(self.LIMIT_QUERY, None)
            if limit is not None:
                if isinstance(limit, int):
                    # Se devuelve la primera pagina con el limite establecido
                    return 0, int(limit)
                else:
                    limit = (
                        self.get_mandatory_value_from_dict(content, self.LIMIT_QUERY)
                        if limit is not None
                        else None
                    )
                    # Se devuelve la primera pagina con el limite establecido
                    return 0, int(limit)

        except Exception as e:
            print("ERROR: UseCase -> get_offset_limit: " + str(e))

        return None, None

    # Dado una lista de diccionarios y una lista de claves para esos diccionarios,
    # los diccionarios de salida solo contentran las claves que estan en list_
    def clean_data(self, data, list_=None) -> dict:
        try:
            if data is not None:
                if isinstance(data, list) and isinstance(list_, list):
                    result = [
                        {key: json_data[key] for key in list_ if key in json_data}
                        for json_data in data
                    ]

                elif isinstance(data, dict) and isinstance(list_, list):
                    result = {key: data[key] for key in list_ if key in data}

                else:
                    result = data

                return result

        except Exception as e:
            print("ERROR: UseCase -> clean_data: " + str(e))

        return None
