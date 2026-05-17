def saludar(nombre: str) -> str:
    return f"Hola, {nombre}. GitHub MCP esta funcionando."


def main() -> None:
    nombre = input("Como te llamas? ").strip() or "Codex"
    print(saludar(nombre))


if __name__ == "__main__":
    main()
