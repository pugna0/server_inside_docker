from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import zlib
import pycurl
from StringIO import StringIO
import httplib

__author__ = 'pugna'


class Storage:
    def __init__(self):
        self.contents = ''
        self.line = 0

    def store(self, buf):
        self.line = self.line + 1
        self.contents = "%s%i: %s" % (self.contents, self.line, buf)

    def __str__(self):
        return self.contents


class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
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
        file_response = ''
        if self.headers.get('Range', None):
            seek_size = int((self.headers.get('Range', None).split("=")[1]).split("-")[0])

            buff, compress_size = self.get_file_from_agent(self.path.split("/")[1], seek_size)
            file_response = self.decompress_(buff, int(compress_size))
        else:
            buff, compress_size = self.get_file_from_agent(self.path.split("/")[1], 0)
            file_response = self.decompress_(buff, int(compress_size))
        print file_response
        print "~~~~~~"
#       self.send_header("header", "Content")
        self.end_headers()

    @staticmethod
    def get_file_from_agent1(dir_, seek_size):
        #retrieved_body = Storage()
        #retrieved_headers = Storage()

        c = pycurl.Curl()
        url = "127.0.0.1:8765/" + dir_
        c.setopt(c.URL, url)
        buffer_ = StringIO()
        if seek_size:
            c.setopt(pycurl.RESUME_FROM_LARGE, seek_size)
        c.setopt(c.WRITEDATA, buffer_)
        #c.setopt(c.WRITEFUNCTION, retrieved_body.store)
        #c.setopt(c.HEADERFUNCTION, retrieved_headers.store)
        c.perform()
        c.close()
        #print retrieved_body
        print buffer_
        return buffer_


    @staticmethod
    def get_file_from_agent(dir_, seek_size):
        url = "http://127.0.0.1:8765/" + dir_
        header_data = ''
        conn = httplib.HTTPConnection("127.0.0.1")
        res = ''
        compress_size = 0
        if seek_size:
            #conn.putheader("Range", seek_size)
            header_data = {"range": seek_size}
        try:
            conn.request(method="GET", url=url, headers=header_data)
            response = conn.getresponse()
            compress_size = response.getheader("compress_size", 0)
            res = response.read()
        except Exception, e:
            print e
        finally:
            conn.close()

        print res

        return res, compress_size

    @staticmethod
    def decompress_(str_, decom_size):
        dst_file = ''
        print str_
        for i in range(1, 11):
            content = str_[decom_size*(i-1):decom_size*i]
            dezip_str = zlib.decompress(content)
            dst_file += dezip_str
        return dst_file


def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8766)
