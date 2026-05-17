from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from huggingface_demo import MODEL_ID, analizar_sentimiento

app = FastAPI(
    title="API de Analisis de Sentimiento",
    description="Clasifica textos en espanol usando un modelo real de Hugging Face.",
    version="0.1.0",
)


class SentimientoRequest(BaseModel):
    texto: str = Field(..., min_length=1, description="Texto en espanol para clasificar.")


class SentimientoResponse(BaseModel):
    texto: str
    etiqueta: str
    puntaje: float
    modelo: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "modelo": MODEL_ID}


@app.post("/sentimiento", response_model=SentimientoResponse)
def clasificar_sentimiento(payload: SentimientoRequest) -> SentimientoResponse:
    try:
        etiqueta, puntaje = analizar_sentimiento(payload.texto)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=(
                "No se pudo consultar Hugging Face. "
                "Revisa tu conexion o configura HF_TOKEN si la API lo solicita. "
                f"Detalle: {exc}"
            ),
        ) from exc

    return SentimientoResponse(
        texto=payload.texto,
        etiqueta=etiqueta,
        puntaje=puntaje,
        modelo=MODEL_ID,
    )
