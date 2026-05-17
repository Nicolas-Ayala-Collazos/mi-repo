# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub, MCP, Hugging Face y FastAPI.

## Que hace

El proyecto incluye un script simple que pide tu nombre en consola y muestra un saludo. Tambien incluye un ejemplo que usa un modelo real de Hugging Face para analisis de sentimiento en espanol y una API con FastAPI para consumirlo desde HTTP.

## Archivos

- `main.py`: punto de entrada del programa inicial.
- `huggingface_demo.py`: usa Hugging Face para clasificar el sentimiento de un texto.
- `app.py`: API con FastAPI para exponer el modelo por HTTP.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: reglas basicas para proyectos Python.

## Como preparar dependencias

Instala las dependencias con:

```bash
python -m pip install -r requirements.txt
```

Si Hugging Face solicita autenticacion, crea un token de lectura y guardalo en la variable de entorno `HF_TOKEN`.

En PowerShell, solo para la terminal actual:

```powershell
$env:HF_TOKEN="TU_TOKEN_NUEVO"
```

## Como usar el modelo desde consola

Ejecuta los ejemplos incluidos:

```bash
python huggingface_demo.py
```

O clasifica tu propio texto:

```bash
python huggingface_demo.py --texto "Me encanta este proyecto"
```

Salida esperada aproximada:

```text
Me encanta este proyecto -> POS (99.12%)
```

## Como ejecutar la API con FastAPI

Levanta el servidor local:

```bash
python -m uvicorn app:app --reload
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/docs
```

FastAPI genera una pagina interactiva donde puedes probar la API.

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

## Probar desde PowerShell

Con el servidor corriendo, ejecuta en otra terminal:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/sentimiento" -Method Post -ContentType "application/json" -Body '{"texto":"Me encanta este proyecto"}'
```

## Modelo usado

El script usa este modelo real de Hugging Face:

https://huggingface.co/finiteautomata/beto-sentiment-analysis

La llamada se hace con `huggingface_hub.InferenceClient`, usando el proveedor remoto `hf-inference`.

## Estado de la prueba

- Repositorio creado en GitHub.
- Repositorio visible desde GitHub MCP.
- Archivos Python creados desde Codex usando MCP.
- Modelo de Hugging Face encontrado usando Hugging Face MCP.
- Demo actualizado para llamar a un modelo real de Hugging Face.
- API agregada con FastAPI.
