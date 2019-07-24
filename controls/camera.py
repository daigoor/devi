#!/usr/bin/env python
"""camera.py: controls all the movements of the camera motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import sys
import RPi.GPIO as GPIO
import time

servoPINUD = 15
servoPINLR = 37

PWMHz = 50
pwds=7.5


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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPINUD, GPIO.OUT)
    GPIO.setup(servoPINLR, GPIO.OUT)
    pwm = GPIO.PWM(servoPINUD, PWMHz) # GPIO 17 for PWM with 50Hz
    pwm.start(pwds) # Initialization
    pwm.ChangeDutyCycle(12.5)

def turn_down():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPINUD, GPIO.OUT)
    GPIO.setup(servoPINLR, GPIO.OUT)
    pwm = GPIO.PWM(servoPINUD, PWMHz) # GPIO 17 for PWM with 50Hz
    pwm.start(pwds) # Initialization
    pwm.ChangeDutyCycle(2.5)

def turn_right():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPINUD, GPIO.OUT)
    GPIO.setup(servoPINLR, GPIO.OUT)
    pwm = GPIO.PWM(servoPINLR, PWMHz) # GPIO 17 for PWM with 50Hz
    pwm.start(pwds) # Initialization
    pwm.ChangeDutyCycle(12.5)

def turn_left():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPINUD, GPIO.OUT)
    GPIO.setup(servoPINLR, GPIO.OUT)
    pwm = GPIO.PWM(servoPINLR, PWMHz) # GPIO 17 for PWM with 50Hz
    pwm.start(pwds) # Initialization
    pwm.ChangeDutyCycle(4)

def _stop():
    """STOP ALL KIND OF MOVEMENTS"""


if __name__ == "__main__":
    main()
