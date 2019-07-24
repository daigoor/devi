#!/usr/bin/env python
"""server.py: SERVER."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import io
import logging
import picamera
import socketserver
import constants
from threading import Condition
from http import server
from control import Vehicle, Camera

vehicle_controls = Vehicle()
camera_controls = Camera()

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self._redirect()
        elif self.path.endswith('.ico'):
            content = self._read_file('../Favicon.ico')
            self._set_common_headers(constants.CONTENT_TYPE_JPEG, len(content))
            self.wfile.write(content)
        elif self.path.endswith('.html'):
            self.open_html()
        elif self.path.endswith('.css'):
            self.load_css()
        elif self.path.endswith('.js'):
            self.load_js()
        elif self.path == '/stream.mjpg':
            self.stream_camera()
        elif self.path.startswith('/robot?'):
            self.move_vehicle()
        elif self.path.startswith('/camera?'):
            self.turn_camera()
        else:
            self._return_error()

    def move_vehicle(self):
        direction, movement, key = self._extract_param()
        print('direction -> ' + direction)
        print('movement -> ' + movement)
        print('key -> ' + key)
        vehicle_controls.move(direction, movement)
        self._set_common_headers('', len(''))

    def turn_camera(self):
        direction, movement, key = self._extract_param()
        print('direction -> ' + direction)
        print('movement -> ' + movement)
        print('key -> ' + key)
        camera_controls.turn(direction, movement)
        self._set_common_headers('', len(''))

    def load_js(self):
        content = self._read_file(constants.DIR_JS + self.path)
        self._set_common_headers(constants.CONTENT_TYPE_JS, len(content))
        self.wfile.write(content)
    
    def load_css(self):
        content = self._read_file(constants.DIR_CSS + self.path)
        self._set_common_headers(constants.CONTENT_TYPE_CSS, len(content))
        self.wfile.write(content)

    def open_html(self):
        content = self._read_file(constants.DIR_HTML + self.path)
        self._set_common_headers(constants.CONTENT_TYPE_HTML, len(content))
        self.wfile.write(content)

    def stream_camera(self):
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header(constants.HEADER_CONTENT_TYPE, constants.CONTENT_TYPE_MULTIPART)
        self.end_headers()
       
        try:
            while True :
                with output.condition:
                     output.condition.wait()
                     frame = output.frame
                self.wfile.write(b'--FRAME\r\n')
                self.send_header(constants.HEADER_CONTENT_TYPE, constants.CONTENT_TYPE_JPEG)
                self.send_header(constants.HEADER_CONTENT_LENGTH, len(frame))
                self.end_headers()
                self.wfile.write(frame)
                self.wfile.write(b'\r\n')
        except Exception as e:
            logging.warning('Removed streaming client %s: %s',self.client_address, str(e))

    def _redirect(self):
        self.send_response(301)
        self.send_header('Location', '/index.html')
        self.end_headers()

    def _read_file(self, path):
        file = open(path,'rb') # open file , r => read , b => byte format
        content = file.read()
        file.close()
        return content

    def _set_common_headers(self, contentType, contentLength):
        self.send_response(200)
        self.send_header(constants.HEADER_CONTENT_TYPE, contentType)
        self.send_header(constants.HEADER_CONTENT_LENGTH, contentLength)
        self.end_headers()
    
    def _extract_param(self):
        parametersStr = self.path.split('?')
        parametersList = parametersStr[1].split('&')
        direction = parametersList[0].split('=')[1]
        movement = parametersList[1].split('=')[1]
        key = parametersList[2].split('=')[1]
        return direction, movement, key

    def _return_error(self):
        self.send_error(404)
        self.end_headers()
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    camera.rotation = 180
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
