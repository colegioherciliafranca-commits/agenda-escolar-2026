# Adaptador PowerPoint para Libras

Uma aplicação web que transforma apresentações PowerPoint em conteúdo acessível para pessoas surdas, com integração com VLibras para tradução em Língua Brasileira de Sinais.

## Funcionalidades

- Upload de arquivos PowerPoint (.ppt, .pptx)
- Extração e simplificação automática de texto
- Interface acessível com navegação por slides
- Integração com VLibras para tradução em Libras
- Texto simplificado para melhor compreensão
- Design responsivo e moderno

## Tecnologias Utilizadas

### Backend
- Node.js com Express
- Python com python-pptx para processamento de PowerPoint
- Multer para upload de arquivos
- Python Shell para integração Node-Python

### Frontend
- React 18
- React Dropzone para upload
- Axios para comunicação com API
- VLibras Plugin para tradução em Libras

## Instalação e Execução

### Pré-requisitos
- Node.js 16+
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Passos

1. **Clonar o projeto**
```bash
cd ppt-libras-adapter
```

2. **Instalar dependências do backend**
```bash
npm install
```

3. **Instalar dependências Python**
```bash
pip install -r requirements.txt
```

4. **Instalar dependências do frontend**
```bash
cd client
npm install
cd ..
```

5. **Executar em modo desenvolvimento**
```bash
# Terminal 1 - Backend
npm run dev

# Terminal 2 - Frontend  
npm run client
```

6. **Acessar a aplicação**
Abra http://localhost:3000 no navegador

## Estrutura do Projeto

```
ppt-libras-adapter/
âââ client/                 # Frontend React
â   âââ public/
â   âââ src/
â       âââ components/    # Componentes React
â       âââ services/      # Serviços API
â       âââ App.js
â       âââ index.js
âââ python/                # Scripts Python
â   âââ process_ppt.py     # Processamento de PowerPoint
âââ uploads/               # Arquivos temporários
âââ processed/             # Slides processados
âââ server.js              # Servidor Node.js
âââ package.json
âââ requirements.txt
âââ README.md
```

## Como Funciona

1. **Upload**: O usuário faz upload de uma apresentação PowerPoint
2. **Processamento**: O script Python extrai texto, imagens e notas dos slides
3. **Simplificação**: O texto é simplificado para torná-lo mais acessível
4. **Interface**: Os slides são exibidos em uma interface navegável
5. **Libras**: Botão para ativar tradução em Libras via VLibras

## API Endpoints

- `POST /api/upload` - Upload e processamento de apresentação
- `GET /api/slides/:sessionId` - Recuperar slides processados

## Características de Acessibilidade

- Texto simplificado e de fácil compreensão
- Navegação por teclado
- Design com alto contraste
- Tradução em Libras integrada
- Estrutura semântica HTML5

## Limitações

- Tamanho máximo de arquivo: 50MB
- Formatos suportados: .ppt, .pptx
- Requer conexão com internet para VLibras

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.

## Licença

MIT License
