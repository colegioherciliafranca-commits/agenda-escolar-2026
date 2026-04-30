#!/usr/bin/env python3
"""
Servidor Local para Agenda Escolar
Execute este script para hospedar a agenda na rede local da escola
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

# Configurações
PORT = 8080
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Adicionar headers para melhor compatibilidade
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def get_local_ip():
    """Obter IP local para acesso na rede"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def main():
    os.chdir(DIRECTORY)
    
    # Obter IP local
    local_ip = get_local_ip()
    
    # Iniciar servidor
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("AGENDA ESCOLAR 2026 - SERVIDOR LOCAL")
        print("=" * 60)
        print(f"Diretório: {DIRECTORY}")
        print(f"Servidor iniciado em:")
        print(f"   Local: http://localhost:{PORT}")
        print(f"   Rede: http://{local_ip}:{PORT}")
        print(f"   Agenda: http://{local_ip}:{PORT}/agenda_escolar.html")
        print("=" * 60)
        print("Para acessar de outros dispositivos na mesma rede:")
        print(f"   Use: http://{local_ip}:{PORT}/agenda_escolar.html")
        print("=" * 60)
        print("Mantenha esta janela aberta para o servidor funcionar")
        print("Pressione Ctrl+C para parar o servidor")
        print("=" * 60)
        
        # Abrir navegador automaticamente
        try:
            webbrowser.open(f"http://localhost:{PORT}/agenda_escolar.html")
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor encerrado")

if __name__ == "__main__":
    main()
