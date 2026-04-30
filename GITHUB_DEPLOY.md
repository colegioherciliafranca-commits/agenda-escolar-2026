# Como Subir Agenda Escolar para GitHub Pages

## 📋 Passo a Passo Completo

### 1. Criar Conta GitHub (se não tiver)
- Acesse: https://github.com
- Clique em "Sign up"
- Preencha seus dados
- Verifique e-mail

### 2. Criar Novo Repositório
1. Faça login no GitHub
2. Clique em **"+"** no canto superior direito
3. Selecione **"New repository"**
4. Configure:
   - **Repository name**: `agenda-escolar-2026`
   - **Description**: `Agenda online interativa para Colégio Hercília`
   - **Public**: ✅ Marcado
   - **Add a README file**: ❌ Desmarcado
5. Clique em **"Create repository"**

### 3. Fazer Upload dos Arquivos
Na página do repositório criado:

1. Clique em **"uploading an existing file"**
2. **Arraste ou selecione** os seguintes arquivos:
   - `agenda_escolar.html`
   - `README_AGENDA.md` (renomeie para `README.md`)
   - `DEPLOY.md`

3. **Importante**: Renomeie `README_AGENDA.md` para `README.md`

4. Clique em **"Commit changes"**

### 4. Configurar GitHub Pages
1. No repositório, clique em **Settings**
2. No menu esquerdo, clique em **Pages**
3. Em **"Build and deployment"**:
   - **Source**: Selecione **"Deploy from a branch"**
   - **Branch**: Selecione **"main"**
   - **Folder**: Selecione **"/ (root)"**
4. Clique em **"Save"**

### 5. Aguardar Deploy
- Aguarde 1-2 minutos
- GitHub vai construir e publicar o site
- Status aparece como: "Your site is published at https://[seu-usuario].github.io/agenda-escolar-2026"

### 6. Acessar a Agenda
Seu site estará disponível em:
```
https://[seu-usuario].github.io/agenda-escolar-2026/agenda_escolar.html
```

## 🔧 Arquivos Necessários

### ✅ Arquivos para Upload:
- `agenda_escolar.html` - A agenda completa
- `README_AGENDA.md` → `README.md` - Documentação
- `DEPLOY.md` - Guia de deploy

### ❌ Arquivos que NÃO devem subir:
- `server_local.py` - Apenas para uso local
- `banner_*.png` - Arquivos vazios
- `__pycache__/` - Pasta Python
- `client/` - Pasta do projeto antigo
- `uploads/`, `processed/` - Pastas vazias

## 📱 Compartilhamento

### Para Compartilhar com a Escola:
1. **Copie a URL** do GitHub Pages
2. **Crie QR Code** com a URL
3. **Adicione aos favoritos** nos celulares
4. **Compartilhe via WhatsApp**

### URL Final Exemplo:
```
https://joaosilva.github.io/agenda-escolar-2026/agenda_escolar.html
```

## 🔄 Atualizações Futuras

### Para Atualizar a Agenda:
1. **Edite** o arquivo `agenda_escolar.html`
2. **Substitua** no GitHub (arrastando novo arquivo)
3. **Commit changes**
4. **Aguarde 1-2 minutos** para atualizar

### Para Adicionar Novas Funcionalidades:
1. **Modifique** o código HTML/CSS/JavaScript
2. **Teste localmente**
3. **Suba para GitHub**
4. **Automaticamente atualizado**

## ✅ Verificação Final

Após subir, verifique:
- [ ] Site abre corretamente
- [ ] Banner colorido aparece
- [ ] Calendário funciona
- [ ] Reuniões podem ser adicionadas
- [ ] Design responsivo no celular
- [ ] Todas as cores oficiais aparecem

## 🎯 Dicas Importantes

1. **Sempre teste localmente** antes de subir
2. **Mantenha backup** dos arquivos
3. **Use descrições claras** nos commits
4. **Compartilhe a URL** com a escola

---

## 🆘 Suporte

Se tiver problemas:
- Verifique se todos os arquivos foram subidos
- Confirme se o GitHub Pages está ativo
- Aguarde alguns minutos para o deploy completar
- Teste em navegador anônimo
