# Como Executar Upload Automático Agora

## 🚀 Execute o Comando Abaixo

Copie e cole este comando no PowerShell (como Administrador):

```powershell
powershell -ExecutionPolicy Bypass -File upload_powershell.ps1 -GitHubToken "SEU_TOKEN_AQUI"
```

## 📋 Substitua SEU_TOKEN_AQUI

1. **Gere seu token** em: https://github.com/settings/tokens
2. **Copie o token** gerado
3. **Substitua** "SEU_TOKEN_AQUI" no comando acima

## 🎯 Exemplo com Token Real

```powershell
powershell -ExecutionPolicy Bypass -File upload_powershell.ps1 -GitHubToken "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## ✅ O Que o Script Faz

- 📤 Upload automático dos 3 arquivos
- 📝 Renomeia README_AGENDA.md → README.md  
- 🌐 Ativa GitHub Pages
- 📱 Fornece URL final

## 🌐 URL Final

```
https://colegioherciliafranca-commits.github.io/agenda-escolar-2026/agenda_escolar.html
```

## ⚡ Execute Agora Mesmo

1. **Abra PowerShell** (como Administrador)
2. **Navegue até a pasta**:
   ```powershell
   cd C:\Users\Hercilia\CascadeProjects\ppt-libras-adapter
   ```
3. **Cole o comando** com seu token
4. **Pressione Enter**

**Em 2 minutos sua agenda estará online!**
