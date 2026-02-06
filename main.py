"""Simple local server for the Fun Route Adventure demo."""
from __future__ import annotations

import http.server
import socketserver
from pathlib import Path


PORT = 8000


class FunGameHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), FunGameHandler) as httpd:
        print("Fun Route Adventure running!")
        print(f"Open http://localhost:{PORT}/index.html in your browser.")
        httpd.serve_forever()
