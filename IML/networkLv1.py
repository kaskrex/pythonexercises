#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = 1337


class HttpHandler(BaseHTTPRequestHandler):
    # Handle HTTP Get request

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the secret token
        self.wfile.write(bytes(os.environ.get('level_1_secret_token'),"utf-8"))
        return

try:
    server = HTTPServer(('', PORT_NUMBER), HttpHandler)
    print('Webserver listening for HTTP request on:', PORT_NUMBER)
    server.serve_forever()

except Exception as err:
    print(err)
