#!/usr/bin/env python

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
        print '''please enter params (python motormotioncommands.py up true)'''
        return

    direction = sys.argv[1:][0]
    movement = sys.argv[1:][1]

    initmotorpins() 

    if movement != 'false':
        if direction == 'up':
            moveforward()
        elif direction == 'down':
            movebackwards()
        if direction == 'right':
            turnright()
        elif direction == 'left':
            turnleft()

    print movement

    return 200


def initmotorpins():
    """init pins"""
    #Set pins as outputs 
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RIGHT1, GPIO.OUT)
    GPIO.setup(RIGHT2, GPIO.OUT)
    GPIO.setup(LEFT1, GPIO.OUT)
    GPIO.setup(LEFT2, GPIO.OUT)
    stop()

# Note: Output arrangement is important to make sure there is no jitter
# in the motors when moving Forwards/Backwards

def moveforward():
    """init pins"""
    print 'moveforward'
    GPIO.output(RIGHT1, GPIO.HIGH)
    GPIO.output(LEFT1, GPIO.HIGH)
    GPIO.output(RIGHT2, GPIO.LOW)
    GPIO.output(LEFT2, GPIO.LOW)

def movebackwards():
    """move backwards"""
    print 'movebackwards'
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.HIGH)

# Note: Output arrangement is important to make sure there is no jitter
# in the motors when turning Right/Left

# Rotation is done by reversing the right motor, while other motors are off
# and therefore doing a circle turn right.

def turnright():
    """move to the right"""
    print 'turnright'
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.LOW)

def turnleft():
    """move to the left"""
    print 'turnleft'
    GPIO.output(RIGHT1, GPIO.LOW)
    GPIO.output(LEFT1, GPIO.LOW)
    GPIO.output(RIGHT2, GPIO.LOW)
    GPIO.output(LEFT2, GPIO.HIGH)

def stop():
    """STOP ALL KIND OF MOVEMENTS"""
    GPIO.output(RIGHT1, GPIO.HIGH)
    GPIO.output(LEFT1, GPIO.HIGH)
    GPIO.output(RIGHT2, GPIO.HIGH)
    GPIO.output(LEFT2, GPIO.HIGH)

if __name__ == "__main__":
    main()
