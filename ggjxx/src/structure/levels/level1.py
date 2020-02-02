from .base_level import BaseLevel
from ...robots.exploration_robot import ExplorationRobot
from ...robots.fire_fighter_robot import FireFighterRobot
from ...robots.radiation_fighter_robot import RadiationFighterRobot
from ...game.map import Map
from ...game.constants import *

class Level1(BaseLevel):
    def __init__(self):
        self.robots = [ExplorationRobot(1, 2), FireFighterRobot(0,7), RadiationFighterRobot(7,0)]
        self.map = Map(8, 8, self.robots, 0,7)
        self.map.get_cell(0,0).setAvailableDirections([DOWN])
        self.map.get_cell(0,1).setAvailableDirections([DOWN,UP])
        self.map.get_cell(0,2).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(0,3).setAvailableDirections([DOWN,RIGHT])
        self.map.get_cell(0,4).setAvailableDirections([UP,RIGHT,DOWN])
        self.map.get_cell(0,5).setAvailableDirections([UP,RIGHT,DOWN])
        self.map.get_cell(0,6).setAvailableDirections([UP,DOWN])
        self.map.get_cell(0,7).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(1,0).setAvailableDirections([DOWN])
        self.map.get_cell(1,1).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(1,2).setAvailableDirections([RIGHT,LEFT])
        self.map.get_cell(1,3).setAvailableDirections([LEFT,DOWN])
        self.map.get_cell(1,4).setAvailableDirections([UP,DOWN,RIGHT,LEFT])
        self.map.get_cell(1,5).setAvailableDirections([UP,DOWN,LEFT])
        self.map.get_cell(1,6).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(1,7).setAvailableDirections([RIGHT,LEFT])
        self.map.get_cell(2,0).setAvailableDirections([DOWN])
        self.map.get_cell(2,1).setAvailableDirections([UP,DOWN,LEFT])
        self.map.get_cell(2,2).setAvailableDirections([UP,DOWN,LEFT])
        self.map.get_cell(2,3).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(2,4).setAvailableDirections([LEFT,DOWN])
        self.map.get_cell(2,5).setAvailableDirections([UP,DOWN])
        self.map.get_cell(2,6).setAvailableDirections([UP,DOWN,LEFT])
        self.map.get_cell(2,7).setAvailableDirections([UP,RIGHT,LEFT])
        self.map.get_cell(3,0).setAvailableDirections([DOWN])
        self.map.get_cell(3,1).setAvailableDirections([UP,RIGHT,DOWN])
        self.map.get_cell(3,2).setAvailableDirections([UP,DOWN])
        self.map.get_cell(3,3).setAvailableDirections([UP,RIGHT,DOWN,LEFT])
        self.map.get_cell(3,4).setAvailableDirections([UP,DOWN])
        self.map.get_cell(3,5).setAvailableDirections([UP,RIGHT,DOWN])
        self.map.get_cell(3,6).setAvailableDirections([UP,DOWN])
        self.map.get_cell(3,7).setAvailableDirections([UP,LEFT])
        self.map.get_cell(4,0).setAvailableDirections([RIGHT,DOWN])
        self.map.get_cell(4,1).setAvailableDirections([UP,RIGHT,DOWN,LEFT])
        self.map.get_cell(4,2).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(4,3).setAvailableDirections([RIGHT,LEFT,DOWN])
        self.map.get_cell(4,4).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(4,5).setAvailableDirections([LEFT,DOWN])
        self.map.get_cell(4,6).setAvailableDirections([UP,DOWN])
        self.map.get_cell(4,7).setAvailableDirections([UP])
        self.map.get_cell(5,0).setAvailableDirections([LEFT,DOWN])
        self.map.get_cell(5,1).setAvailableDirections([UP,LEFT])
        self.map.get_cell(5,2).setAvailableDirections([RIGHT,LEFT])
        self.map.get_cell(5,3).setAvailableDirections([RIGHT,LEFT])
        self.map.get_cell(5,4).setAvailableDirections([LEFT,DOWN])
        self.map.get_cell(5,5).setAvailableDirections([UP,RIGHT,DOWN])
        self.map.get_cell(5,6).setAvailableDirections([UP,DOWN])
        self.map.get_cell(5,7).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(6,0).setAvailableDirections([DOWN])
        self.map.get_cell(6,1).setAvailableDirections([UP,DOWN])
        self.map.get_cell(6,2).setAvailableDirections([UP,LEFT])
        self.map.get_cell(6,3).setAvailableDirections([LEFT,RIGHT,DOWN])
        self.map.get_cell(6,4).setAvailableDirections([UP])
        self.map.get_cell(6,5).setAvailableDirections([LEFT,RIGHT,DOWN])
        self.map.get_cell(6,6).setAvailableDirections([UP,RIGHT])
        self.map.get_cell(6,7).setAvailableDirections([RIGHT,LEFT])
        self.map.get_cell(7,0).setAvailableDirections([DOWN])
        self.map.get_cell(7,1).setAvailableDirections([DOWN,UP])
        self.map.get_cell(7,2).setAvailableDirections([UP,DOWN])
        self.map.get_cell(7,3).setAvailableDirections([UP,LEFT])
        self.map.get_cell(7,4).setAvailableDirections([DOWN])
        self.map.get_cell(7,5).setAvailableDirections([UP,LEFT])
        self.map.get_cell(7,6).setAvailableDirections([LEFT])
        self.map.get_cell(7,7).setAvailableDirections([LEFT])

        self.map.get_cell(1,4).setOnFire()
        self.map.get_cell(5,0).setOnFire()
        self.map.get_cell(7,4).setOnFire()
        self.map.get_cell(0,0).putRadiation()
        self.map.get_cell(4,7).putRadiation()
        self.map.get_cell(3,3).putRadiation()
        self.map.get_cell(6,4).putRadiation()
        self.map.get_cell(7,7).putRadiation()
        self.map.get_cell(6,1).putRadiation()

        self.max_turns = 10
        # self.gameState = Game(map, max_turns, robots)
        # self.gameState.setRobots(robots)