#!/usr/bin/env python3
"""Minimal HTTP server for Tekton / container smoke tests."""

import http.server
import os
import socketserver

PORT = int(os.environ.get("PORT", "8080"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        if self.path in ("/", "/health"):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"hello from python\n")
            return
        self.send_error(404)


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"listening on :{PORT}")
        httpd.serve_forever()
