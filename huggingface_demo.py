"""Ejemplo basico inspirado en Hugging Face.

Este archivo no descarga modelos. Sirve para entender la idea:
una frase entra, el programa devuelve una etiqueta de sentimiento.

Modelo real para explorar:
https://huggingface.co/finiteautomata/beto-sentiment-analysis
"""

FRASES_POSITIVAS = {"encanta", "excelente", "feliz", "bueno", "genial"}
FRASES_NEGATIVAS = {"malo", "triste", "odio", "terrible", "problema"}


def analizar_sentimiento(texto: str) -> str:
    texto_normalizado = texto.lower()

    if any(palabra in texto_normalizado for palabra in FRASES_POSITIVAS):
        return "positivo"

    if any(palabra in texto_normalizado for palabra in FRASES_NEGATIVAS):
        return "negativo"

    return "neutral"


def main() -> None:
    ejemplos = [
        "Me encanta aprender con este proyecto",
        "Tengo un problema con la instalacion",
        "Hoy estamos probando Hugging Face",
    ]

    for frase in ejemplos:
        sentimiento = analizar_sentimiento(frase)
        print(f"{frase} -> {sentimiento}")


if __name__ == "__main__":
    main()
