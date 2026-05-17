# mi-repo

Mini proyecto Python creado para probar la conexion entre Codex, GitHub y MCP.

## Que hace

El proyecto incluye un script simple que muestra un saludo. Puedes pasar el nombre por argumento de consola o escribirlo cuando el programa lo pregunte.

## Archivos

- `main.py`: punto de entrada del programa y logica del saludo.
- `test_main.py`: pruebas automatizadas con pytest.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: reglas basicas para proyectos Python.
- `.github/workflows/python.yml`: workflow de GitHub Actions para ejecutar tests automaticamente.

## Como ejecutarlo

Necesitas Python 3 instalado. Luego ejecuta:

```bash
python main.py
```

Tambien puedes pasar el nombre directamente:

```bash
python main.py --nombre Nicolas
```

Ejemplo:

```text
Hola, Nicolas. GitHub MCP esta funcionando.
```

## Como correr los tests

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta las pruebas:

```bash
python -m pytest
```

## Automatizacion

GitHub Actions ejecuta los tests automaticamente cuando hay cambios en `main`, ramas `feature/**` o pull requests hacia `main`.

## Estado de la prueba

- Repositorio creado en GitHub.
- Repositorio visible desde GitHub MCP.
- Rama `feature/tests` creada desde MCP.
- Tests agregados con pytest.
- GitHub Actions configurado para CI.
