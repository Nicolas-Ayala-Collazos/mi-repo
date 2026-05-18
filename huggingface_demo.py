"""Usa un modelo real de Hugging Face para analisis de sentimiento.

Modelo usado:
https://huggingface.co/finiteautomata/beto-sentiment-analysis

El script llama a la API remota de Hugging Face con huggingface_hub.
Si tienes un token, puedes guardarlo en la variable de entorno HF_TOKEN.
"""

from __future__ import annotations

import argparse
import os
from typing import Any

from huggingface_hub import InferenceClient

MODEL_ID = os.getenv("HF_MODEL", "finiteautomata/beto-sentiment-analysis")
EJEMPLOS = [
    "Me encanta aprender con este proyecto",
    "Tengo un problema con la instalacion",
    "Hoy estamos probando Hugging Face",
]


def _leer_campo(resultado: Any, campo: str) -> Any:
    if isinstance(resultado, dict):
        return resultado[campo]
    return getattr(resultado, campo)


def analizar_sentimiento(texto: str) -> tuple[str, float]:
    client = InferenceClient(
        model=MODEL_ID,
        provider="hf-inference",
        token=os.getenv("HF_TOKEN"),
        timeout=30,
    )
    resultados = client.text_classification(texto, top_k=1)
    mejor = resultados[0]

    etiqueta = str(_leer_campo(mejor, "label"))
    puntaje = float(_leer_campo(mejor, "score"))
    return etiqueta, puntaje


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clasifica sentimiento en espanol usando un modelo real de Hugging Face."
    )
    parser.add_argument(
        "--texto",
        help="Texto a clasificar. Si no lo pasas, se usan ejemplos incluidos.",
    )
    args = parser.parse_args()

    frases = [args.texto] if args.texto else EJEMPLOS

    for frase in frases:
        try:
            etiqueta, puntaje = analizar_sentimiento(frase)
        except Exception as exc:
            print("No se pudo consultar Hugging Face.")
            print("Revisa tu conexion o configura un token en HF_TOKEN si la API lo solicita.")
            print(f"Detalle: {exc}")
            return

        print(f"{frase} -> {etiqueta} ({puntaje:.2%})")


if __name__ == "__main__":
    main()
