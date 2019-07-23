#!/usr/bin/env python
"""camera.py: controls all the movements of the camera motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import sys
import RPi.GPIO as GPIO
import time

servoPINUD = 22
servoPINLR = 26

file_lr = 'lrp.d'
file_ud = 'udp.d'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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
    servoPIN = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 10) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_ud)
    print(position)
    p.start(position) # Initialization
    sum = float(position) + float(1)
    p.ChangeDutyCycle(sum)
    _write_file(file_ud, sum)
    time.sleep(0.5)

def turn_down():
    servoPIN = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 10) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_ud)
    print(position)
    p.start(position) # Initialization
    sum = float(position) - float(1)
    p.ChangeDutyCycle(sum)
    _write_file(file_ud, sum)
    time.sleep(0.5)

def turn_right():
    servoPIN = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 10) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_lr)
    print(position)
    p.start(position) # Initialization
    p.ChangeDutyCycle(1)
    time.sleep(0.5)


def turn_left():
    servoPIN = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 10) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_lr)
    print(position)
    p.start(position) # Initialization
    p.ChangeDutyCycle(1)
    time.sleep(0.5)

def _stop():
    """STOP ALL KIND OF MOVEMENTS"""

def _read_file(path):
    file = open(path,'rb') # open file , r => read , b => byte format
    value = file.read()
    file.close()
    return float(value)

def _write_file(path, value):
    file = open(path,'w') # open file , r => read , b => byte format
    file.write(str(value)) 
    file.close()

if __name__ == "__main__":
    main()
