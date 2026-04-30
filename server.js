const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');
const { PythonShell } = require('python-shell');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Configuração do Multer para upload de arquivos
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const uploadDir = 'uploads/';
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    const uniqueName = uuidv4() + path.extname(file.originalname);
    cb(null, uniqueName);
  }
});

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 50 * 1024 * 1024 // 50MB
  },
  fileFilter: function (req, file, cb) {
    const allowedTypes = ['.ppt', '.pptx'];
    const fileExt = path.extname(file.originalname).toLowerCase();
    if (allowedTypes.includes(fileExt)) {
      cb(null, true);
    } else {
      cb(new Error('Apenas arquivos .ppt e .pptx são permitidos'));
    }
  }
});

// Rotas
app.post('/api/upload', upload.single('presentation'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'Nenhum arquivo enviado' });
    }

    const filePath = req.file.path;
    const sessionId = uuidv4();
    
    // Processar o PowerPoint
    const result = await processPowerPoint(filePath, sessionId);
    
    res.json({
      success: true,
      sessionId: sessionId,
      slides: result.slides,
      message: 'Apresentação processada com sucesso'
    });
  } catch (error) {
    console.error('Erro no upload:', error);
    res.status(500).json({ error: 'Erro ao processar o arquivo' });
  }
});

app.get('/api/slides/:sessionId', (req, res) => {
  try {
    const { sessionId } = req.params;
    const slidesPath = path.join('processed', sessionId, 'slides.json');
    
    if (fs.existsSync(slidesPath)) {
      const slides = JSON.parse(fs.readFileSync(slidesPath, 'utf8'));
      res.json({ slides });
    } else {
      res.status(404).json({ error: 'Sessão não encontrada' });
    }
  } catch (error) {
    console.error('Erro ao buscar slides:', error);
    res.status(500).json({ error: 'Erro ao buscar slides' });
  }
});

// Função para processar PowerPoint
async function processPowerPoint(filePath, sessionId) {
  return new Promise((resolve, reject) => {
    const options = {
      mode: 'text',
      pythonPath: 'python',
      pythonOptions: ['-u'],
      scriptPath: './python',
      args: [filePath, sessionId]
    };

    PythonShell.run('process_ppt.py', options, function (err, results) {
      if (err) {
        console.error('Erro no Python:', err);
        reject(err);
        return;
      }
      
      try {
        const result = JSON.parse(results[0]);
        resolve(result);
      } catch (parseError) {
        console.error('Erro ao parsear resultado:', parseError);
        reject(parseError);
      }
    });
  });
}

// Servir arquivos estáticos do cliente
app.use(express.static(path.join(__dirname, 'client/build')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
