#!/usr/bin/env python
"""server.py: SERVER."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import io
import logging
import socketserver
from threading import Condition
from http import server

from route import StreamingHandler

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

address = ('', 8000)
server = StreamingServer(address, StreamingHandler)
server.serve_forever()
