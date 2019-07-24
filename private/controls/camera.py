#!/usr/bin/env python
"""camera.py: controls all the movements of the camera motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import sys
import RPi.GPIO as GPIO
import time

servoPINUD = 22
servoPINLR = 26

step = 0.5
PWMHz = 50

file_lr = 'lrp.d'
file_ud = 'udp.d'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINUD, GPIO.OUT)
GPIO.setup(servoPINLR, GPIO.OUT)

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
    pwm = GPIO.PWM(servoPINUD, PWMHz) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_ud)
    pwm.start(position) # Initialization
    new_position = float(position) + float(step)
    pwm.ChangeDutyCycle(new_position)
    _write_file(file_ud, new_position)
    # time.sleep(0.5)

def turn_down():
    pwm = GPIO.PWM(servoPINUD, PWMHz) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_ud)
    pwm.start(position) # Initialization
    sum = float(position) - float(step)
    pwm.ChangeDutyCycle(sum)
    _write_file(file_ud, sum)

def turn_right():
    pwm = GPIO.PWM(servoPINLR, PWMHz) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_lr)
    pwm.start(position) # Initialization
    new_position = float(position) + float(step)
    pwm.ChangeDutyCycle(new_position)
    _write_file(file_lr, new_position)

def turn_left():
    pwm = GPIO.PWM(servoPINLR, PWMHz) # GPIO 17 for PWM with 50Hz
    position = _read_file(file_lr)
    pwm.start(position) # Initialization
    new_position = float(position) - float(step)
    pwm.ChangeDutyCycle(new_position)
    _write_file(file_lr, new_position)

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
