# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub, MCP y Hugging Face.

## Que hace

El proyecto incluye un script simple que pide tu nombre en consola y muestra un saludo. Tambien incluye un ejemplo basico inspirado en Hugging Face para entender el analisis de sentimiento.

## Archivos

- `main.py`: punto de entrada del programa.
- `huggingface_demo.py`: ejemplo simple de analisis de sentimiento inspirado en modelos de Hugging Face.
- `requirements.txt`: dependencias del proyecto, por ahora vacio porque solo usamos Python estandar.
- `.gitignore`: reglas basicas para proyectos Python.

## Como ejecutar el saludo

Necesitas Python 3 instalado. Luego ejecuta:

```bash
python main.py
```

Ejemplo:

```text
Como te llamas? Nicolas
Hola, Nicolas. GitHub MCP esta funcionando.
```

## Como ejecutar el ejemplo de Hugging Face

Ejecuta:

```bash
python huggingface_demo.py
```

Salida esperada:

```text
Me encanta aprender con este proyecto -> positivo
Tengo un problema con la instalacion -> negativo
Hoy estamos probando Hugging Face -> neutral
```

## Modelo real para explorar

El ejemplo se inspira en este modelo de Hugging Face:

https://huggingface.co/finiteautomata/beto-sentiment-analysis

Ese modelo real sirve para clasificar sentimiento en textos en espanol.

## Estado de la prueba

- Repositorio creado en GitHub.
- Repositorio visible desde GitHub MCP.
- Archivos Python creados desde Codex usando MCP.
- Modelo de Hugging Face encontrado usando Hugging Face MCP.
