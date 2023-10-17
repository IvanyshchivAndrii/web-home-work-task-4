
from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

    def do_POST(self):
        pass

    def send_html(self, file, response):
        self.send_response(response)
        self.send_header('Content_Type', 'text/html')
        self.end_headers()
        with open(file, 'rb') as file:
            self.wfile.write(file.read())


def run_server():
    address = ('localhost', 3000)
    http_server = HTTPServer(address, MyHTTPRequestHandler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    run_server()
