# mi-repo

Aplicacion web y API REST para clasificar sentimientos de texto usando Flask, Docker y un modelo de Hugging Face.

## Modelo

Usa `finiteautomata/beto-sentiment-analysis` a traves de la API de inferencia de Hugging Face. Puedes cambiarlo con la variable `HF_MODEL`.

## Configurar token

Crea un archivo `.env` tomando como base `.env.example`:

```text
HF_MODEL=finiteautomata/beto-sentiment-analysis
HF_TOKEN=hf_tu_token
```

No subas `.env` a GitHub. Solo `.env.example` debe quedar en el repositorio.

## Ejecutar con PowerShell

```powershell
.\run.ps1
```

El script lee automaticamente `.env`, define las variables para Docker y ejecuta:

```powershell
docker compose up --build
```

Luego abre:

```text
http://localhost:8000
```

## Probar la API

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/sentimiento" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"texto":"Me encanto el servicio"}'
```

Respuesta de ejemplo:

```json
{
  "etiqueta": "POS",
  "modelo": "finiteautomata/beto-sentiment-analysis",
  "puntaje": 0.98,
  "texto": "Me encanto el servicio"
}
```

## Endpoints

- `GET /`: interfaz web con Flask.
- `GET /health`: estado de la aplicacion.
- `POST /sentimiento`: clasifica un texto.
