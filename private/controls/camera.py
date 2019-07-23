#!/usr/bin/env python

import sys
import subprocess

def main():
    """Main runnable method"""

    if (sys.argv).__len__() < 3:
        print '''please enter params (python motormotioncommands.py up true)'''
        return

    direction = sys.argv[1:][0]
    movement = sys.argv[1:][1]

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


# Note: Output arrangement is important to make sure there is no jitter
# in the motors when moving Forwards/Backwards

def moveforward():
    """init pins"""
    print 'moveforward'
    subprocess.call('crc/rotateCam.sh up'.split())


def movebackwards():
    """move backwards"""
    print 'movebackwards'
    subprocess.call('crc/rotateCam.sh down'.split())


# Note: Output arrangement is important to make sure there is no jitter
# in the motors when turning Right/Left

# Rotation is done by reversing the right motor, while other motors are off
# and therefore doing a circle turn right.

def turnright():
    """move to the right"""
    print 'turnright'
    subprocess.call('crc/rotateCam.sh right'.split())
    

def turnleft():
    """move to the left"""
    print 'turnleft'
    subprocess.call('crc/rotateCam.sh left'.split())

def stop():
    """STOP ALL KIND OF MOVEMENTS"""
  

if __name__ == "__main__":
    main()
