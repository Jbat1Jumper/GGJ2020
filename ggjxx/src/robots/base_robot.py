from ..game.constants import *


class BaseRobot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = '_'
        self.busy = False
        self.is_being_controlled = False
        self.initX = x
        self.initY = y
        self.direction = UP
        self.renderCharConstant = 'X'

    def action(self, map):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, _x):
        self.x = _x

    def setY(self, _y):
        self.y = _y

    def advance(self):
        if self.direction == LEFT:
            self.x -= 1
        elif self.direction == RIGHT:
            self.x += 1
        elif self.direction == DOWN:
            self.y += 1
        elif self.direction == UP:
            self.y -= 1

    def resetPosition(self):
        self.setX(self.initX)
        self.setY(self.initY)

    def interactWithRadiation(self, game, cell):
        game.killRobot(self)

    def interactWithFire(self, game, cell):
        game.killRobot(self)

    def interactWithReactor(self, game, cell):
        if (cell.reactorIsFaulty()):
            game.killRobot(self)

    def render(self):
        return self.renderCharConstant