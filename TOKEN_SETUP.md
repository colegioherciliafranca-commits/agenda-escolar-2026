# Como Gerar GitHub Token Automático

## 🔑 Passo a Passo Rápido

### 1. Acessar GitHub Tokens
- Abra: https://github.com/settings/tokens
- Faça login se necessário

### 2. Gerar Novo Token
1. Clique em **"Generate new token"** → **"Generate new token (classic)"**
2. **Note**: Digite "Agenda Escolar Deploy"
3. **Expiration**: Selecione "No expiration" ou "90 days"
4. **Scopes**: Marque **✅ repo** (isso seleciona todos os sub-itens)

### 3. Copiar Token
1. Clique em **"Generate token"**
2. **Copie o token imediatamente** (ele não aparecerá novamente!)
3. **Guarde em local seguro**

### 4. Usar no Script
1. Abra `github_upload.py`
2. Substitua `SEU_TOKEN_AQUI` pelo token copiado
3. Salve o arquivo

### 5. Executar Upload
```bash
pip install requests
python github_upload.py
```

## ⚠️ Importante

- **Segurança**: Nunca compartilhe seu token
- **Backup**: Guarde o token em local seguro
- **Permissões**: O token tem acesso total aos repositórios

## 🚀 Após Upload

O script irá:
- ✅ Upload automático dos 3 arquivos
- ✅ Ativar GitHub Pages
- ✅ Fornecer URL final

URL final: https://colegioherciliafranca-commits.github.io/agenda-escolar-2026/agenda_escolar.html
