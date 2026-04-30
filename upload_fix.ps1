# Script Corrigido para Upload GitHub
param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubToken
)

$RepoOwner = "colegioherciliafranca-commits"
$RepoName = "agenda-escolar-2026"
$BaseUrl = "https://api.github.com/repos/$RepoOwner/$RepoName"

$Headers = @{
    "Authorization" = "token $GitHubToken"
    "Accept" = "application/vnd.github.v3+json"
}

Write-Host "Iniciando upload..." -ForegroundColor Green

# Ler arquivos
$agendaContent = [Convert]::ToBase64String([IO.File]::ReadAllBytes("agenda_escolar.html"))
$readmeContent = [Convert]::ToBase64String([IO.File]::ReadAllBytes("README_AGENDA.md"))
$deployContent = [Convert]::ToBase64String([IO.File]::ReadAllBytes("DEPLOY.md"))

# Upload agenda_escolar.html
$body = @{
    message = "Upload agenda escolar"
    content = $agendaContent
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/contents/agenda_escolar.html" -Headers $Headers -Method Put -Body $body
    Write-Host "agenda_escolar.html uploaded" -ForegroundColor Green
} catch {
    Write-Host "Erro no upload de agenda_escolar.html" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Upload README.md
$body = @{
    message = "Upload README"
    content = $readmeContent
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/contents/README.md" -Headers $Headers -Method Put -Body $body
    Write-Host "README.md uploaded" -ForegroundColor Green
} catch {
    Write-Host "Erro no upload de README.md" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Upload DEPLOY.md
$body = @{
    message = "Upload DEPLOY"
    content = $deployContent
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/contents/DEPLOY.md" -Headers $Headers -Method Put -Body $body
    Write-Host "DEPLOY.md uploaded" -ForegroundColor Green
} catch {
    Write-Host "Erro no upload de DEPLOY.md" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Ativar GitHub Pages
try {
    $pagesBody = @{
        source = @{
            branch = "main"
            path = "/"
        }
    } | ConvertTo-Json
    
    $response = Invoke-RestMethod -Uri "$BaseUrl/pages" -Headers $Headers -Method Post -Body $pagesBody
    Write-Host "GitHub Pages ativado" -ForegroundColor Green
} catch {
    Write-Host "GitHub Pages pode ja estar ativo ou houve erro" -ForegroundColor Yellow
}

$finalUrl = "https://$RepoOwner.github.io/$RepoName/agenda_escolar.html"
Write-Host ""
Write-Host "SUCESSO!" -ForegroundColor Green
Write-Host "URL da Agenda: $finalUrl" -ForegroundColor Cyan
Write-Host "Aguarde 2-3 minutos para o site ficar online" -ForegroundColor Yellow
