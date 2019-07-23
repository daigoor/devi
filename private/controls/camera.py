#!/usr/bin/env python
"""camera.py: controls all the movements of the camera motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import sys
import subprocess

def main():
    """Main runnable method"""

    if (sys.argv).__len__() < 2:
        print('please enter params [left|right|up|down]')
        return

    direction = sys.argv[1:][0]
    movement = sys.argv[1:][1]

    if movement != 'false':
        if direction == 'up':
            turn_up()
        elif direction == 'down':
            turn_down()
        if direction == 'right':
            turn_right()
        elif direction == 'left':
            turn_left()

    return 200

def turn_up():
    subprocess.call('crc/rotateCam.sh up'.split())


def turn_down():
    subprocess.call('crc/rotateCam.sh down'.split())


def turn_right():
    subprocess.call('crc/rotateCam.sh right'.split())
    

def turn_left():
    subprocess.call('crc/rotateCam.sh left'.split())

def _stop():
    """STOP ALL KIND OF MOVEMENTS"""
  

if __name__ == "__main__":
    if(not constants.DEBUG):
        main()
