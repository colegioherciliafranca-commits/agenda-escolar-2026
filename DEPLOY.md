# Como Disponibilizar a Agenda Escolar Online Gratuitamente

## 🚀 Opção 1: GitHub Pages (Recomendado)

### Passos:
1. **Criar conta no GitHub**: https://github.com
2. **Criar novo repositório**: `agenda-escolar-2026`
3. **Fazer upload dos arquivos**:
   - `agenda_escolar.html`
   - (se houver outras imagens/css)

4. **Ativar GitHub Pages**:
   - Vá em Settings → Pages
   - Selecione "Deploy from a branch"
   - Escolha branch `main` e pasta `/root`
   - Salve

5. **Acessar**: `https://[seu-usuario].github.io/agenda-escolar-2026`

---

## 🚀 Opção 2: Netlify

### Passos:
1. **Criar conta**: https://netlify.com
2. **Arrastar pasta** do projeto para o site
3. **Site publicado automaticamente**
4. **URL**: `https://[nome-aleatorio].netlify.app`

---

## 🚀 Opção 3: Vercel

### Passos:
1. **Criar conta**: https://vercel.com
2. **Importar projeto** do GitHub
3. **Deploy automático**
4. **URL**: `https://[projeto].vercel.app`

---

## 🚀 Opção 4: Servidor Local (Rede Escola)

### Requisitos:
- Computador ligado na escola
- Node.js instalado
- Acesso à rede interna

### Passos:
1. **Instalar Node.js**: https://nodejs.org
2. **Criar servidor simples**:
```bash
npm install -g http-server
http-server -p 8080 -c-1
```

3. **Acessar na rede**: `http://[IP-do-servidor]:8080`

---

## 📱 Acesso Móvel

Para facilitar acesso em celulares:
- Adicionar atalho na tela inicial
- Criar QR Code com o link
- Compartilhar link via WhatsApp

---

## 🔧 Manutenção

- **Backup semanal** dos dados (localStorage)
- **Atualizações** via upload de arquivos
- **Monitoramento** de acesso

---

## 💡 Dicas Importantes

1. **Dados salvos localmente** (no navegador) - não se perdem ao atualizar a página
2. **Para backup**: exportar dados do localStorage periodicamente
3. **Para múltiplos usuários**: cada um terá suas próprias reuniões
4. **Para compartilhar**: todos veem os eventos oficiais, mas cada um adiciona suas reuniões

---

## 🎯 Recomendação Final

**GitHub Pages** é a melhor opção porque:
- ✅ Totalmente gratuito
- ✅ Sem anúncios  
- ✅ Rápido e confiável
- ✅ Fácil de atualizar
- ✅ Acesso de qualquer lugar
- ✅ HTTPS automático
