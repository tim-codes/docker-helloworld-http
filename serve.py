import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the hostname for the HTML content
hostname = os.uname().nodename

# HTML content template
html_content = f"""<html>
<head>
    <title>HTTP Hello World</title>
</head>
<body>
    <h1>Hello from {hostname}</h1>
</body>
</html>
"""

# Custom HTTP request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Send the HTML content
        self.wfile.write(html_content.encode("utf-8"))

# Get the port from the environment variable, default to 80
PORT = int(os.getenv("PORT", 80))

# Server setup
server_address = ("", PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f"Serving on port {PORT}...")
httpd.serve_forever()
