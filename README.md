# mi-repo

Aplicacion web y API REST para clasificar sentimientos de texto usando Docker y un modelo de Hugging Face.

## Modelo

Usa `finiteautomata/beto-sentiment-analysis` a traves de la API de inferencia de Hugging Face. Puedes cambiarlo con la variable `HF_MODEL`. La aplicacion soporta etiquetas `NEG`, `NEU`, `POS` y tambien modelos que devuelven calificaciones de 1 a 5 estrellas.

- `NEG` o 1-2 estrellas: `negativo`.
- `NEU` o 3 estrellas: `neutral`.
- `POS` o 4-5 estrellas: `positivo`.

## Ejecutar con Docker

```bash
docker compose up --build
```

Luego abre:

```text
http://localhost:8001
```

Esta version no instala PyTorch ni descarga el modelo dentro del contenedor, por eso construye mucho mas rapido. Hugging Face puede exigir autenticacion para la API de inferencia. Define tu token antes de levantar Docker:

```bash
export HF_TOKEN=tu_token
```

En PowerShell:

```powershell
$env:HF_TOKEN="tu_token"
```

Tambien puedes usar el script de PowerShell incluido:

```powershell
.\run.ps1
```

El script lee automaticamente el archivo `.env` si existe.

O pasar el token directamente:

```powershell
.\run.ps1 -HfToken "hf_tu_token"
```

Tambien puedes crear un archivo `.env` tomando como base `.env.example`:

```text
HF_MODEL=finiteautomata/beto-sentiment-analysis
HF_TOKEN=hf_tu_token
```

Para usar otro modelo:

```powershell
$env:HF_MODEL="nlptown/bert-base-multilingual-uncased-sentiment"
```

## Probar la API

```bash
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Me encanto el servicio, fue rapido y muy amable.\"}"
```

Respuesta de ejemplo:

```json
{
  "text": "Me encanto el servicio, fue rapido y muy amable.",
  "sentiment": "positivo",
  "stars": 5,
  "confidence": 0.71,
  "model": "finiteautomata/beto-sentiment-analysis"
}
```

## Endpoints

- `GET /`: interfaz web.
- `GET /health`: estado de la aplicacion.
- `POST /predict`: clasifica un texto.
