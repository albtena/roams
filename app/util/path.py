import inspect
import os


def get_current_path():
    try:
        frame = inspect.stack()[1]
        # Obtener el path del archivo que llama a esta función
        caller_file = frame.filename
        # Obtener la ruta absoluta del archivo
        caller_path = os.path.abspath(caller_file)
        # Obtener el directorio del archivo
        caller_dir = os.path.dirname(caller_path)
        return caller_dir
    except Exception as e:
        print("ERROR Util path -> get_current_path: " + str(e))


def get_path_file(path, file_name):
    try:
        return os.path.join(path, file_name)
    except Exception as e:
        print("ERROR Util path -> get_path_file: " + str(e))
