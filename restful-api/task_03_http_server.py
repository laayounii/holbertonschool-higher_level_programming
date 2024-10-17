#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        # Set response for the root endpoint "/"
        if self.path == '/':
            self.send_response(200)  # OK status
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # Handle /data endpoint
        elif self.path == '/data':
            self.send_response(200)  # OK status
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Sample JSON data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Handle /status endpoint
        elif self.path == '/status':
            self.send_response(200)  # OK status
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            status = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status).encode('utf-8'))

        # Handle undefined endpoints (404 Not Found)
        else:
            self.send_response(404)  # Not Found status
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            error_message = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Define the main function to run the server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

# If this script is executed, run the server
if __name__ == '__main__':
    run()
