from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
__author__ = 'pugna'

class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        buf = "It works"
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)

        if self.path == "sent_test":
            f = open("/home/pugna/sent_test", "rb")
            self.wfile.write(f.read())
            f.close()



    def get_file_from_agent(self):
        pass


    def cache_file(self):
        pass


def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8765)
