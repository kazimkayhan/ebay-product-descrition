#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler

print(f"Server running at http://localhost:{PORT}/")
print(f"Serving from: {os.getcwd()}")
print("Press Ctrl+C to stop the server")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
