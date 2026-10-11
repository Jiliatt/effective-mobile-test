from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            status = 200
            body = b"BROKWOEROKSODFOOSDFKOSKORKEAOKROVKEOSHello from Effective Mobile!\n"
        elif self.path == "/health":
            status = 200
            body = b"ok\n"
        else:
            status = 404
            body = b"Not found\n"

        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Backend running on port 8080", flush=True)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
