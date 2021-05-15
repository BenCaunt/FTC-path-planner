'''

path.py

written by Ben Caunt

An easy way of managing lists of positions's as well as performing code generation

'''

from position import position

class path:
    def __init__(self):
        self.pathPoints = []
        self.pathIndex = 0
        self.followDistance = 5
    def addPoint(self, point):
        if self.pathPoints is not None:
            self.pathPoints.append(point)
        else:
            self.pathPoints = [point]

    def followPath(self, robot):
        if self.pathPoints is not None and not not self.pathPoints:

            currentPoint = self.pathPoints[self.pathIndex]

            robot.moveToPosition(currentPoint)

            notAtLastPoint = self.pathIndex != len(self.pathPoints) - 1

            if robot.pose.distanceToPosition(currentPoint) < self.followDistance and self.pathIndex != len(self.pathPoints) - 1:
                self.pathIndex += 1
            elif robot.pose.distanceToPosition(currentPoint) < self.followDistance and self.pathIndex == len(self.pathPoints) - 1:
                self.pathIndex = 0
                robot.pose = self.pathPoints[self.pathIndex]

    def reset(self):
        self.pathIndex = 0

    def thermalPointSyntax(self,position):
        return f"new driveToPositionAction(new Vector3D({position.x},{position.y},{position.radians}),robot)"
    def generateAutoPath(self):
        for point in self.pathPoints:
            print(f"actions.add({self.thermalPointSyntax(point.toRoadrunnerCoordinates(600))});")
