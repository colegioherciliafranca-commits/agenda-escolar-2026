#!/usr/bin/env python3
import requests
import json
import time
import os
from typing import Optional, Dict, Any

class VLibrasService:
    """Serviço de integração com a API oficial do VLibras"""
    
    def __init__(self):
        self.base_url = "https://api.vlibras.gov.br"
        self.translate_endpoint = "/translate"
        self.video_endpoint = "/video"
        self.timeout = 30
        
    def translate_text_to_glosa(self, text: str, regionalism: str = "PB") -> Optional[Dict[str, Any]]:
        """
        Traduz texto em português para glosa em Libras
        
        Args:
            text: Texto em português para traduzir
            regionalism: Regionalismo (PB, RJ, SP, etc)
            
        Returns:
            Dicionário com a glosa ou None em caso de erro
        """
        try:
            url = f"{self.base_url}{self.translate_endpoint}"
            payload = {
                "text": text,
                "regionalism": regionalism
            }
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            
            response = requests.post(
                url, 
                json=payload, 
                headers=headers, 
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro na tradução: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão com VLibras API: {e}")
            return None
    
    def generate_video_from_glosa(self, glosa: str, regionalism: str = "PB") -> Optional[str]:
        """
        Gera vídeo em Libras a partir da glosa
        
        Args:
            glosa: Texto em glosa Libras
            regionalism: Regionalismo (PB, RJ, SP, etc)
            
        Returns:
            URL do vídeo gerado ou None em caso de erro
        """
        try:
            url = f"{self.base_url}{self.video_endpoint}"
            payload = {
                "glosa": glosa,
                "regionalism": regionalism,
                "format": "mp4"
            }
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            
            response = requests.post(
                url, 
                json=payload, 
                headers=headers, 
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("video_url")
            else:
                print(f"Erro na geração de vídeo: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão com VLibras API: {e}")
            return None
    
    def translate_and_generate_video(self, text: str, regionalism: str = "PB") -> Optional[str]:
        """
        Processo completo: traduz texto para glosa e gera vídeo
        
        Args:
            text: Texto em português
            regionalism: Regionalismo
            
        Returns:
            URL do vídeo ou None em caso de erro
        """
        # Primeiro traduz para glosa
        glosa_result = self.translate_text_to_glosa(text, regionalism)
        if not glosa_result:
            return None
        
        glosa_text = glosa_result.get("glosa", "")
        if not glosa_text:
            return None
        
        # Depois gera o vídeo
        video_url = self.generate_video_from_glosa(glosa_text, regionalism)
        return video_url
    
    def get_available_signs(self) -> Optional[Dict[str, Any]]:
        """
        Obtém a lista de sinais disponíveis no dicionário
        
        Returns:
            Dicionário com os sinais ou None em caso de erro
        """
        try:
            url = f"{self.base_url}/dictionary"
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro ao obter dicionário: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
            return None

# Serviço alternativo usando VLibras Vídeo (mais robusto)
class VLibrasVideoService:
    """Serviço alternativo usando VLibras Vídeo para tradução"""
    
    def __init__(self):
        self.base_url = "https://video.vlibras.gov.br"
        self.api_url = "https://api.video.vlibras.gov.br"
        
    def create_translation_request(self, text: str) -> Optional[str]:
        """
        Cria uma solicitação de tradução via API do VLibras Vídeo
        
        Args:
            text: Texto para traduzir
            
        Returns:
            ID da solicitação ou None em caso de erro
        """
        try:
            # Esta é uma implementação simulada baseada na documentação
            # A API real pode requerer autenticação via gov.br
            url = f"{self.api_url}/translate"
            payload = {
                "text": text,
                "source_language": "pt-BR",
                "target_language": "libras"
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("request_id")
            else:
                print(f"Erro na solicitação: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Erro ao criar solicitação: {e}")
            return None
    
    def get_translation_status(self, request_id: str) -> Optional[Dict[str, Any]]:
        """
        Verifica o status de uma tradução
        
        Args:
            request_id: ID da solicitação
            
        Returns:
            Status da tradução ou None
        """
        try:
            url = f"{self.api_url}/status/{request_id}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
                
        except Exception as e:
            print(f"Erro ao verificar status: {e}")
            return None

# Função para obter o serviço VLibras ativo
def get_vlibras_service():
    """Retorna a melhor implementação do serviço VLibras disponível"""
    # Tenta usar a API oficial primeiro
    try:
        service = VLibrasService()
        # Testa se a API está respondendo
        if service.get_available_signs():
            return service
    except:
        pass
    
    # Fallback para o serviço alternativo
    return VLibrasVideoService()

# Função de tradução simplificada para uso no projeto
def translate_text_for_libras(text: str, max_length: int = 500) -> Optional[Dict[str, Any]]:
    """
    Traduz texto para Libras usando VLibras Widget (fallback funcional)
    
    Args:
        text: Texto para traduzir
        max_length: Comprimento máximo do texto
        
    Returns:
        Dicionário com informações da tradução ou None
    """
    # Limita o tamanho do texto para evitar problemas
    if len(text) > max_length:
        text = text[:max_length] + "..."
    
    # Como a API oficial não está acessível, usar VLibras Widget
    # Retornar informações para o frontend usar o Widget
    return {
        "method": "widget",
        "text": text,
        "widget_url": "https://vlibras.gov.br/app",
        "instructions": "Use VLibras Widget para tradução",
        "success": True
    }

def create_libras_widget_content(text: str) -> str:
    """
    Cria conteúdo HTML para VLibras Widget
    
    Args:
        text: Texto para traduzir
        
    Returns:
        HTML com VLibras Widget configurado
    """
    return f"""
    <div vw class="enabled" vw-access-button="true" vw-plugin-wrapper="true">
        <div vw-plugin-name="VP" class="active" vw-access-button="true" vw-plugin-wrapper="true">
            <div vw-plugin-wrapper="true">
                <div vw-plugin-name="VP" vw-access-button="true"></div>
            </div>
        </div>
    </div>
    <script>
        // Configurar texto para tradução
        window.vlibrasText = "{text}";
        // Inicializar VLibras
        if (window.VLibras) {{
            new window.VLibras.Widget('https://vlibras.gov.br/app');
        }}
    </script>
    """
