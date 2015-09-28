from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import zlib
import pycurl
from StringIO import StringIO
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
        file_response = ''
        if self.headers.get('Range', None):
            seek_size = int((self.headers.get('Range', None).split("=")[1]).split("-")[0])

            buff = self.get_file_from_agent(self.path.split("/")[1], seek_size)
            file_response = self.decompress(buff, self.headers.get('compress_size', None))
        else:
            buff = self.get_file_from_agent(self.path.split("/")[1], 0)
            file_response = self.decompress(buff, self.headers.get('compress_size', None))

        print "~~~~~~"
#       self.send_header("header", "Content")
        self.end_headers()

    @staticmethod
    def get_file_from_agent(self, dir_, seek_size):
        c = pycurl.Curl()
        url = "127.0.0.1:8765/" + dir_
        c.setopt(c.URL, url)
        buffer_ = StringIO()
        if seek_size:
            c.setopt(pycurl.RESUME_FROM_LARGE, seek_size)
        c.setopt(c.WRITEDATA, buffer_)
        c.perform()
        return buffer_

    @staticmethod
    def decompress(self, str, decom_size):
        dst_file = ''
        with open(str, 'rb') as f:
            for i in range(1, 11):
                content = f.read(decom_size)
                f.seek(decom_size*i)
                dezip_str = zlib.decompress(content)
                dst_file += dezip_str
        return dst_file


def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8766)

"""
c = pycurl.Curl()
c.setopt(pycurl.RESUME_FROM_LARGE, location)
"""