$ErrorActionPreference = "Stop"

$envFile = Join-Path $PSScriptRoot ".env"

if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        $line = $_.Trim()
        if (-not $line -or $line.StartsWith("#")) {
            return
        }

        $parts = $line.Split("=", 2)
        if ($parts.Count -eq 2) {
            $name = $parts[0].Trim()
            $value = $parts[1].Trim().Trim('"')
            [Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
} else {
    Write-Host "No existe .env. Crea uno copiando .env.example y pon alli tu HF_TOKEN." -ForegroundColor Yellow
    Write-Host "Ejemplo: Copy-Item .env.example .env" -ForegroundColor Yellow
    exit 1
}

if (-not $env:HF_TOKEN) {
    Write-Host "HF_TOKEN no esta configurado en .env." -ForegroundColor Red
    exit 1
}

Write-Host "Instalando dependencias..." -ForegroundColor Cyan
python -m pip install -r requirements.txt

Write-Host "Iniciando API en http://127.0.0.1:8000/docs" -ForegroundColor Green
python -m uvicorn app:app --reload
