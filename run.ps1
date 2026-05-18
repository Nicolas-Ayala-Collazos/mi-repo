param(
    [string]$HfToken = $env:HF_TOKEN,
    [string]$HfModel = $env:HF_MODEL
)

$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $PSScriptRoot

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
Write-Host "Levantando la aplicacion en http://localhost:8001 ..."

docker compose up --build
