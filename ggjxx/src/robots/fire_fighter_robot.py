from .base_robot import BaseRobot

class FireFighterRobot(BaseRobot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.renderCharConstant = '2'

    def interactWithFire(self, game, cell):
        cell.putOutFire()