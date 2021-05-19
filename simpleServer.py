from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

with TCPServer(("", 8000), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
