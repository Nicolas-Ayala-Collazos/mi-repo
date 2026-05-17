import argparse


def saludar(nombre: str) -> str:
    return f"Hola, {nombre}. GitHub MCP esta funcionando."


def obtener_nombre(nombre: str | None) -> str:
    if nombre and nombre.strip():
        return nombre.strip()

    respuesta = input("Como te llamas? ").strip()
    return respuesta or "Codex"


def main() -> None:
    parser = argparse.ArgumentParser(description="Saluda a una persona por nombre.")
    parser.add_argument("--nombre", help="Nombre de la persona a saludar.")
    args = parser.parse_args()

    print(saludar(obtener_nombre(args.nombre)))


if __name__ == "__main__":
    main()
