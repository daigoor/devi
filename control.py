#!/usr/bin/env python
"""control.py: controls all the movements of the vehicle & camera motors."""

__author__      = "DaiGooR"
__copyright__   = "Copyright 2019, DaiGooR"

import constants
import controls.vehicle as vehicle
import controls.camera as camera

class Vehicle():
    def move(self, direction, movement):
        vehicle.reset()
        if movement != constants.MOVEMENT_DISABLED:
            if direction == constants.MOVE_UP:
                vehicle.move_forward()
            elif direction == constants.MOVE_DOWN:
                vehicle.move_backwards()
            if direction == constants.MOVE_RIGHT:
                vehicle.move_right()
            elif direction == constants.MOVE_LEFT:
                vehicle.move_left()

class Camera():  
    def turn(self, direction, movement):
        if movement != constants.MOVEMENT_DISABLED:
            if direction == constants.MOVE_UP:
                camera.turn_up()
            elif direction == constants.MOVE_DOWN:
                camera.turn_down()
            if direction == constants.MOVE_RIGHT:
                camera.turn_right()
            elif direction == constants.MOVE_LEFT:
                camera.turn_left()