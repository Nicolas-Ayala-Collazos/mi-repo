param(
    [string]$HfToken,
    [string]$HfModel
)

$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $PSScriptRoot

function Read-DotEnv {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return
    }

    Get-Content -LiteralPath $Path | ForEach-Object {
        $line = $_.Trim()

        if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) {
            return
        }

        $parts = $line -split "=", 2

        if ($parts.Count -ne 2) {
            return
        }

        $name = $parts[0].Trim()
        $value = $parts[1].Trim().Trim('"').Trim("'")

        if (-not [string]::IsNullOrWhiteSpace($name)) {
            Set-Item -Path "Env:$name" -Value $value
        }
    }
}

Read-DotEnv -Path (Join-Path $PSScriptRoot ".env")

if ([string]::IsNullOrWhiteSpace($HfToken)) {
    $HfToken = $env:HF_TOKEN
}

if ([string]::IsNullOrWhiteSpace($HfModel)) {
    $HfModel = $env:HF_MODEL
}

if ([string]::IsNullOrWhiteSpace($HfModel)) {
    $HfModel = "finiteautomata/beto-sentiment-analysis"
}

if ([string]::IsNullOrWhiteSpace($HfToken)) {
    $secureToken = Read-Host "Pega tu token de Hugging Face" -AsSecureString
    $plainTokenPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureToken)

    try {
        $HfToken = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($plainTokenPointer)
    }
    finally {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($plainTokenPointer)
    }
}

if ([string]::IsNullOrWhiteSpace($HfToken)) {
    Write-Error "Debes indicar HF_TOKEN para consultar la API de Hugging Face."
}

$env:HF_MODEL = $HfModel
$env:HF_TOKEN = $HfToken

Write-Host "Usando modelo: $env:HF_MODEL"
Write-Host "Levantando la aplicacion Flask en http://localhost:8000 ..."

docker compose up --build
