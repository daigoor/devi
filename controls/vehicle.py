#!/usr/bin/env python
"""vehicle.py: controls all the movements of the vehicle motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import sys
import RPi.GPIO as GPIO

#Standard Pin Definitions for motor
RIGHT1 = 5
RIGHT2 = 3
LEFT1 = 13
LEFT2 = 11

def main():
    """Main runnable method"""

    if (sys.argv).__len__() < 3:
        print('please enter params [left|right|up|down] [true|false|]')
        return

    direction = sys.argv[1:][0]
    movement = sys.argv[1:][1]

    reset() 

    if movement != 'false':
        if direction == 'up':
            move_forward()
        elif direction == 'down':
            move_backwards()
        if direction == 'right':
            move_right()
        elif direction == 'left':
            move_left()
            
    return 200


def reset():
    """init pins"""
    #Set pins as outputs 
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RIGHT1, GPIO.OUT)
    GPIO.setup(RIGHT2, GPIO.OUT)
    GPIO.setup(LEFT1, GPIO.OUT)
    GPIO.setup(LEFT2, GPIO.OUT)
    _stop()

# Note: Output arrangement is important to make sure there is no jitter
# in the motors when moving Forwards/Backwards

def move_forward():
    GPIO.output(RIGHT1, GPIO.HIGH)
    GPIO.output(LEFT1, GPIO.HIGH)
    GPIO.output(RIGHT2, GPIO.LOW)
    GPIO.output(LEFT2, GPIO.LOW)

def move_backwards():
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.HIGH)

# Rotation is done by reversing the right motor, while other motors are off
# and therefore doing a circle turn right.

def move_right():
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.LOW)

def move_left():
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.LOW)
    GPIO.output(LEFT2, GPIO.HIGH)

def _stop():
    """STOP ALL KIND OF MOVEMENTS"""
    GPIO.output(RIGHT1, GPIO.HIGH)
    GPIO.output(LEFT1, GPIO.HIGH)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.HIGH)

if __name__ == "__main__":
    main()
