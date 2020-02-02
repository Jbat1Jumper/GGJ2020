from .base_robot import BaseRobot

class RadiationFighterRobot(BaseRobot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.renderCharConstant = '3'

    def interactWithRadiation(self, game, cell):
        cell.putOutRadiation()