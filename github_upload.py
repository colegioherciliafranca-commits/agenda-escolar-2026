#!/usr/bin/env python3
"""
Upload automático para GitHub usando GitHub API
Requer: pip install requests
"""

import requests
import json
import base64
import os
from pathlib import Path

# Configurações
REPO_OWNER = "colegioherciliafranca-commits"
REPO_NAME = "agenda-escolar-2026"
GITHUB_TOKEN = "SEU_TOKEN_AQUI"  # Você precisa gerar um token no GitHub

class GitHubUploader:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_file_content(self, file_path):
        """Ler conteúdo do arquivo em base64"""
        with open(file_path, "rb") as f:
            content = f.read()
        return base64.b64encode(content).decode('utf-8')
    
    def create_or_update_file(self, file_path, content, message):
        """Criar ou atualizar arquivo no repositório"""
        url = f"{self.base_url}/contents/{file_path}"
        
        data = {
            "message": message,
            "content": content
        }
        
        # Verificar se arquivo já existe
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                data["sha"] = response.json()["sha"]
        except:
            pass
        
        response = requests.put(url, headers=self.headers, json=data)
        return response.status_code == 200 or response.status_code == 201
    
    def upload_files(self):
        """Fazer upload dos arquivos necessários"""
        files_to_upload = [
            ("agenda_escolar.html", "Adicionar agenda escolar completa"),
            ("README.md", "Adicionar documentação do projeto"),
            ("DEPLOY.md", "Adicionar guia de deploy")
        ]
        
        success_count = 0
        
        for file_name, commit_message in files_to_upload:
            print(f"📤 Upload de {file_name}...")
            
            # Ler arquivo README_AGENDA.md e renomear para README.md
            if file_name == "README.md":
                if os.path.exists("README_AGENDA.md"):
                    content = self.get_file_content("README_AGENDA.md")
                else:
                    print(f"❌ Arquivo README_AGENDA.md não encontrado")
                    continue
            else:
                if os.path.exists(file_name):
                    content = self.get_file_content(file_name)
                else:
                    print(f"❌ Arquivo {file_name} não encontrado")
                    continue
            
            if self.create_or_update_file(file_name, content, commit_message):
                print(f"✅ {file_name} uploaded com sucesso!")
                success_count += 1
            else:
                print(f"❌ Falha no upload de {file_name}")
        
        return success_count == len(files_to_upload)
    
    def enable_github_pages(self):
        """Ativar GitHub Pages para o repositório"""
        url = f"{self.base_url}/pages"
        
        data = {
            "source": {
                "branch": "main",
                "path": "/"
            }
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        return response.status_code == 201

def main():
    print("=" * 60)
    print("🚀 UPLOAD AUTOMÁTICO PARA GITHUB PAGES")
    print("=" * 60)
    
    # Verificar se token foi configurado
    if GITHUB_TOKEN == "SEU_TOKEN_AQUI":
        print("❌ ERRO: Você precisa configurar seu GitHub Token!")
        print("\n📋 Como gerar token:")
        print("1. Acesse: https://github.com/settings/tokens")
        print("2. Clique em 'Generate new token'")
        print("3. Selecione 'repo' scope")
        print("4. Copie o token gerado")
        print("5. Substitua 'SEU_TOKEN_AQUI' no código")
        return
    
    # Mudar para diretório do script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Verificar arquivos necessários
    required_files = ["agenda_escolar.html", "README_AGENDA.md", "DEPLOY.md"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Arquivos não encontrados: {missing_files}")
        return
    
    # Fazer upload
    uploader = GitHubUploader(GITHUB_TOKEN)
    
    print("📤 Iniciando upload dos arquivos...")
    if uploader.upload_files():
        print("✅ Todos os arquivos uploaded com sucesso!")
        
        print("\n🌐 Ativando GitHub Pages...")
        if uploader.enable_github_pages():
            print("✅ GitHub Pages ativado!")
            
            url = f"https://{REPO_OWNER}.github.io/{REPO_NAME}/agenda_escolar.html"
            print(f"\n🎉 SUCESSO!")
            print(f"📱 URL da Agenda: {url}")
            print(f"⏰ Aguarde 2-3 minutos para o site ficar online")
        else:
            print("❌ Falha ao ativar GitHub Pages")
            print("💡 Ative manualmente em Settings > Pages")
    else:
        print("❌ Falha no upload dos arquivos")

if __name__ == "__main__":
    main()
