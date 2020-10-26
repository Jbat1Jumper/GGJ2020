from .cell import Cell
from .constants import UP, DOWN, RIGHT, LEFT, MOVEMENT_NOT_ALLOWED, MOVEMENT_DONE, KILL_ROBOT
from ..structure.levels.base_level import BaseLevel
from .map import Map
from copy import deepcopy


class Game:
    def __init__(self, gameLevel):
        self.initialGameLevel = gameLevel
        self.listeners = []

    def restart(self):
        gameLevel = deepcopy(self.initialGameLevel)
        self.map = gameLevel.getMap()
        self.turns_left = gameLevel.getMaxTurns()
        self.robots = gameLevel.getRobots()
        self.choose_robot(self.robots[0])
        self._won = False

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
        return self._won

    def checkWin(self):
        if (self._won):
            return True
        if self.everyReactorHasBeenRepaired():
            self.turns_left = 0
            self._won = True
            return True
        return False

    def everyReactorHasBeenRepaired(self):
        return not self.map.hasFaultyReactor()

    def lost(self):
        return self.turns_left <= 0 and not self._won

    def available_robots(self):
        return filter(lambda r: not r.busy, self.map.get_robots())

    def choose_robot(self, robot):
        robot.is_being_controlled = True
        self.controlled_robot = robot

    def is_robot_being_controlled(self):
        return self.controlled_robot != None

    def processTurnAfterMove(self, robot):
        self.consumeTurn()
        self.checkHazards(robot)
        self.checkWin()

    def go(self, direction):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if not self.map.getCell(r.x, r.y).canGo(direction) or not self.turns_left > 0:
            self.trigger_event(MOVEMENT_NOT_ALLOWED)
            return

        r.direction = direction
        r.advance()
        self.trigger_event(MOVEMENT_DONE)
        self.processTurnAfterMove(r)

    def go_left(self):
        self.go(LEFT)

    def go_right(self):
        self.go(RIGHT)

    def go_down(self):
        self.go(DOWN)

    def go_up(self):
        self.go(UP)

    def consumeTurn(self):
        self.turns_left = self.turns_left - 1

    def checkHazards(self, robot):
        xPosition = robot.getX()
        yPosition = robot.getY()
        currentCell = self.map.getCell(robot.getX(), robot.getY())
        cells = self.map.getAdjacentCells(xPosition, yPosition)
        for cell in cells:
            if cell.hasRadiation():
                robot.interactWithRadiation(self, currentCell)
            if cell.hasFire():
                robot.interactWithFire(self, currentCell)
            if cell.hasReactor():
                robot.interactWithReactor(self, currentCell)


    def killRobot(self, robot):
        robot.resetPosition()
        self.trigger_event(KILL_ROBOT)

    def robot_action(self):
        pass

    def end_turn(self):
        self.turns_left -= 1
        self.controlled_robot.is_being_controlled = False
        self.controlled_robot = None

    def terminate(self):
        self.turns_left = -1

    def finished(self):
        return self.turns_left <= 0

    def trigger_event(self, event):
        for listener in self.listeners:
            listener.trigger(event)

    def subscribe(self, listener):
        if not hasattr(listener, "trigger"):
            return
        self.listeners.append(listener)

    def update(self):
        self.update_fog()

    def update_fog(self):
        for robot in self.map.robots:
            x = robot.getX()
            y = robot.getY()

            for cell in self.map.getAdjacentCells(x, y):
                cell.disableFog()

    def getAdjacentCells(self,x,y):
        return self.map.getAdjacentCells(x,y)
