'''

positionMaker.py

written by Ben Caunt

programs purpose is to create points for the robot to follow using mouse clicks

'''
from enum import Enum
import math
from position import position, angleWrap
from time import sleep

class positionMakingStates(Enum):
    IDLE = 1
    SET_POSITION = 2
    SET_ANGLE = 3

class positionMaker:
    def __init__(self, pathObject):
        self.pathObject = pathObject
        self.positionMakerState = positionMakingStates.IDLE
        self.currentPosition = position(0,0,0)
        self.replaceThreshold = 30
    def onClick(self, pos):

        if self.positionMakerState == positionMakingStates.IDLE:
            self.positionMakerState = positionMakingStates.SET_POSITION
        # set the x,y position of the point
        if (self.positionMakerState == positionMakingStates.SET_POSITION):
            print(pos)
            self.currentPosition = self.currentPosition.copy()
            self.currentPosition.x = pos[0]
            self.currentPosition.y = pos[1]
            self.positionMakerState = positionMakingStates.SET_ANGLE
        # set the angle of the point
        elif (self.positionMakerState == positionMakingStates.SET_ANGLE):
            self.pathObject.reset()
            x,y = pos
            angle = math.pi - math.atan2(x - self.currentPosition.x,
                                        y - self.currentPosition.y)
            self.currentPosition.radians = angle

            replacedOtherPoint = False
            if not not self.pathObject.pathPoints:
                for i, position in enumerate(self.pathObject.pathPoints):
                    if position.distanceToPosition(self.currentPosition) < self.replaceThreshold:
                        replacedOtherPoint = True
                        self.pathObject.pathPoints[i] = self.currentPosition
                        continue
            if not replacedOtherPoint:
                self.pathObject.pathPoints.append(self.currentPosition)

            self.positionMakerState = positionMakingStates.SET_POSITION
