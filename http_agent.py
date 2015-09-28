from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import zlib
__author__ = 'pugna'

class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        buf = "It works"
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)
        print self.headers.get('Range', None)
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
        if self.headers.get('Range', None):
            seek_size = int((self.headers.get('Range', None).split("=")[1]).split("-")[0])
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

    def compress(self, str):
        zip_str = zlib.compress(str)
        zip_len = len(zip_str)
        return zip_str, zip_len
    def slice_blk(self):
        pass

def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8765)
