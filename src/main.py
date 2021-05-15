'''

main.py

written by Ben Caunt

programs purpose is to be the entry point of the program and is what the user runs.

'''


import simpleguitk as simplegui
from mecanum import mecanumRobot
from position import position
from path import path
import math
import pyautogui
from positionMaker import positionMaker

isVisualizing = False
isDrawingLines = False

def runRobot():
    global isVisualizing
    isVisualizing = not isVisualizing

def toggleLines():
    global isDrawingLines
    isDrawingLines = not isDrawingLines

def deletePath():
    robotPath.pathPoints = []


FRAME_SIZE = 600

INCHES_TO_PIXEL = (600/2) / (6*12)


field = simplegui.load_image('https://preview.redd.it/34dkt25hk1n51.png?width=5000&format=png&auto=webp&s=d33797ae15eadc10f3084b3dd8bc53d2ceef8a33')

robotImg = simplegui.load_image('https://i.ibb.co/0JZBPnM/drivetrain-Full-PNG.png')

robot = mecanumRobot(position(0,0,math.radians(0)), position(0,0,0), robotImg)

robotPath = path()

clickToAddPosition = positionMaker(robotPath)


def draw(canvas):
    canvas.draw_image(field, (5000 / 2, 5000 / 2), (5000,5000), (FRAME_SIZE / 2,FRAME_SIZE / 2), (FRAME_SIZE,FRAME_SIZE))
    if not not robotPath.pathPoints:
        if isDrawingLines:
            for i in range(1,len(robotPath.pathPoints)):
                canvas.draw_line(robotPath.pathPoints[i - 1].toList(), robotPath.pathPoints[i].toList(), 6, 'Blue')
        for point in robotPath.pathPoints:
            canvas.draw_circle(point.toList(), 20, 12, 'Green')

    if isVisualizing:
        robot.draw(canvas)
        robotPath.followPath(robot)



if __name__ == "__main__":

    frame = simplegui.create_frame("simulator", FRAME_SIZE, FRAME_SIZE)

    frame.set_mouseclick_handler(clickToAddPosition.onClick)
    frame.add_button("Run Robot!",runRobot)
    frame.add_button("Code Generation",robotPath.generateAutoPath)
    frame.add_button("Toggle Line",toggleLines)
    frame.add_button("Reset Path",deletePath)
    frame.set_draw_handler(draw)
    frame.start()
