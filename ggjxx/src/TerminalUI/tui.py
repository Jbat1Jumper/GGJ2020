# ==================================================
# =================== DEPRECATED ===================
# ==================================================

from ..game.game import Game, Map, Robot, FireFighter, RadiationFighter
from ..game.constants import *
from ..input.getch import _Getch

class Tui:

    def init(self):
        self.initGame()
        self.render()
        pass

    def run(self):
        while (not self.gameState.willShutdown()):
            self.updateGame()
        pass

    def teardown(self):
        pass

    def render(self):
        map = self.gameState.get_map()
        # robot = self.gameState.get_robot()
        for y in range(map.getHeight()):
            lines = ['', '', '']
            for x in range(map.getWidth()):
                cell = map.getCell(x, y)
                # newLines = self.renderCell(cell, robot.isInCell(x, y))
                cr = self.gameState.get_controlled_robot()
                robot = cr if cr.x == x and cr.y == y else None
                newLines = self.renderCell(cell, robot)
                lines[0] += newLines[0]
                lines[1] += newLines[1]
                lines[2] += newLines[2]
            lines[0] = lines[0].replace('\\/', '--')
            lines[0] = lines[0].replace('/\\', '--')
            lines[1] = lines[1].replace('\\/', '--')
            lines[1] = lines[1].replace('/\\', '--')
            lines[2] = lines[2].replace('\\/', '--')
            lines[2] = lines[2].replace('/\\', '--')
            print(lines[0])
            print(lines[1])
            print(lines[2])


    def renderCell(self, cell, robot):
        if cell.canGo(LEFT):
            if cell.canGo(UP):
                line1 = ' '
            else:
                line1 = '\\'
            line2 = ' '
            if cell.canGo(DOWN):
                line3 = ' '
            else:
                line3 = '/'
        else:
            if cell.canGo(UP):
                line1 = '|'
            else:
                line1 = '+'
            line2 = '|'
            if cell.canGo(DOWN):
                line3 = '|'
            else:
                line3 = '+'

        if cell.canGo(UP):
            line1 += '   '
        else:
            line1 += '---'

        if cell.canGo(DOWN):
            line3 += '   '
        else:
            line3 += '---'

        if (robot):
            line2 += 'X'
        else:
            line2 += ' '

        if (cell.hasFire()):
            line2 += 'F'
        else:
            line2 += ' '

        if (cell.hasRadiation()):
            line2 += 'R'
        else:
            line2 += ' '

        if cell.canGo(RIGHT):
            if cell.canGo(UP):
                line1 += ' '
            else:
                line1 += '/'
            line2 += ' '
            if cell.canGo(DOWN):
                line3 += ' '
            else:
                line3 += '\\'
        else:
            if cell.canGo(UP):
                line1 += '|'
            else:
                line1 += '+'
            line2 += '|'
            if cell.canGo(DOWN):
                line3 += '|'
            else:
                line3 += '+'

        return (line1, line2, line3)

    def initGame(self):
        robots = [Robot(1, 2), FireFighter(0,7), RadiationFighter(7,0)]
        map = Map(8, 8, robots, 0,7)
        map.get_cell(0,0).setAvailableDirections([DOWN])
        map.get_cell(0,1).setAvailableDirections([DOWN,UP])
        map.get_cell(0,2).setAvailableDirections([UP,RIGHT])
        map.get_cell(0,3).setAvailableDirections([DOWN,RIGHT])
        map.get_cell(0,4).setAvailableDirections([UP,RIGHT,DOWN])
        map.get_cell(0,5).setAvailableDirections([UP,RIGHT,DOWN])
        map.get_cell(0,6).setAvailableDirections([UP,DOWN])
        map.get_cell(0,7).setAvailableDirections([UP,RIGHT])
        map.get_cell(1,0).setAvailableDirections([DOWN])
        map.get_cell(1,1).setAvailableDirections([UP,RIGHT])
        map.get_cell(1,2).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(1,3).setAvailableDirections([LEFT,DOWN])
        map.get_cell(1,4).setAvailableDirections([UP,DOWN,RIGHT,LEFT])
        map.get_cell(1,5).setAvailableDirections([UP,DOWN,LEFT])
        map.get_cell(1,6).setAvailableDirections([UP,RIGHT])
        map.get_cell(1,7).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(2,0).setAvailableDirections([DOWN])
        map.get_cell(2,1).setAvailableDirections([UP,DOWN,LEFT])
        map.get_cell(2,2).setAvailableDirections([UP,DOWN,LEFT])
        map.get_cell(2,3).setAvailableDirections([UP,RIGHT])
        map.get_cell(2,4).setAvailableDirections([LEFT,DOWN])
        map.get_cell(2,5).setAvailableDirections([UP,DOWN])
        map.get_cell(2,6).setAvailableDirections([UP,DOWN,LEFT])
        map.get_cell(2,7).setAvailableDirections([UP,RIGHT,LEFT])
        map.get_cell(3,0).setAvailableDirections([DOWN])
        map.get_cell(3,1).setAvailableDirections([UP,RIGHT,DOWN])
        map.get_cell(3,2).setAvailableDirections([UP,DOWN])
        map.get_cell(3,3).setAvailableDirections([UP,RIGHT,DOWN,LEFT])
        map.get_cell(3,4).setAvailableDirections([UP,DOWN])
        map.get_cell(3,5).setAvailableDirections([UP,RIGHT,DOWN])
        map.get_cell(3,6).setAvailableDirections([UP,DOWN])
        map.get_cell(3,7).setAvailableDirections([UP,LEFT])
        map.get_cell(4,0).setAvailableDirections([RIGHT,DOWN])
        map.get_cell(4,1).setAvailableDirections([UP,RIGHT,DOWN,LEFT])
        map.get_cell(4,2).setAvailableDirections([UP,RIGHT])
        map.get_cell(4,3).setAvailableDirections([RIGHT,LEFT,DOWN])
        map.get_cell(4,4).setAvailableDirections([UP,RIGHT])
        map.get_cell(4,5).setAvailableDirections([LEFT,DOWN])
        map.get_cell(4,6).setAvailableDirections([UP,DOWN])
        map.get_cell(4,7).setAvailableDirections([UP])
        map.get_cell(5,0).setAvailableDirections([LEFT,DOWN])
        map.get_cell(5,1).setAvailableDirections([UP,LEFT])
        map.get_cell(5,2).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(5,3).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(5,4).setAvailableDirections([LEFT,DOWN])
        map.get_cell(5,5).setAvailableDirections([UP,RIGHT,DOWN])
        map.get_cell(5,6).setAvailableDirections([UP,DOWN])
        map.get_cell(5,7).setAvailableDirections([UP,RIGHT])
        map.get_cell(6,0).setAvailableDirections([DOWN])
        map.get_cell(6,1).setAvailableDirections([UP,DOWN])
        map.get_cell(6,2).setAvailableDirections([UP,LEFT])
        map.get_cell(6,3).setAvailableDirections([LEFT,RIGHT,DOWN])
        map.get_cell(6,4).setAvailableDirections([UP])
        map.get_cell(6,5).setAvailableDirections([LEFT,RIGHT,DOWN])
        map.get_cell(6,6).setAvailableDirections([UP,RIGHT])
        map.get_cell(6,7).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(7,0).setAvailableDirections([DOWN])
        map.get_cell(7,1).setAvailableDirections([DOWN,UP])
        map.get_cell(7,2).setAvailableDirections([UP,DOWN])
        map.get_cell(7,3).setAvailableDirections([UP,LEFT])
        map.get_cell(7,4).setAvailableDirections([DOWN])
        map.get_cell(7,5).setAvailableDirections([UP,LEFT])
        map.get_cell(7,6).setAvailableDirections([LEFT])
        map.get_cell(7,7).setAvailableDirections([LEFT])

        map.get_cell(1,4).setOnFire()
        map.get_cell(5,0).setOnFire()
        map.get_cell(7,4).setOnFire()
        map.get_cell(0,0).putRadiation()
        map.get_cell(4,7).putRadiation()
        map.get_cell(3,3).putRadiation()
        map.get_cell(6,4).putRadiation()
        map.get_cell(7,7).putRadiation()
        map.get_cell(6,1).putRadiation()

        max_turns = 10
        self.gameState = Game(map, max_turns, robots)
        self.gameState.setRobots(robots)

    def updateGame(self):
        self.applyActionByInput()
        self.render()

    def applyActionByInput(self):
        inkey = _Getch()
        key_pressed = inkey()
        if (key_pressed == UP_KEY_CHAR):
            self.gameState.go_up()
        if (key_pressed == DOWN_KEY_CHAR):
            self.gameState.go_down()
        if (key_pressed == RIGHT_KEY_CHAR):
            self.gameState.go_right()
        if (key_pressed == LEFT_KEY_CHAR):
            self.gameState.go_left()
        if (key_pressed == QUIT_KEY_CHAR):
            self.gameState.terminate()
        if (key_pressed == CHANGE_ROBOT_KEY):
            self.gameState.switchControlledRobot()

