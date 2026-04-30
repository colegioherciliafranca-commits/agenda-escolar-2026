# Script PowerShell para Upload Automático no GitHub
# Execute: powershell -ExecutionPolicy Bypass -File upload_powershell.ps1

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubToken
)

Write-Host "🚀 UPLOAD AUTOMÁTICO PARA GITHUB" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green

# Configurações
$RepoOwner = "colegioherciliafranca-commits"
$RepoName = "agenda-escolar-2026"
$BaseUrl = "https://api.github.com/repos/$RepoOwner/$RepoName"

# Headers para API
$Headers = @{
    "Authorization" = "token $GitHubToken"
    "Accept" = "application/vnd.github.v3+json"
}

function Get-FileBase64($filePath) {
    $content = Get-Content -Path $filePath -Raw -Encoding Byte
    return [System.Convert]::ToBase64String($content)
}

function Upload-File($fileName, $content, $message) {
    $url = "$BaseUrl/contents/$fileName"
    
    $body = @{
        message = $message
        content = $content
    } | ConvertTo-Json
    
    # Verificar se arquivo já existe
    try {
        $response = Invoke-RestMethod -Uri $url -Headers $Headers -Method Get
        $existingFile = $response | ConvertTo-Json | ConvertFrom-Json
        $body = @{
            message = $message
            content = $content
            sha = $existingFile.sha
        } | ConvertTo-Json
    } catch {
        # Arquivo não existe, continua sem SHA
    }
    
    try {
        $response = Invoke-RestMethod -Uri $url -Headers $Headers -Method Put -Body $body -ContentType "application/json"
        return $true
    } catch {
        Write-Host "❌ Erro no upload de $fileName`: $_" -ForegroundColor Red
        return $false
    }
}

function Enable-GitHubPages {
    $url = "$BaseUrl/pages"
    
    $body = @{
        source = @{
            branch = "main"
            path = "/"
        }
    } | ConvertTo-Json
    
    try {
        $response = Invoke-RestMethod -Uri $url -Headers $Headers -Method Post -Body $body -ContentType "application/json"
        return $true
    } catch {
        Write-Host "❌ Erro ao ativar GitHub Pages: $_" -ForegroundColor Red
        return $false
    }
}

# Verificar arquivos necessários
$filesToUpload = @(
    @{Name="agenda_escolar.html"; Message="Adicionar agenda escolar completa"},
    @{Name="README.md"; Message="Adicionar documentação do projeto"},
    @{Name="DEPLOY.md"; Message="Adicionar guia de deploy"}
)

Write-Host "📁 Verificando arquivos..." -ForegroundColor Yellow

# Verificar README_AGENDA.md para renomear
if (Test-Path "README_AGENDA.md") {
    $readmeContent = Get-FileBase64 "README_AGENDA.md"
    Write-Host "✅ README_AGENDA.md encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ README_AGENDA.md não encontrado" -ForegroundColor Red
    exit 1
}

# Verificar outros arquivos
foreach ($file in $filesToUpload) {
    if ($file.Name -eq "README.md") {
        continue  # Já verificado acima
    }
    
    if (Test-Path $file.Name) {
        Write-Host "✅ $($file.Name) encontrado" -ForegroundColor Green
    } else {
        Write-Host "❌ $($file.Name) não encontrado" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n📤 Iniciando upload dos arquivos..." -ForegroundColor Yellow

$successCount = 0

# Upload dos arquivos
foreach ($file in $filesToUpload) {
    Write-Host "📤 Upload de $($file.Name)..." -ForegroundColor Cyan
    
    if ($file.Name -eq "README.md") {
        $content = $readmeContent
    } else {
        $content = Get-FileBase64 $file.Name
    }
    
    if (Upload-File $file.Name $content $file.Message) {
        Write-Host "✅ $($file.Name) uploaded com sucesso!" -ForegroundColor Green
        $successCount++
    } else {
        Write-Host "❌ Falha no upload de $($file.Name)" -ForegroundColor Red
    }
}

if ($successCount -eq $filesToUpload.Count) {
    Write-Host "`n🌐 Ativando GitHub Pages..." -ForegroundColor Yellow
    
    if (Enable-GitHubPages) {
        Write-Host "✅ GitHub Pages ativado!" -ForegroundColor Green
        
        $finalUrl = "https://$RepoOwner.github.io/$RepoName/agenda_escolar.html"
        Write-Host "`n🎉 SUCESSO!" -ForegroundColor Green
        Write-Host "📱 URL da Agenda: $finalUrl" -ForegroundColor Cyan
        Write-Host "⏰ Aguarde 2-3 minutos para o site ficar online" -ForegroundColor Yellow
    } else {
        Write-Host "❌ Falha ao ativar GitHub Pages" -ForegroundColor Red
        Write-Host "💡 Ative manualmente em Settings > Pages" -ForegroundColor Yellow
    }
} else {
    Write-Host "`n❌ Falha no upload dos arquivos" -ForegroundColor Red
    Write-Host "Verifique o token e tente novamente" -ForegroundColor Yellow
}

Write-Host "`n======================================" -ForegroundColor Green
Write-Host "Processo concluído!" -ForegroundColor Green
