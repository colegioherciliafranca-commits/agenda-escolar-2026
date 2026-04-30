import requests
import json
import time
from typing import Optional, Dict, Any

class HandTalkTranslator:
    """
    Integração com Hand Talk API para tradução em Libras
    Documentação: https://api-docs.handtalk.me/v1/
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.base_url = "https://api.handtalk.me/v1"
        self.sdk_url = "https://cdn.handtalk.me/handtalk-sdk/latest/handtalk-sdk.js"
        
    def translate_text(self, text: str, language: str = "pt-br") -> Dict[str, Any]:
        """
        Traduz texto para Libras usando Hand Talk API
        
        Args:
            text: Texto para traduzir (máx 1000 caracteres)
            language: Idioma de origem (pt-br ou en-us)
            
        Returns:
            Dicionário com resultado da tradução
        """
        if len(text) > 1000:
            text = text[:1000]  # Limitar para 1000 caracteres
            
        if not self.api_key:
            return self._simulate_translation(text)
            
        # Implementação real com API key
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "source_language": language,
            "target_language": "libras"
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/translate",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API Error: {response.status_code}", "details": response.text}
                
        except Exception as e:
            return {"error": "Connection Error", "details": str(e)}
    
    def _simulate_translation(self, text: str) -> Dict[str, Any]:
        """
        Simulação de tradução para demonstração
        Remove quando tiver API key real
        """
        # Dicionário básico de tradução
        translations = {
            "bom": "BOM",
            "dia": "DIA", 
            "biologia": "BIOLOGIA",
            "célula": "CÉLULA",
            "vegetal": "VEGETAL",
            "aula": "AULA",
            "primeira": "1ª",
            "série": "SÉRIE",
            "todos": "TODOS",
            "sejam": "SER",
            "bem-vindos": "BEM-VINDO",
            "nossa": "NOSSO",
            "para": "PARA",
            "em": "EM",
            "de": "DE",
            "e": "E",
            "ou": "OU",
            "mas": "MAS",
            "com": "COM",
            "sem": "SEM",
            "por": "POR",
            "que": "QUE"
        }
        
        # Processar texto
        words = text.lower().replace(/[.,!?;:]/g, ' ').split()
        translated = []
        
        for word in words:
            if word in translations:
                translated.append(translations[word])
            else:
                translated.append(word.upper())
        
        return {
            "success": True,
            "original_text": text,
            "translated_text": " ".join(translated),
            "gloss": " ".join(translated),
            "word_count": len(words),
            "character_count": len(text),
            "simulation": True
        }
    
    def generate_html_widget(self, text: str, container_id: str = "handtalk-container") -> str:
        """
        Gera código HTML para embed do widget Hand Talk
        """
        return f"""
        <div id="{container_id}" style="width: 100%; height: 400px; border: 2px solid #28a745; border-radius: 10px; margin: 20px 0;">
            <div style="padding: 20px; text-align: center;">
                <h3>Hand Talk Avatar</h3>
                <p>Traduzindo: "{text[:50]}{'...' if len(text) > 50 else ''}"</p>
                <div id="handtalk-avatar" style="width: 300px; height: 300px; margin: 0 auto; background: #f8f9fa; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                    <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="#28a745" stroke-width="2">
                        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
                        <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                        <line x1="12" y1="19" x2="12" y2="23"></line>
                        <line x1="8" y1="23" x2="16" y2="23"></line>
                    </svg>
                </div>
                <p style="margin-top: 15px; color: #6c757d;">
                    <strong>Glosa:</strong> {self.translate_text(text).get('gloss', 'Tradução em andamento...')}
                </p>
            </div>
        </div>
        
        <script src="{self.sdk_url}"></script>
        <script>
            // Inicialização do Hand Talk SDK
            window.addEventListener('load', function() {{
                try {{
                    if (window.HandTalk) {{
                        const handtalk = new window.HandTalk.SDK({{
                            apiKey: '{self.api_key or "demo-key"}',
                            language: 'pt-br',
                            targetLanguage: 'libras'
                        }});
                        
                        handtalk.translate('{text}', {{
                            container: '{container_id}',
                            avatar: {{
                                visible: true,
                                position: 'center'
                            }}
                        }});
                    }}
                }} catch (error) {{
                    console.log('Hand Talk SDK loading...', error);
                }}
            }});
        </script>
        """

# Exemplo de uso
if __name__ == "__main__":
    translator = HandTalkTranslator()
    
    # Teste de tradução
    result = translator.translate_text("BIOLOGIA 1ª SÉRIE CÉLULA VEGETAL AULA 16")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Gerar HTML
    html_widget = translator.generate_html_widget("BIOLOGIA 1ª SÉRIE CÉLULA VEGETAL AULA 16")
    print("\nHTML Widget gerado com sucesso!")
