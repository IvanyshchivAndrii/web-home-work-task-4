import urllib.parse
from pathlib import Path
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = Path()


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        print(route)
        match route.path:
            case '/':
                self.send_html('index.html')
            case '/message':
                self.send_html('message.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():
                    self.send_statics(file)
                else:
                    self.send_html('error.html', 404)

    def do_POST(self):
        pass

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content_Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_statics(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, other = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content_Type', mime_type)
        else:
            self.send_header('Content_Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as file:
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
