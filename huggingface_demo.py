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

import requests

MODEL_ID = "finiteautomata/beto-sentiment-analysis"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
EJEMPLOS = [
    "Me encanta aprender con este proyecto",
    "Tengo un problema con la instalacion",
    "Hoy estamos probando Hugging Face",
]


def _leer_campo(resultado: Any, campo: str) -> Any:
    if isinstance(resultado, dict):
        return resultado[campo]
    return getattr(resultado, campo)


def _verificar_ssl() -> bool:
    valor = os.getenv("HF_SSL_VERIFY", "true").strip().lower()
    return valor not in {"0", "false", "no"}


def analizar_sentimiento(texto: str) -> tuple[str, float]:
    headers = {}
    token = os.getenv("HF_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": texto},
        timeout=30,
        verify=_verificar_ssl(),
    )
    response.raise_for_status()

    resultados = response.json()
    if isinstance(resultados, list) and resultados and isinstance(resultados[0], list):
        resultados = resultados[0]
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
            print("Revisa tu conexion, HF_TOKEN, HF_CA_BUNDLE o usa HF_SSL_VERIFY=false para una prueba local.")
            print(f"Detalle: {exc}")
            return

        print(f"{frase} -> {etiqueta} ({puntaje:.2%})")


if __name__ == "__main__":
    main()
