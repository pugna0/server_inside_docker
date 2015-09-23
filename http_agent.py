from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
__author__ = 'pugna'

class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        pass

    def compress(self):
        pass

    def slice_blk(self):
        pass

def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8765)
