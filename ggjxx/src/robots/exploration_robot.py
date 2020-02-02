from .base_robot import BaseRobot

class ExplorationRobot(BaseRobot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.renderCharConstant = '1'