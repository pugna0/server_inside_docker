from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import zlib
import os


__author__ = 'pugna'


WORK_DIR = '/home/pugna/'


class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)
        seek_size = 0
        if self.headers.get('Range', None):
            seek_size = int((self.headers.get('Range', None).split("=")[1]).split("-")[0])
        self.send_file(seek_size)
        print "~~~~~~"

    def send_file(self, seek_size):
        path = self.path.split("/")[1]
        buff = self.construct_file(path, seek_size)
        self.end_headers()
        #print buff
        self.wfile.write(buff)

    @staticmethod
    def compress(str):
        zip_str = zlib.compress(str)
        zip_len = len(zip_str)
        return zip_str, zip_len

    def construct_file(self, path, start_pos=0):
        path = WORK_DIR + path
        f = open(path, "rb")
        size = os.path.getsize(path)
        if start_pos >= size:
            return None, 0
        send_file = ''
        compress_size = 0
        if start_pos:
            f.seek(start_pos)
            read_size = size / 10
            if size % 10 != 0:
                read_size = size/10 + 1
            for i in range(1, 11):
                tmp = f.read(read_size)
                com_str, com_size = self.compress(tmp)
                send_file += com_str
                f.seek(i * read_size + start_pos)
        else:
            read_size = size / 10
            if size % 10 != 0:
                read_size = size/10 + 1
            for i in range(1, 11):
                tmp = f.read(read_size)
                com_str = self.compress(tmp)
                send_file += com_str
                f.seek(i * read_size)
            compress_size = read_size
        self.send_header("compress_size", compress_size)
        return send_file, compress_size


def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8765)

