from __future__ import annotations

from flask import Flask, jsonify, render_template_string, request

from huggingface_demo import MODEL_ID, analizar_sentimiento


app = Flask(__name__)


INDEX_HTML = """
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Analisis de Sentimiento</title>
    <style>
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        padding: 28px 16px;
        background: #f5f7fb;
        color: #172033;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      main {
        width: min(760px, 100%);
        background: #ffffff;
        border: 1px solid #d9e2ef;
        border-radius: 8px;
        box-shadow: 0 18px 50px rgba(20, 35, 60, 0.12);
        overflow: hidden;
      }

      header, section {
        padding: 28px 32px;
      }

      header {
        border-bottom: 1px solid #e5ebf3;
      }

      h1 {
        margin: 0 0 8px;
        font-size: 28px;
        line-height: 1.2;
      }

      p {
        margin: 0;
        color: #52627a;
        line-height: 1.5;
      }

      label {
        display: block;
        margin-bottom: 10px;
        font-weight: 700;
      }

      textarea {
        box-sizing: border-box;
        width: 100%;
        min-height: 150px;
        resize: vertical;
        border: 1px solid #bac7d8;
        border-radius: 8px;
        padding: 14px 16px;
        font: inherit;
        line-height: 1.5;
      }

      textarea:focus {
        outline: 3px solid #c7ddff;
        border-color: #286ec2;
      }

      .actions {
        margin-top: 16px;
        display: flex;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
      }

      button {
        border: 0;
        border-radius: 8px;
        background: #195fb8;
        color: #ffffff;
        font: inherit;
        font-weight: 700;
        padding: 11px 18px;
        cursor: pointer;
      }

      button:disabled {
        cursor: wait;
        opacity: 0.65;
      }

      output {
        display: block;
        margin-top: 22px;
        min-height: 86px;
        padding: 18px;
        border: 1px solid #d8e5f4;
        border-radius: 8px;
        background: #eef4fb;
      }

      .result {
        display: grid;
        gap: 8px;
      }

      .sentiment {
        font-size: 24px;
        font-weight: 800;
        text-transform: uppercase;
      }

      .meta {
        color: #52627a;
      }

      .error {
        color: #9b1c1c;
        font-weight: 700;
      }
    </style>
  </head>
  <body>
    <main>
      <header>
        <h1>Analisis de Sentimiento</h1>
        <p>Aplicacion Flask con Docker y un modelo de Hugging Face para texto en espanol.</p>
      </header>
      <section>
        <form id="form">
          <label for="texto">Texto para analizar</label>
          <textarea id="texto" required>Me encanto el servicio, fue rapido y muy amable.</textarea>
          <div class="actions">
            <button id="submit" type="submit">Clasificar</button>
            <span class="meta">Endpoint: <code>POST /sentimiento</code></span>
          </div>
        </form>
        <output id="output" aria-live="polite">El resultado aparecera aqui.</output>
      </section>
    </main>

    <script>
      const form = document.querySelector("#form");
      const texto = document.querySelector("#texto");
      const output = document.querySelector("#output");
      const submit = document.querySelector("#submit");

      form.addEventListener("submit", async (event) => {
        event.preventDefault();
        submit.disabled = true;
        output.textContent = "Analizando con Hugging Face...";

        try {
          const response = await fetch("/sentimiento", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ texto: texto.value }),
          });
          const data = await response.json();

          if (!response.ok) {
            throw new Error(data.detail || "No se pudo clasificar el texto.");
          }

          output.innerHTML = `
            <div class="result">
              <div class="sentiment">${data.etiqueta}</div>
              <div>Confianza: <strong>${(data.puntaje * 100).toFixed(2)}%</strong></div>
              <div class="meta">Modelo: <code>${data.modelo}</code></div>
            </div>
          `;
        } catch (error) {
          output.innerHTML = `<span class="error">${error.message}</span>`;
        } finally {
          submit.disabled = false;
        }
      });
    </script>
  </body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(INDEX_HTML)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "modelo": MODEL_ID})


@app.post("/sentimiento")
def clasificar_sentimiento():
    payload = request.get_json(silent=True) or {}
    texto = str(payload.get("texto", "")).strip()

    if not texto:
        return jsonify({"detail": "El campo 'texto' es obligatorio."}), 400

    try:
        etiqueta, puntaje = analizar_sentimiento(texto)
    except Exception as exc:
        return (
            jsonify(
                {
                    "detail": (
                        "No se pudo consultar Hugging Face. "
                        "Revisa tu conexion o configura HF_TOKEN si la API lo solicita. "
                        f"Detalle: {exc}"
                    )
                }
            ),
            502,
        )

    return jsonify(
        {
            "texto": texto,
            "etiqueta": etiqueta,
            "puntaje": puntaje,
            "modelo": MODEL_ID,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
