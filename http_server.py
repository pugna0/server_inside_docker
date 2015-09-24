from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
__author__ = 'pugna'

class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        buf = "It works"
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)
        print "~~~~~~"
        """
        print dir(self.headers)
        print self.headers.items()
        print self.headers.keys()
        print self.headers.has_key("range")

        print self.headers.values()
        print self.headers.getplist()
        """
        seek_size = 0
        for content in self.headers.items():
            if content[0] == "range":
                off_set = content[1].split("=")[1]
                seek_size = int(off_set.split("-")[0])
                print seek_size
        print "~~~~~~"
        self.send_header("header", "Content")
        self.end_headers()
        if self.path.split("/")[1] == "sent_test":

            f = open("/home/pugna/sent_test", "rb")
            if seek_size:
                f.seek(seek_size)
                print f.tell()
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
