from main import obtener_nombre, saludar


def test_saludar_devuelve_mensaje_esperado():
    assert saludar("Nicolas") == "Hola, Nicolas. GitHub MCP esta funcionando."


def test_obtener_nombre_usa_argumento_cli():
    assert obtener_nombre(" Ana ") == "Ana"


def test_obtener_nombre_usa_codex_si_no_hay_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    assert obtener_nombre(None) == "Codex"
