import math
import random
import pylab
import numpy as np

class Position(object):
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

class Room(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = np.zeros((width, height), np.int64)

    def isPositionInRoom(self, pos):
        try:
            index = self.tiles[pos.getY(), pos.getX()]
            return True
        except IndexError:
            return False


class Robot(object):
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name

    def getName(self):
        return self.name


class StandardRobot(Robot):
    def clean(self):
        return self.speed


robot = StandardRobot(300, "Mik")

print(robot.clean())
