#!/usr/bin/python3
"""	
1. Install Required Libraries:
pip install requests

2. Run the Proxy Server:
python web_proxy_server.py

3. Test Your Proxy:
Open a web browser and configure it to use localhost:8080 as the proxy server. (localhost/Server IP Address)
Try accessing a website by entering its full URL (e.g., http://example.com) in the browser's address bar.

"""

import http.server
import socketserver
import requests

PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  # Remove the leading '/'
        try:
            response = requests.get(url)
            self.send_response(response.status_code)
            self.send_header('Content-type', response.headers['Content-Type'])
            self.end_headers()
            self.wfile.write(response.content)
        except Exception as e:
            self.send_error(500, f"Error: {e}")

with socketserver.TCPServer(("", PORT), Proxy) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
