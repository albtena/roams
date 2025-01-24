import hashlib
import random
import re
import string
from keyword import iskeyword


def text_to_class(text: str) -> str:
    try:
        # words = re.split(r"(?<=[a-z])(?=[A-Z])|_", text)
        # pascal_case_str = "".join(
        #     word.capitalize() if word.islower() else word.title() for word in words
        # )
        # return pascal_case_str

        aux = re.compile(r"(?u)\W").sub("_", text)
        aux = "".join(part[:1].upper() + part[1:] for part in aux.split("_"))
        aux = aux.strip()
        aux = re.compile(r"(?u)\W").sub("_", aux)
        if aux[0].isdigit():
            aux = "_" + aux
        elif iskeyword(aux) or aux == "metadata":
            aux += "_"

        return aux

    except Exception as e:
        print("ERROR Util string -> text_to_class: " + str(e))


def text_to_pascal(text: str) -> str:
    try:
        words = re.split(r"(?<=[a-z])(?=[A-Z])|_", text)
        pascal_case_str = "".join(
            word.capitalize() if word.islower() else word.title() for word in words
        )
        return pascal_case_str

    except Exception as e:
        print("ERROR Util string -> text_to_pascal: " + str(e))


def text_to_snake(text: str) -> str:
    try:
        snake_case_str = "_".join(
            word.lower() for word in re.split(r"(?<=[a-z])(?=[A-Z])|_", text)
        )
        return snake_case_str
    except Exception as e:
        print("ERROR Util string -> text_to_snake: " + str(e))


def get_module(packages: list[str]) -> str:
    try:
        if not packages:
            return ""

        path_module = ".".join(packages)
        return path_module

    except Exception as e:
        print("ERROR Util string -> get_module: " + str(e))


def validate_dni(dni):
    pattern = r"^\d{8}[A-Z]$"

    # Tabla de letras válidas según el cálculo
    valid_letters = "TRWAGMYFPDXBNJZSQVHLCKE"

    if re.match(pattern, dni):
        # Separar los números y la letra
        numbers = int(dni[:-1])
        letter = dni[-1]

        # Calcular la letra correcta según el número
        correct_letter = valid_letters[numbers % 23]

        # Comparar la letra dada con la calculada
        if letter == correct_letter:
            return True
        else:
            return False
    else:
        return False
