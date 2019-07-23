import io
import logging
import socketserver
from threading import Condition
from http import server
from stream import StreamingOutput

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.selfRedirect()
        elif self.path == '/index.html':
            self.openIndex()
        elif self.path == '/stream.mjpg':
            self.streamCamera()
        elif self.path.endswith('.js'):
            self.loadJS()
        elif self.path.endswith('.css'):
            self.loadCSS()
        elif self.path.startswith('/robot?'):
            self.moveRobot()
        elif self.path.startswith('/camera?'):
            self.moveRobot()
        else:
            self.returnError()

    def moveRobot(self):
        #/robot?direction=right&movement=false&key=ro_right_arrow
        parametersStr = self.path.split('?')
        parametersList = parametersStr[1].split('&')
        direction = parametersList[0].split('=')[1]
        print('direction -> ' + direction)
        movement = parametersList[1].split('=')[1]
        print('movement -> ' + movement)
        key = parametersList[2].split('=')[1]
        print('key -> ' + key)

    def moveCamera(self):
        #/robot?direction=right&movement=false&key=ro_right_arrow
        parametersStr = self.path.split('?')
        parametersList = parametersStr[1].split('&')
        direction = parametersList[0].split('=')[1]
        print('direction -> ' + direction)
        movement = parametersList[1].split('=')[1]
        print('movement -> ' + movement)
        key = parametersList[2].split('=')[1]
        print('key -> ' + key)

    def loadJS(self):
        file = open('scripts/js' + self.path,'rb') # open file , r => read , b => byte format
        content = file.read()
        file.close()
        self.send_response(200)
        self.send_header('Content-Type', 'text/js')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)
    
    def loadCSS(self):
        file = open('scripts/css' + self.path,'rb') # open file , r => read , b => byte format
        content = file.read()
        file.close()
        self.send_response(200)
        self.send_header('Content-Type', 'text/css')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)

    def selfRedirect(self):
        self.send_response(301)
        self.send_header('Location', '/index.html')
        self.end_headers()

    def openIndex(self):
        file = open('index.html','rb') # open file , r => read , b => byte format
        content = file.read()
        file.close()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)

    def streamCamera(self):
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
        self.end_headers()
        # try:
        #     while True:
        #         with self.output.condition:
        #             self.output.condition.wait()
        #             frame = self.output.frame
        #         self.wfile.write(b'--FRAME\r\n')
        #         self.send_header('Content-Type', 'image/jpeg')
        #         self.send_header('Content-Length', len(frame))
        #         self.end_headers()
        #         self.wfile.write(frame)
        #         self.wfile.write(b'\r\n')
        # except Exception as e:
        #     logging.warning(
        #         'Removed streaming client %s: %s',
        #         self.client_address, str(e))

    def returnError(self):
        self.send_error(404)
        self.end_headers()