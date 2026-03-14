#!/usr/bin/env python3
import http.server
import socketserver
import os
from pathlib import Path

# Change to project directory
os.chdir(Path(__file__).parent)

PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
