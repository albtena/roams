# Usa una imagen base de Python 3.11
FROM python:3.11

# Variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /api

# Instalar  dependencias
RUN apt-get update \
  && apt-get install -y libaio1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

####################################
############ DEPENDENCIAS ##########
####################################
# Copiar el archivo de requerimientos
COPY requirements.txt .
# Instalar las dependencias, incluyendo cx_Oracle
RUN pip install --no-cache-dir -r requirements.txt

####################################
############## PROYECTO ############
####################################
# Copiar archivos necesarios
COPY .env ../
COPY /. /api

# Exponer el puerto
EXPOSE 8000


# Comando por defecto para ejecutar la aplicación
CMD ["python", "main.py", "--env", "docker"]
