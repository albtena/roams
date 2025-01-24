## Licencia
Este proyecto está protegido por derechos de autor.

- **Uso permitido:** Uso privado y no comercial únicamente.
- **Prohibiciones:**
  - Está prohibida la distribución total o parcial del código.
  - Está prohibido el uso con fines comerciales.

Para más detalles, consulta el archivo [LICENSE](LICENSE).

# Instrucciones de Uso

Esta aplicación puede ejecutarse utilizando **Docker** o de manera manual. A continuación, se detallan las instrucciones para ambos métodos.

---

## Opción 1: Usando Docker

### Prerrequisitos
- Tener instalado [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

### Pasos
1. Clona el repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd [NOMBRE_DEL_REPOSITORIO]
   ```
2. Construye los contenedores de Docker:
   ```bash
   docker-compose build
   ```
3. Inicia la aplicación:
   ```bash
   docker-compose up
   ```

---

## Opción 2: Instalación manual

### Prerrequisitos
- Tener instalado [Python 3.11+](https://www.python.org/).

### Pasos
1. Clona el repositorio:
   ```bash
   git clone https://github.com/albtena/roams.git
   cd roams
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python main.py
   


