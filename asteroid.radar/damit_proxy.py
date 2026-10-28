from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re
import ssl
import truststore

SSL_CONTEXT = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        match = re.fullmatch(r"/damit/(\d+)/shape\.obj", self.path)

        if not match:
            self.send_error(404, "Unknown model URL")
            return

        model_id = match.group(1)
        url = (
            "https://damit.cuni.cz/projects/damit/generated_files/"
            f"open/AsteroidModel/{model_id}/shape.obj"
        )

        try:
            request = Request(url, headers={"User-Agent": "AsteroidRadar/1.0"})
            with urlopen(request, timeout=30, context=SSL_CONTEXT) as response:
                model_data = response.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(model_data)))
            self.end_headers()
            self.wfile.write(model_data)

        except (HTTPError, URLError, TimeoutError) as error:
            message = f"Could not retrieve DAMIT model: {error}".encode()
            self.send_response(502)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(message)))
            self.end_headers()
            self.wfile.write(message)

    def log_message(self, format, *args):
        print(*args)

print("DAMIT helper is running at http://localhost:8000")
HTTPServer(("localhost", 8000), ProxyHandler).serve_forever()