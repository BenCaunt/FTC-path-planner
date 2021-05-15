'''

position.py

written by Ben Caunt

programs purpose is to provide a custom datatype for storing Pose information


'''

import math
import numpy as np

def angleWrap(radians):
    while radians > math.pi:
        radians -= 2 * math.pi
    while radians < -math.pi:
        radians += 2 * math.pi
    return radians

class position:
    def __init__(self, x, y, radians = 0):
        self.x = x
        self.y = y
        self.radians = radians

    def rotateBy(self, origin):
        s = math.sin(origin.radians)
        c = math.cos(origin.radians)
        xDifference = self.x - origin.x
        yDifference = self.y - origin.y

        rotatedX = xDifference * c - yDifference * s
        rotatedY = xDifference * s + yDifference * c

        return position(rotatedX + origin.x,rotatedY+ origin.y,self.radians)

    def toList(self):
        return [self.x, self.y]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radians = angleWrap(self.radians + other.radians)
        return position(x,y,radians)

    def __str__(self):
        return f"x: {self.x} y: {self.y} theta: {self.radians}"

    def distanceToPosition(self,other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))

    def copy(self):
        return position(self.x, self.y, self.radians)

    def scaleVector(self, scaler):
        return position(self.x * scaler, self.y * scaler, self.radians)
    def swapAxis(self):
        return position(self.y, self.x, self.radians)
    def toRoadrunnerCoordinates(self, FRAME_SIZE):
        conversion = (6*12) / (FRAME_SIZE/2)
        new = position(self.x - (FRAME_SIZE / 2),self.y - (FRAME_SIZE / 2),self.radians)
        new = position(-new.x,-new.y,new.radians)
        new = new.swapAxis()
        return new.scaleVector(conversion)
