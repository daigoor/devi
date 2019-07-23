#!/usr/bin/env python
"""stream.py: controls the camera output stream."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import io
import logging
import fake_rpi
import socketserver
import constants
from threading import Condition
from http import server

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

if(not constants.DEBUG):
    with fake_rpi.picamera.PiCamera() as camera:
        output = StreamingOutput()
        #Uncomment the next line to change your Pi's Camera rotation (in degrees)
        #camera.rotation = 90
        camera.start_recording(output, format='mjpeg')



