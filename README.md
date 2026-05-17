# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub, MCP y Hugging Face.

## Que hace

El proyecto incluye un script simple que pide tu nombre en consola y muestra un saludo. Tambien incluye un ejemplo que usa un modelo real de Hugging Face para analisis de sentimiento en espanol.

## Archivos

- `main.py`: punto de entrada del programa.
- `huggingface_demo.py`: usa Hugging Face para clasificar el sentimiento de un texto.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: reglas basicas para proyectos Python.

## Como ejecutar el saludo

Necesitas Python 3 instalado. Luego ejecuta:

```bash
python main.py
```

## Como preparar dependencias

Instala las dependencias con:

```bash
python -m pip install -r requirements.txt
```

## Como usar el modelo de Hugging Face

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

## Modelo usado

El script usa este modelo real de Hugging Face:

https://huggingface.co/finiteautomata/beto-sentiment-analysis

La llamada se hace con `huggingface_hub.InferenceClient`, usando el proveedor remoto `hf-inference`. Si Hugging Face solicita autenticacion o aparece limite de uso, crea un token en Hugging Face y guardalo como variable de entorno `HF_TOKEN`.

## Estado de la prueba

- Repositorio creado en GitHub.
- Repositorio visible desde GitHub MCP.
- Archivos Python creados desde Codex usando MCP.
- Modelo de Hugging Face encontrado usando Hugging Face MCP.
- Demo actualizado para llamar a un modelo real de Hugging Face.
