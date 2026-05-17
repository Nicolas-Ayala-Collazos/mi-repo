# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub, MCP, Hugging Face, FastAPI y Docker.

## Que hace

El proyecto incluye una API con FastAPI que clasifica sentimiento en espanol usando un modelo real de Hugging Face. Esta rama agrega Docker para ejecutar la API dentro de un contenedor.

## Archivos

- `main.py`: punto de entrada del programa inicial.
- `huggingface_demo.py`: usa Hugging Face para clasificar el sentimiento de un texto.
- `app.py`: API con FastAPI para exponer el modelo por HTTP.
- `run_api.ps1`: script de PowerShell para ejecutar la API localmente sin Docker.
- `Dockerfile`: instrucciones para construir la imagen Docker.
- `docker-compose.yml`: configuracion para levantar la API con Docker Compose.
- `.dockerignore`: evita copiar archivos innecesarios o secretos a la imagen.
- `.env.example`: plantilla para crear tu archivo local `.env`.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: evita subir archivos privados como `.env`.

## Configurar el token una sola vez

Copia la plantilla:

```powershell
Copy-Item .env.example .env
```

Abre `.env` en VS Code y reemplaza el texto por tu token nuevo:

```env
HF_TOKEN=tu_token_nuevo_aqui
```

No subas `.env` a GitHub. Ya esta protegido por `.gitignore` y tambien queda fuera de la imagen por `.dockerignore`.

## Ejecutar sin Docker

En PowerShell:

```powershell
.\run_api.ps1
```

Luego abre:

```text
http://127.0.0.1:8000/docs
```

## Ejecutar con Docker Compose

Con Docker Desktop abierto, ejecuta:

```powershell
docker compose up --build
```

Luego abre:

```text
http://127.0.0.1:8000/docs
```

Para apagar:

```powershell
Ctrl + C
```

O en otra terminal:

```powershell
docker compose down
```

## Ejecutar con Docker sin Compose

Construir la imagen:

```powershell
docker build -t sentimiento-api .
```

Ejecutar el contenedor usando tu `.env` local:

```powershell
docker run --rm -p 8000:8000 --env-file .env sentimiento-api
```

Luego abre:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

Revisar si la API esta viva:

```text
GET /health
```

Clasificar sentimiento:

```text
POST /sentimiento
```

Ejemplo de cuerpo JSON:

```json
{
  "texto": "Me encanta este proyecto"
}
```

Ejemplo de respuesta:

```json
{
  "texto": "Me encanta este proyecto",
  "etiqueta": "POS",
  "puntaje": 0.9912,
  "modelo": "finiteautomata/beto-sentiment-analysis"
}
```

## Modelo usado

El script usa este modelo real de Hugging Face:

https://huggingface.co/finiteautomata/beto-sentiment-analysis

La llamada se hace con `huggingface_hub.InferenceClient`, usando el proveedor remoto `hf-inference`.
