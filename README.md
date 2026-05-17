# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub, MCP, Hugging Face y FastAPI.

## Que hace

El proyecto incluye una API con FastAPI que clasifica sentimiento en espanol usando un modelo real de Hugging Face.

## Archivos

- `main.py`: punto de entrada del programa inicial.
- `huggingface_demo.py`: usa Hugging Face para clasificar el sentimiento de un texto.
- `app.py`: API con FastAPI para exponer el modelo por HTTP.
- `run_api.ps1`: script de PowerShell para instalar dependencias, cargar `HF_TOKEN` y levantar la API.
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

No subas `.env` a GitHub. Ya esta protegido por `.gitignore`.

## Ejecutar la API con un solo script

En PowerShell:

```powershell
.\run_api.ps1
```

El script hace tres cosas:

1. Lee `HF_TOKEN` desde `.env`.
2. Instala dependencias con `python -m pip install -r requirements.txt`.
3. Levanta FastAPI con `python -m uvicorn app:app --reload`.

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
