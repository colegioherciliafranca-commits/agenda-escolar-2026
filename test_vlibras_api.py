#!/usr/bin/env python3
"""
Teste direto da API VLibras para verificar funcionamento
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vlibras_service import VLibrasService, translate_text_for_libras
import requests
import json

def test_vlibras_direct():
    """Teste direto da API VLibras"""
    print("=== Teste Direto da API VLibras ===")
    
    # Teste 1: Verificar se a API base está respondendo
    print("\n1. Testando conectividade com API base...")
    try:
        response = requests.get("https://api.vlibras.gov.br", timeout=10)
        print(f"   Status API Base: {response.status_code}")
    except Exception as e:
        print(f"   Erro API Base: {e}")
    
    # Teste 2: Tentar usar o serviço VLibras
    print("\n2. Testando serviço VLibras...")
    try:
        service = VLibrasService()
        print("   Serviço VLibras criado com sucesso")
        
        # Teste com texto simples
        test_text = "Olá mundo. Como você está?"
        print(f"   Texto para traduzir: '{test_text}'")
        
        result = service.translate_text_to_glosa(test_text)
        if result:
            print(f"   Tradução para glosa: {result}")
        else:
            print("   Falha na tradução para glosa")
            
    except Exception as e:
        print(f"   Erro no serviço VLibras: {e}")
    
    # Teste 3: Tentar tradução completa
    print("\n3. Testando tradução completa...")
    try:
        video_url = translate_text_for_libras("Bom dia a todos")
        if video_url:
            print(f"   URL do vídeo: {video_url}")
        else:
            print("   Falha na geração de vídeo")
    except Exception as e:
        print(f"   Erro na tradução completa: {e}")

def test_alternative_endpoints():
    """Testar endpoints alternativos do VLibras"""
    print("\n=== Testando Endpoints Alternativos ===")
    
    endpoints = [
        "https://vlibras.gov.br/api/translate",
        "https://video.vlibras.gov.br/api/translate",
        "https://api.video.vlibras.gov.br/translate",
        "https://www.vlibras.gov.br/api/translate"
    ]
    
    test_payload = {
        "text": "Olá mundo",
        "source_language": "pt-BR",
        "target_language": "libras"
    }
    
    for endpoint in endpoints:
        print(f"\nTestando: {endpoint}")
        try:
            response = requests.post(endpoint, json=test_payload, timeout=10)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                print(f"   Resposta: {response.text[:200]}...")
            else:
                print(f"   Erro: {response.text[:200]}...")
        except Exception as e:
            print(f"   Falha: {e}")

def test_vlibras_widget():
    """Testar se o VLibras Widget está disponível"""
    print("\n=== Testando VLibras Widget ===")
    
    try:
        response = requests.get("https://vlibras.gov.br/app/vlibras-plugin.js", timeout=10)
        print(f"Status VLibras Widget: {response.status_code}")
        if response.status_code == 200:
            print("Widget VLibras disponível")
        else:
            print("Widget VLibras não disponível")
    except Exception as e:
        print(f"Erro ao testar Widget: {e}")

if __name__ == "__main__":
    print("Iniciando testes da API VLibras...")
    
    test_vlibras_direct()
    test_alternative_endpoints()
    test_vlibras_widget()
    
    print("\n=== Testes Concluídos ===")
    print("\nRecomendações:")
    print("1. Se a API oficial não funcionar, usar VLibras Widget como fallback")
    print("2. Implementar sistema de tentativas múltiplas")
    print("3. Adicionar tratamento robusto de erros")
    print("4. Considerar usar VLibras Vídeo para tradução de vídeo")
