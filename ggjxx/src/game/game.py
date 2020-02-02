from .cell import Cell
from .constants import UP,DOWN,RIGHT,LEFT
from ..structure.levels.base_level import BaseLevel
from .map import Map


class Game:
    def __init__(self, gameLevel):
        self.initialGameLevel = gameLevel

    def restart(self):
        self.map = self.initialGameLevel.getMap()
        self.turns_left = self.initialGameLevel.getMaxTurns()
        self.robots = self.initialGameLevel.getRobots()
        self.choose_robot(self.robots[0])

    def setRobots(self, robots):
        self.robots = robots

    def get_map(self):
        return self.map

    def get_controlled_robot(self):
        return self.controlled_robot

    def switchControlledRobot(self):
        for i in range(len(self.robots)):
            if self.robots[i].is_being_controlled:
                pos = i
                self.robots[i].is_being_controlled = False
        if pos+1 == len(self.robots):
            newPos = 0
        else:
            newPos = pos+1
        self.choose_robot(self.robots[newPos])

    
    def won(self):
        # check win condition
        return False

    def lost(self):
        return self.turns_left > 0

    def available_robots(self):
        return filter(lambda r: not r.busy, self.map.get_robots())

    def choose_robot(self, robot):
        robot.is_being_controlled = True
        self.controlled_robot = robot

    def is_robot_being_controlled(self):
        return self.controlled_robot != None

    def go_left(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(LEFT):
            r.x -= 1
        self.checkHazards(r)

    def go_right(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(RIGHT):
            r.x += 1
        self.checkHazards(r)

    def go_down(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(DOWN):
            r.y += 1
        self.checkHazards(r)

    def go_up(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(UP):
            r.y -= 1
        self.checkHazards(r)

    def checkHazards(self, robot):
        xPosition = robot.getX()
        yPosition = robot.getY()
        currentCell = self.map.getCell(robot.getX(), robot.getY())
        cells = self.getAdjacentCells(xPosition, yPosition)
        for cell in cells:
            if cell.hasRadiation():
                robot.interactWithRadiation(self,currentCell)
            if cell.hasFire():
                robot.interactWithFire(self, currentCell)


    def getAdjacentCells(self,x,y):
        center = self.map.getCell(x,y)
        allCells = [center]
        
        if (center.canGo(UP)):
            allCells.append(self.map.getCell(x, y-1))
        if (center.canGo(DOWN)):
            allCells.append(self.map.getCell(x, y+1))
        if (center.canGo(LEFT)):
            allCells.append(self.map.getCell(x-1, y))
        if (center.canGo(RIGHT)):
            allCells.append(self.map.getCell(x+1, y))

        return allCells

    def killRobot(self, robot):
        robot.resetPosition()

    def robot_action(self):
        pass

    def end_turn(self):
        self.turns_left -= 1
        self.controlled_robot.is_being_controlled = False
        self.controlled_robot = None

    def willShutdown(self):
        return self.turns_left < 0

    def terminate(self):
        exit()
        self.turns_left = -1

    def finished(self):
        return False
