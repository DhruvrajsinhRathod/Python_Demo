# Making a http server

from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "10.0.0.126"
PORT = 9090
class Dhruvraj(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Dhruvrajsinh Rathod</h1></body></html>","UTF-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "UTF-8"))

server = HTTPServer((HOST,PORT), Dhruvraj)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server Stopped!")