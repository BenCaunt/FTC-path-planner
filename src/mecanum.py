'''

mecanum.py

written by Ben Caunt

programs purpose is to represent a holonomic mecanum robot to be used for simulation


'''

from position import position, angleWrap
import math

def positionFromList(ls):
    return position(ls[0],ls[1],0)

class mecanumRobot:
    def __init__(self, pose = position(0,0,0), velocity = position(0,0,0), robotImage = None):
        self.pose = pose
        self.velocity = velocity
        self.size = 18 # 18 inch robot
        self.sizeToPixel = self.size * 1000
        self.robotImage = robotImage
        self.translationalXAcceleration = 0
        self.translationalYAcceleration = 0
        self.rotationalAcceleration = 0
        self.maxTranslationalAcceleration = 10
        self.maxRotationalAcceleration = 10
        self.KpTranslation = 0.03
        self.KpRotation = 0.025

    def draw(self, canvas):
        '''
        draw robot using simplegui
        '''

        if self.pose is None:
            print("self.pose is none for some reason")
            self.pose = position(0,0,0)

        canvas.draw_image(self.robotImage, (575 / 2, 575 / 2), (575, 575), self.pose.toList(), (575 / 6 ,575 / 6), self.pose.radians)

    def moveToPosition(self, targetPose):
        errorX = (targetPose.x - self.pose.x) * self.KpTranslation
        errorY = (targetPose.y - self.pose.y)  * self.KpTranslation
        errorTheta = angleWrap(targetPose.radians - self.pose.radians) * self.KpRotation
        self.pose += position(errorX, errorY, errorTheta)
