## Licencia
Este proyecto está protegido por derechos de autor.

- **Uso permitido:** Uso privado y no comercial únicamente.
- **Prohibiciones:**
  - Está prohibida la distribución total o parcial del sotfware.
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
   git clone git clone https://github.com/albtena/roams.git
   cd roams
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
   


## Ejemplo de Uso de la API

La documentación de la API se encuentra disponible accediendo a `http://localhost:8000/docs`, proporcionada automáticamente por **FastAPI**. Desde esta documentación interactiva, puedes probar las rutas disponibles utilizando el método **POST**.

### Rutas disponibles

#### 1. `user/new_user`
**Método:** POST  
**Ejemplo de body:**
```json
{
  "dni": "XXXXXXXX",  
  "name": "Test",  
  "email": "test@test.com"
}
```

#### 2. `user/get_user`
**Método:** POST  
**Ejemplo de body:**
```json
{
  "dni": "XXXXXXXX"
}
```

#### 3. `user/update_user`
**Método:** POST  
**Ejemplo de body:**
```json
{
  "dni": "XXXXXXXX",  
  "name": "Test",  
  "email": "test@test.com"
}
```

#### 4. `mortgage_sim/new_sim`
**Método:** POST  
**Ejemplo de body:**
```json
{
  "dni": "XXXXXXXX",  
  "tae": "2.5",  
  "requested_capital": 100000,  
  "amortization_period": 150
}
```
